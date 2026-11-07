from l4tools import char_count, word_count


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
