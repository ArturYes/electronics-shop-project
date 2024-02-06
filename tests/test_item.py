"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

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
