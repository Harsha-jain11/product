from product import get_product_info

def test_get_product_info():
    expected = "Product ID: 1001\nName: Laptop\nQuantity: 3\nPrice: 65000"
    assert get_product_info(1001, "Laptop", 3, 65000) == expected
