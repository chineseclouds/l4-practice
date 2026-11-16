import pytest

from l4tools import char_count, truncate, word_count


def test_word_count_basic():
    assert word_count("hello world") == 2


def test_word_count_empty():
    assert word_count("") == 0


def test_char_count_basic():
    assert char_count("hello world") == 11


def test_char_count_empty():
    assert char_count("") == 0
    assert char_count("", ignore_whitespace=True) == 0


def test_char_count_ignore_whitespace():
    assert char_count("a b\tc\nd", ignore_whitespace=True) == 4
    assert char_count(" \t\n", ignore_whitespace=True) == 0


def test_char_count_non_ascii():
    assert char_count("你好") == 2
    assert char_count("你 好", ignore_whitespace=True) == 2


def test_truncate_shorter_than_limit():
    assert truncate("hi", 5) == "hi"


def test_truncate_exactly_at_limit():
    assert truncate("hello", 5) == "hello"


def test_truncate_normal():
    result = truncate("hello world", 8)
    assert result == "hello w…"
    assert len(result) == 8


def test_truncate_custom_suffix():
    assert truncate("hello world", 8, suffix="...") == "hello..."


def test_truncate_empty_suffix():
    assert truncate("hello world", 5, suffix="") == "hello"


def test_truncate_invalid_max_len():
    with pytest.raises(ValueError):
        truncate("hello world", 2, suffix="...")
    with pytest.raises(ValueError):
        truncate("hello world", -1)


def test_truncate_invalid_max_len_short_text():
    with pytest.raises(ValueError):
        truncate("hi", 2, suffix="...")


def test_truncate_max_len_equals_suffix_len():
    assert truncate("hello", 1) == "…"
