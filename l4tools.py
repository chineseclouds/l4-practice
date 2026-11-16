"""Tiny utilities used to practice an agent-friendly GitHub workflow."""


def word_count(text: str) -> int:
    """Number of whitespace-separated words in text."""
    return len(text.split())


def char_count(text: str, ignore_whitespace: bool = False) -> int:
    """Number of characters in text, optionally excluding whitespace."""
    if ignore_whitespace:
        return sum(1 for ch in text if not ch.isspace())
    return len(text)


def truncate(text: str, max_len: int, suffix: str = "…") -> str:
    """Shorten text to at most max_len characters, ending with suffix if cut."""
    if max_len < len(suffix):
        raise ValueError("max_len must be at least len(suffix)")
    if len(text) <= max_len:
        return text
    return text[: max_len - len(suffix)] + suffix
