import pytest

from src.mixin_lang import MixinLang
from src.item import Item
from src.keyboard import KeyBoard


@pytest.fixture
def make_keyboard():
    return KeyBoard('Super cool keyboard', 15_000, 2)


def test_init(make_keyboard):
    keyboard = make_keyboard
    assert keyboard.name == "Super cool keyboard"
    assert keyboard.price == 15000
    assert keyboard.quantity == 2
    assert keyboard.language == 'EN'
    assert isinstance(keyboard, Item)
    assert isinstance(keyboard, MixinLang)


def test_mixin(make_keyboard):
    keyboard = make_keyboard
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'
    keyboard.change_lang().change_lang()
    assert keyboard.language == 'EN'

    with pytest.raises(AttributeError):
        keyboard.language = 'UK'
