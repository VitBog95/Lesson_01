import pytest
from string_utils import StringUtils


utils = StringUtils()


# --- Тесты для функции capitalize ---
@pytest.mark.parametrize("input_string, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("123abc", "123abc"),
    ("", ""),
    (" ", " "),
])
def test_capitalize(input_string, expected):
    """Тестируем функцию capitalize на разных строках."""
    assert utils.capitalize(input_string) == expected


# --- Тесты для функции trim ---
@pytest.mark.parametrize("input_string, expected", [
    ("   skypro", "skypro"),
    ("skypro   ", "skypro   "),
    ("   skypro   ", "skypro   "),
    ("", ""),
    ("   ", ""),
])
def test_trim(input_string, expected):
    """Тестируем функцию trim."""
    assert utils.trim(input_string) == expected


# --- Тесты для функции contains ---
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "S", False),
    ("SkyPro", "", True),
])
def test_contains(string, symbol, expected):
    """Тестируем функцию contains."""
    assert utils.contains(string, symbol) == expected


# --- Тесты для функции delete_symbol ---
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("", "k", ""),
    ("SkyPro", "", "SkyPro"),
])
def test_delete_symbol(string, symbol, expected):
    """Тестируем функцию delete_symbol."""
    assert utils.delete_symbol(string, symbol) == expected


# --- Негативные тесты с None ---
def test_capitalize_none():
    with pytest.raises(AttributeError):
        utils.capitalize(None)


def test_trim_none():
    with pytest.raises(AttributeError):
        utils.trim(None)


def test_contains_none():
    with pytest.raises(AttributeError):
        utils.contains(None, "S")


def test_delete_symbol_none():
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "k")
