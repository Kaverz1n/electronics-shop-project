import pytest

from src.item import Item


@pytest.fixture
def make_item():
    return Item("Телевизор", 3000, 4)


def test_init(make_item):
    item = make_item
    assert item.name == "Телевизор"
    assert item.price == 3000
    assert item.quantity == 4


def test_calculate_total_price(make_item):
    item = make_item
    assert item.calculate_total_price() == 12_000
    assert item.calculate_total_price() == item.price * item.quantity


def test_apply_discount(make_item):
    item = make_item
    first_price = item.price
    item.apply_discount()
    assert item.price == first_price * Item.pay_rate
    assert item.price == 3000.0

    item.price = first_price
    item.pay_rate = 1.2
    item.apply_discount()
    assert item.price == first_price * item.pay_rate
    assert item.price == 3600.0


def test_all(make_item):
    for i in Item.all:
        assert isinstance(i, object)


def test_repr(make_item):
    item = make_item
    assert str(item) == "Товар Телевизор"
