Jarvis 智能中控管理舱
项目简介
<img width="2560" height="1311" alt="image" src="https://github.com/user-attachments/assets/fb19ffcd-92e1-4855-b662-4c017a6ad250" />

Jarvis 智能中控管理舱是一套面向制造业测试、FA分析（Failure Analysis）、品质监控以及生产数据决策的 AI Agent 平台。

平台以 Large Language Model（LLM）为核心，结合机器视觉、数据分析、知识库检索以及自动化工作流能力，将原本分散的测试系统、分析工具和工程经验整合至统一入口，实现：

AI辅助分析
自动故障诊断
智能决策建议
数据可视化管理
测试流程自动化

最终目标是打造一套具备“数字工程师”能力的智能分析平台。

项目目标

传统测试环境中存在以下问题：

问题	影响
测试系统分散	工程师需要频繁切换工具
数据孤岛	无法形成统一分析
FA经验依赖个人	新人学习成本高
异常判断效率低	影响产线效率
测试结果无法自动闭环	人工介入成本高

因此开发 Jarvis 平台，实现：

数据采集
    ↓
AI分析
    ↓
自动判断
    ↓
原因推理
    ↓
改善建议
    ↓
知识沉淀

形成完整闭环。

系统架构
AI Agent 中央控制层

Jarvis 的核心是 AI Agent Workflow Controller。
<img width="1344" height="410" alt="image" src="https://github.com/user-attachments/assets/2d8b31aa-dee7-4fcc-af06-0cf4d34a38eb" />

作用：

接收用户自然语言指令
调用对应分析模块
自动执行分析流程
汇总结果
输出改善建议

例如：

用户输入：

分析本批次LED亮度异常原因

Agent 自动完成：
<img width="1290" height="130" alt="image" src="https://github.com/user-attachments/assets/2a7499e3-d655-4fd7-b46c-8e47df6b4d12" />

读取数据库
↓
调取检测图像
↓
调用视觉模型
↓
比对历史案例
↓
生成FA报告
↓
输出改善建议

无需人工逐个操作。

首页总览 Dashboard
任务管理

实时展示：

FA分析任务
当前待分析失效案件
<img width="569" height="148" alt="image" src="https://github.com/user-attachments/assets/0f759e29-2add-4ba4-a79a-8e5e7ad2fee8" />

帮助管理层了解：

当前异常数量
AI分析负载
工程资源需求
表单签核任务

显示：
<img width="543" height="154" alt="image" src="https://github.com/user-attachments/assets/8d034547-6cb2-4c06-b903-405b6d675ff9" />

待审批项目

实现：

AI辅助审核
自动流程追踪
待处理任务

显示：
<img width="559" height="147" alt="image" src="https://github.com/user-attachments/assets/ca3ab969-892c-4996-923a-65b01787fd89" />

异常案件
待确认项目

帮助现场快速响应。

已完成任务

显示：
<img width="536" height="148" alt="image" src="https://github.com/user-attachments/assets/85b785dc-da4d-4c86-a61f-90ab1bb0f030" />

AI自动完成分析数量

体现自动化价值。

FA失效分析系统
功能定位

用于失效产品分析（Failure Analysis）。

支持：

CT分析
Gray Spot分析
LED异常分析
声音异常分析
数据关联分析
CT智能分析系统
功能介绍

利用AI视觉模型自动识别：

裂纹
刮伤
气泡
污染
光学异常
工作流程
CT影像
    ↓
图像预处理
    ↓
缺陷检测
    ↓
位置标记
    ↓
异常分类
    ↓
FA建议
功能亮点
多视角同步分析

同时分析：
<img width="1341" height="815" alt="image" src="https://github.com/user-attachments/assets/b7efaae3-6bdc-4cde-abd8-2096ed7c4ace" />

CAM_REAR_01；
CAM_REAR_02；
CAM_REAR_03；
CAM_REAR_04；

自动交叉验证。

缺陷定位

自动标记：

红点位置

