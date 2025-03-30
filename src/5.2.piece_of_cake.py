def piece_of_cake(prices, optionals=None, **quantities):
    """
    The function calculates the total price of a recipe based
     on the prices of the ingredients and their quantities.

    Parameters:
    prices (dict): A dictionary with the prices of the ingredients
    optionals (list): A list of optional ingredients
    quantities (dict): A dictionary with the quantities of the ingredients

    Returns the total price of the recipe
    
    """
    if optionals is None:
        optionals = []

    total_price = 0
    for ingredient, price_per_100g in prices.items():
        if ingredient not in optionals and ingredient in quantities:
            quantity = quantities[ingredient]
            total_price += (price_per_100g / 100) * quantity

    return total_price


def main():
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))  # Output: 44
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))  # Output: 54
    print(piece_of_cake({}))  # Output: 0
if __name__ == '__main__':
    main()
