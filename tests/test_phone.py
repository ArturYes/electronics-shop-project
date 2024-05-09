from src.phone import Phone
from src.item import Item
import pytest


@pytest.fixture
def my_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def my_item():
    return Item("Смартфон", 10000, 20)


def test_init(my_phone):
    assert my_phone.name == "iPhone 14"
    assert my_phone.price == 120000
    assert my_phone.quantity == 5
    assert my_phone.number_of_sim == 2


def test_repr(my_phone):
    assert repr(my_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(my_phone):
    assert str(my_phone) == "iPhone 14"


def test_add(my_phone, my_item):
    with pytest.raises(Exception, match='Складывать можно только экземпляры класса'):
        my_phone + 5
        my_phone + 'text'
    assert my_item + my_phone == 25
    assert my_item + my_item == 40
    assert my_phone + my_item == 25
    assert my_phone + my_phone == 10


def test_number_of_sim_getter(my_phone):
    assert my_phone.number_of_sim == 2


def test_number_of_sim_setter(my_phone):
    my_phone.number_of_sim = 1
    assert my_phone.number_of_sim == 1
    with pytest.raises(Exception, match='Количество физических SIM-карт должно быть целым числом больше нуля.'):
        my_phone.number_of_sim = 0
        my_phone.number_of_sim = 0.5
        my_phone.number_of_sim = -1