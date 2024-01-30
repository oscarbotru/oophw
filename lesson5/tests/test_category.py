import pytest

from src.category import Category


@pytest.fixture
def category_products():
    return Category(
        'Напитки',
        'Здесь находится описание категории',
        ['молоко', 'вода', 'вино', 'сок']
    )


def test_init_category(category_products):
    assert category_products.name == 'Напитки'
    assert category_products.description == 'Описание категории'
    assert category_products.products == ['молоко', 'вода', 'вино', 'сок']


def test_counting(category_products):
    assert len(category_products.products) == 4