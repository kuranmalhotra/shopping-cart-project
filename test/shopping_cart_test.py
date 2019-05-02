# testing the shopping cart application

from app.shopping_cart import (
	to_usd,
	tax,
	total
	tax_rate
	)


def test_to_usd():
	result = to_usd(5200.2)
	assert result == "$5200.20"

def test_tax():
	result = tax(100)
	assert result == 6

def test_total():
	result = total(100)
	assert result == 106