from __future__ import annotations

DIAGNOSTIC_ITEM_PREFIXES = (
    "LLM JSON 파싱/호출 실패",
    "LLM 호출/응답 실패",
    "일부 시드에서 LLM JSON 파싱/호출 실패",
    "일부 시드에서 LLM 호출/응답 실패",
    "해당 상품-페르소나 케이스를 낮은 workers",
    "실패한 시드는 추가 재실행",
    "seed=",
)
DIAGNOSTIC_ITEM_MARKERS = (
    "FDM_LLM_",
    "FDM_OPENAI_",
    "FDM_GEMINI_",
    "generativelanguage.googleapis.com",
    "openai/chat/completions",
    "JSON 파싱 실패",
    "연결 실패:",
    "호출 실패:",
    "응답 본문 없음",
)


def is_diagnostic_item(item: str) -> bool:
    text = item.strip()
    if not text:
        return False
    return text.startswith(DIAGNOSTIC_ITEM_PREFIXES) or any(
        marker in text for marker in DIAGNOSTIC_ITEM_MARKERS
    )


def public_items(items: list[str]) -> list[str]:
    return [item.strip() for item in items if item and item.strip() and not is_diagnostic_item(item)]
