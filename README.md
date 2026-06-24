# 知命 · 开源版（zhiming-life）

> [**zhiming.life**](https://zhiming.life) 的开源版——讲清多智能体命理系统的**构建思路**，附一个能跑的**对话 demo**。

## 它给你什么

一个能跑、能改、能学的最小实现：

- **多智能体编排骨架**：问诊分诊（Supervisor）→ 确定性排盘 → 专家解读（Specialist）
- **确定性算法层**：八字排盘 +「算法只给客观事实、评估交给上层」的边界
- **prompt 与 RAG 的结构骨架**
- **一个终端对话 demo**

设计思路见 **[ARCHITECTURE.md](ARCHITECTURE.md)**。

## 快速开始

```bash
pip install -e .
cp .env.example .env        # 填上 API key（默认接 DeepSeek，换任意 OpenAI 兼容端点也行）
python -m zhiming_life
```

报上生辰（公历农历都行）或直接发问，走一遍「问诊 → 排盘 → 解读」。

## 代码导览

```
zhiming_life/
├── conductor.py          ← 先看这个：单轮编排
├── agents/               ← supervisor（问诊+路由）/ bazi_master（解读）
├── core/                 ← bazi.py 排盘 / wuxing.py「只给关系不给方向」
├── prompts/ rag/ vendor/ ← prompt 骨架 / RAG 接口 / 自带历法库
└── cli.py
```

## 说明

最小骨架，非生产级：没有鉴权、限流、持久化、流式。解读质量取决于你接的模型和填入的内容。

## 免责声明

命理内容仅供文化研究与娱乐参考，不构成任何决策建议。信命不认命——命盘揭示倾向，不预设终局。

## License

MIT。

---

<sub>由 [zhiming.life](https://zhiming.life) 维护</sub>
