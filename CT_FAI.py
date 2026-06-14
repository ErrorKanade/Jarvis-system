import asyncio
import json
import csv
import os
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def load_rig_script_from_csv(file_path="fai_issues.csv"):
    script = []
    if not os.path.exists(file_path):
        return [{"type": "system_error", "text": f"錯誤：找不到數據檔案 {file_path}"}]

    with open(file_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)

        def clean_key(k):
            return k.strip().replace("_", "").replace(" ", "").lower() if k else ""

        headers_map = {
            clean_key(k): k for k in reader.fieldnames} if reader.fieldnames else {}

        def get_value(row_dict, *possible_keys):
            for pk in possible_keys:
                cleaned_pk = clean_key(pk)
                if cleaned_pk in headers_map:
                    return row_dict.get(headers_map[cleaned_pk], "").strip()
            return ""

        for row in reader:
            fai_id = get_value(row, 'fai', 'faino') or "未知 FAI"
            feature = get_value(row, 'Fail Des.', 'item') or "未知項目"
            issue_cat = get_value(row, 'issuecategory',
                                  'issue_category') or "未分類異常"
            fa_raw = get_value(row, 'nextfastep', 'next_fa_step') or ""

            fa_steps = [s for s in fa_raw.replace(
                '\n', ';').split(';') if s.strip()]
            if not fa_steps:
                fa_steps = ["發起通用根因庫檢索排查。"]

            fai_task = {
                "fai_id": fai_id,
                "feature": feature,
                "issue_cat": issue_cat,
                "steps": []
            }

            for idx, step in enumerate(fa_steps):
                fai_task["steps"].append({
                    "query": f"{fai_id} {feature} -> {step[:25]}",
                    "reason": f"執行根因排查步驟 {idx+1}：獲取該工站數據與分佈圖。",
                    "score": f"{0.965 + (idx * 0.005):.3f}",
                    "latency": f"{15 + (idx * 8)}ms",
                    "result": f"召回成功 [{fai_id}_Doc_{idx+1}]: 已完成動作【{step}】並撈取 CPK 參數。"
                })

            script.append(fai_task)

    return script


@app.websocket("/ws/rig")
async def websocket_rig_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        await websocket.receive_text()
        fai_tasks = load_rig_script_from_csv("fai_issues.csv")

        for task in fai_tasks:
            await websocket.send_json({
                "type": "start_new_fai",
                "fai_id": task["fai_id"],
                "feature": task["feature"]
            })
            await asyncio.sleep(0.3)

            intro_text = f"【系統正在分析 {task['fai_id']} ({task['feature']})】。檢測到異常分類為： {task['issue_cat']} 。"
            for char in intro_text:
                await websocket.send_json({"type": "gen_token", "token": char})
                await asyncio.sleep(0.005)  # 高速打字

            for step in task["steps"]:
                await asyncio.sleep(0.5)

                await websocket.send_json({
                    "type": "ret_trigger",
                    "query": step["query"],
                    "reason": step["reason"]
                })

                await asyncio.sleep(0.8)  # 模擬檢索中

                await websocket.send_json({
                    "type": "db_response",
                    "fai_id": task["fai_id"],
                    "score": step["score"],
                    "latency": step["latency"],
                    "result": step["result"]
                })

                await asyncio.sleep(0.5)

            conclusion_text = f" <span class='citation-tag'>{task['fai_id']} 數據鏈注入完成<span class='citation-popup'><b>Insight 數據庫回傳：</b>已完成 {task['fai_id']} 的所有量測值對比與 Breakdown 繪圖分析。</span></span> 數據流已更新，建議團隊優先依據右側召回日誌的集中性結果進行產線排查。<br/>"

            idx = 0
            conclusion_tokens = []
            while idx < len(conclusion_text):
                if conclusion_text[idx] == '<':
                    close_idx = conclusion_text.find('>', idx)
                    if close_idx != -1:
                        conclusion_tokens.append(
                            conclusion_text[idx:close_idx + 1])
                        idx = close_idx + 1
                        continue
                conclusion_tokens.append(conclusion_text[idx])
                idx += 1

            for token in conclusion_tokens:
                await websocket.send_json({"type": "gen_token", "token": token})
                if token.startswith('<'):
                    await asyncio.sleep(0) 
                else:
                    await asyncio.sleep(0.005) 
            await asyncio.sleep(0.8)  
        await websocket.send_json({"type": "status", "value": "done"})

    except WebSocketDisconnect:
        print("連線中斷")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("CT_FAI:app", host="0.0.0.0", port=8000, reload=True)