工程师无需人工寻找缺陷。

失效占比统计

系统自动统计：
<img width="682" height="577" alt="image" src="https://github.com/user-attachments/assets/444fb60e-f029-42de-87ca-c845d50ed4a0" />

表面微尘
内部刮痕
光学畸变

帮助快速定位主要失效来源。

AI改善建议

例如：

灰度异常集中于中心区域

建议：
1. 检查清洗工艺
2. 检查光学模组校准
3. 对比历史FATP批次

减少工程师分析时间。

Gray Spot识别系统
功能定位

用于光学显示模组灰度异常分析。

AI能力

自动识别：

Gray Spot
Mura
光学不均匀
亮度偏差
分析方式
图像采集
    ↓
灰度增强
    ↓
特征提取
    ↓
缺陷定位
    ↓
异常评分
输出结果

包括：

异常位置
面积比例
严重等级
历史批次对比
LED Issue Analysis
功能定位

LED缺陷自动分类系统。
<img width="2062" height="757" alt="image" src="https://github.com/user-attachments/assets/ac2160be-bc3a-4691-bb3d-c0acf5c13093" />

支持缺陷类型
PASS

正常产品

ALL BLACK

全黑

可能原因：

电源异常
芯片损坏
OUT OF FOCUS

离焦

可能原因：

光学偏移
镜头安装异常
MATERIAL

材料异常

可能原因：

胶体污染
封装缺陷
GLUE OVERFLOW

溢胶

可能原因：

点胶工艺异常
AI视觉分析流程
图像输入
    ↓
预处理
    ↓
特征提取
    ↓
模型推理
    ↓
结果分类
    ↓
可信度计算
输出内容

系统输出：

分类结果
置信度
异常原因
FA建议

例如：

结果：PASS

可信度：
99.8%
数据分析矩阵
功能定位

跨系统数据整合中心

统一整合：

MES
FATP
AOI
ICT
CT
实验室数据
实现价值

过去：

工程师手工整理Excel

现在：

AI自动汇总
自动关联分析
自动发现规律
语音识别分析
功能定位

工程师语音交互入口

支持：

语音下达任务
语音查询结果
语音生成报告

例如：

帮我查询LOT20260524异常原因

Agent自动执行分析。

表单追踪系统
功能定位

追踪：
<img width="2035" height="497" alt="image" src="https://github.com/user-attachments/assets/a8874b04-e1e8-49ad-88ef-222c248e5e41" />

ECN
工程变更
异常单
品质改善单
出货审核单
AI辅助能力

自动：

分类
归档
风险评分
催办提醒
LLM Agent工作流控制器

这是整个系统最重要的部分。

功能

统一调度：

CT系统
Gray Spot系统
LED分析系统
数据库
知识库
MES
ERP
Agent执行流程
用户提问
      ↓
意图识别
      ↓
工具选择
      ↓
执行任务
      ↓
结果汇总
      ↓
生成建议
示例

工程师输入：

分析本批次LED亮度异常

Agent自动：

查询数据库
↓
调取图像
↓
执行视觉模型
↓
分析历史记录
↓
输出结论

整个过程无需人工切换系统。

项目价值
效率提升

预计：

FA分析时间降低70%
知识沉淀

将资深工程师经验转化为：

AI知识库

避免经验流失。

质量提升

通过统一分析平台：

更早发现异常
更快定位问题
更快推动改善
自动化能力

未来目标：

AI发现问题
AI分析问题
AI生成报告
AI提出改善方案
AI追踪改善结果

形成完整智能制造闭环。

项目定位总结

Jarvis 并不是单纯的测试界面，而是一套面向制造业测试与FA分析场景的 AI Agent 中控平台。

其核心价值在于：

将分散的测试系统、视觉检测模型、工程知识库和生产数据整合到统一的 AI Agent 平台中，实现从“发现问题 → 分析问题 → 提出建议 → 知识沉淀”的智能化闭环，大幅提升工程分析效率和制造品质管理能力。
