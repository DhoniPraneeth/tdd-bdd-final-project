from behave import given, when, then
from models import Product  # Assuming a Product model is used in your application

@given('the product data is loaded')
def step_impl(context):
    """
    Step to load initial data for products into the context's test database.
    """
    context.products = [
        Product(name="Laptop", category="Electronics", price=999.99, available=True),
        Product(name="Phone", category="Electronics", price=499.99, available=True),
        Product(name="Desk Chair", category="Furniture", price=89.99, available=False)
    ]
    for product in context.products:
        product.save()  # Mock save method for the product to simulate database insertion

@when('a product with name "{product_name}" is searched')
def step_impl(context, product_name):
    """
    Step to simulate searching for a product by name.
    """
    context.search_result = Product.find_by_name(product_name)  # Mock search function

@then('the product details should be displayed')
def step_impl(context):
    """
    Step to check if the product search returned expected results.
    """
    assert context.search_result is not None, "Product not found!"
    print(f"Product found: {context.search_result.name}, {context.search_result.category}, ${context.search_result.price}")
