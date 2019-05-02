# testing the shopping cart application

import time

from app.shopping_cart import (
	to_usd,
	tax,
	total,
	lookup_product,
	scan,
	subtotal,
	get_time,
	tax_rate,
	sale,
	products
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

def test_lookup_product():
	result = lookup_product(2)
	assert result == "Name: All-Seasons Salt | Price: $4.99"

def test_scan():
	scan(2)
	scan(3)
	scan(1)
	assert sale == [
		{'name': 'All-Seasons Salt', 'price': 4.99},
		{'name': 'Robust Golden Unsweetened Oolong Tea', 'price': 2.49},
		{'name': 'Chocolate Sandwich Cookies', 'price': 3.5},
		]

def test_subtotal():	
	# since items were scanned above
	result = subtotal()
	assert result == 10.98

def test_get_time():
	result = get_time()
	assert result == time.strftime('%X %x %Z').center(50, " ")