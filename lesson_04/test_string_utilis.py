import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("hello", "Hello"),
        ("привет", "Привет"),
        ("скоро зима", "Скоро зима"),
        ("Чудесная пора", "Чудесная пора"),
    ],
)
def test_capitalize_positive(input_text, expected):
    assert string_utils.capitalize(input_text) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("", ""),
        ("   ", "   "),
        ("12-oe", "12-oe"),
    ],
)
def test_capitalize_negative(input_text, expected):
    assert string_utils.capitalize(input_text) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected",
    [
        (None, AttributeError),
        (12345, AttributeError),
    ],
)
def test_capitalize_negative_errors(input_text, expected):
    with pytest.raises(expected):
        string_utils.capitalize(input_text)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("   Ночь и тишина", "Ночь и тишина"),
        (" hello", "hello"),
        ("Python", "Python"),
        (" Ночь. Улица.  Фонарь. ", "Ночь. Улица.  Фонарь. "),
    ],
)
def test_trim_positive(input_text, expected):
    assert string_utils.trim(input_text) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("  ", ""),
        ("", ""),
        ("hello   ", "hello   "),
    ],
)
def test_trim_negative(input_text, expected):
    assert string_utils.trim(input_text) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected",
    [
        (None, AttributeError),
        (12345, AttributeError),
    ],
)
def test_trim_negative_errors(input_text, expected):
    with pytest.raises(expected):
        string_utils.trim(input_text)


@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("Hello", "H", True),
        ("Hello", "o", True),
        ("Hello", "ell", True),
        ("Привет", "и", True),
        ("Привет", "п", False),
        ("Hello", "S", False),
    ],
)
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("", "a", False),
        ("   ", "a", False),
        ("12345", "8", False),
        ("1234", "b", False),
    ],
)
def test_contains_neganive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        (None, "b", AttributeError),
        ("Hello", None, TypeError),
        (12345, "3", AttributeError),
    ],
)
def test_contains_negative_errors(string, symbol, expected):
    with pytest.raises(expected):
        string_utils.contains(string, symbol)


@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("Припев", "П", "рипев"),
        ("Припев", "п", "Приев"),
        ("Колос", "о", "Клс"),
        ("Hello World", "llo", "He World"),
        ("Good bay", " ", "Goodbay"),
    ],
)
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("Hello", "s", "Hello"),
        ("", "p", ""),
        ("Hello", "", "Hello"),
    ],
)
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        (None, "b", AttributeError),
        ("Hello", None, TypeError),
        (12345, "3", AttributeError),
    ],
)
def test_delete_symbol_negative_errors(string, symbol, expected):
    with pytest.raises(expected):
        string_utils.delete_symbol(string, symbol)
