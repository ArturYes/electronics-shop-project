"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from config import TEST_ITEM
from src.item import Item


@pytest.fixture
def product():
    return Item("Смартфон", 10000, 20)


def test_init(product):
    assert product.name == "Смартфон"
    assert product.price == 10000
    assert product.quantity == 20


def test_calculate_total_price(product):
    assert product.calculate_total_price() == 200000


def test_apply_discount(product):
    product.pay_rate = 0.8
    product.apply_discount()
    assert product.price == 8000


def test_setter(product):
    product.name = 'iphone'
    assert product.name == 'iphone'
    product.name = 'iphone15maxultra'
    assert product.name == 'iphone15ma'




def test_instantiate_from_csv():
    Item.instantiate_from_csv(TEST_ITEM)
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100
    assert item1.quantity == 1


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
