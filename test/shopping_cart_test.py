# testing the shopping cart application

from app.shopping_cart import to_usd


def test_to_usd():
	result = to_usd(5.2)
	assert result == "$5.20"