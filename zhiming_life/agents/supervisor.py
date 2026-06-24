"""Supervisor agent —— 问诊 + 路由，输出结构化决策。"""

from __future__ import annotations

import json
from dataclasses import dataclass

from zhiming_life import llm
from zhiming_life.prompts import SUPERVISOR_SYSTEM


_BIRTH_FIELDS = ("year", "month", "day", "hour", "calendar")


@dataclass
class Decision:
    reply: str
    route: str            # "bazi" | "ask_more" | "decline"
    birth: dict | None

    @property
    def birth_complete(self) -> bool:
        """五项（年月日时 + 历法）是否都抽到了——「能不能排盘」由代码判，不靠 LLM 自报。"""
        b = self.birth
        return bool(b) and all(b.get(k) is not None for k in _BIRTH_FIELDS)


def decide(messages: list[dict]) -> Decision:
    """跑一轮 supervisor，把自由文本里的 JSON 解析成结构化决策。

    这里求简单，做一次容错解析，解析失败就降级成「再问一句」，不让整轮挂掉。
    要更稳可以换结构化输出 + 重试 + 校验。temperature 略低让 JSON 更稳。
    """
    raw = llm.chat(SUPERVISOR_SYSTEM, messages, temperature=0.3)
    data = _extract_json(raw)
    if data is None:
        return Decision(reply="能再说说你的生辰，或者你想了解什么吗？",
                        route="ask_more", birth=None)
    return Decision(
        reply=data.get("reply", ""),
        route=data.get("route", "ask_more"),
        birth=data.get("birth"),
    )


def _extract_json(text: str) -> dict | None:
    """从可能夹着代码块标记 / 闲话的回复里抠出第一个 JSON 对象。"""
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    try:
        return json.loads(text[start:end + 1])
    except json.JSONDecodeError:
        return None
