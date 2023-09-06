def print_price_list(price: dict[str, float]) -> None:
    """Print specified price list."""
    print('*' * 30)
    print('ПРАЙС ЛИСТ'.center(30, '*'))
    print('*' * 30)

    for product_name, product_cost in price.items():
        print(f'{product_name}: {product_cost} за кило')
