def tuple_product(numbers):
    """
    Function to calculate the product of all elements in a tuple.
    Argument:
        numbers (tuple): A tuple containing numeric values.
    Returns:
        int/float: Product of all elements.
    """
    product = 1
    for num in numbers:
        product *= num
    return product

# Example usage
my_tuple = (2, 3, 4, 5)
print("Tuple:", my_tuple)
print("Product of tuple elements =", tuple_product(my_tuple))
