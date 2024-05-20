"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from config import TEST_ITEM
from src.csv_exception import InstantiateCSVError
from src.item import Item
from src.phone import Phone


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


def test_instantiate_from_csv(item1):
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


@pytest.fixture()
def item1():
    return Item("Смартфон", 10000, 20)


def test_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item1):
    assert str(item1) == 'Смартфон'


def test_add(product):
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    with pytest.raises(Exception, match='Складывать можно только экземпляры класса'):
        product + 5
        product + 'text'
    assert product + phone1 == 25


def test_instantiate_from_csv_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('test.csv')
        Item.instantiate_from_csv('')


def test_instantiate_from_csv_defect():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('src/fake.csv')

