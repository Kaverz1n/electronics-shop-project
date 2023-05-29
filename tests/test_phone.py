import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def make_phone():
    return Phone('Iphone', 15_000, 2, 1)

def test_init(make_phone):
    phone = make_phone
    assert phone.name == "Iphone"
    assert phone.price == 15_000
    assert phone.quantity == 2
    assert phone.number_of_sim == 1

def test_repr(make_phone):
    phone = make_phone
    assert repr(phone) == "Phone('Iphone', 15000, 2, 1)"


def test_add(make_phone):
    phone = make_phone
    item = Item("Телевизор", 3000, 4)
    assert phone + phone == 4
    assert phone + item == 6


def test_num_of_sim():
    phone = Phone('Iphone', 15_000, 2, -1)
    assert phone.number_of_sim == 1

    phone.number_of_sim = 4
    assert phone.number_of_sim == 4

    phone.number_of_sim = -3
    assert phone.number_of_sim == 1