# rag/ —— 接口在，自己接语料

让解读引经据典靠 RAG。这层只给**接口形状**，语料与检索自己接。

`retriever.py` 是 stub：`retrieve()` 默认返回空字符串，系统照样能跑（师傅靠模型自身知识解读，少了引证那层）。想要引证，自己准备语料、在 TODO 处接上检索。

参考资料只用于触发联想，不作判决依据。

---

<sub>[zhiming.life](https://zhiming.life)</sub>
