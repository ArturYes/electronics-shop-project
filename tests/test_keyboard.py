import pytest

from src.keyboard import Keyboard


@pytest.fixture
def product():
    return Keyboard("Смартфон", 10000, 20)


def test_init(product):
    assert product.name == "Смартфон"
    assert product.price == 10000
    assert product.quantity == 20


def test_language(product):
    assert product.language == 'EN'


def test_change_lang(product):
    product.change_lang()
    assert product.language == 'RU'
    product.change_lang()
    assert product.language == 'EN'
    with pytest.raises(AttributeError):
        product.language = 'CH'
        product.language = 'UA'
        product.language = 'KZ'