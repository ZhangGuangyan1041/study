def make_pizza(size, *toppings):
    """打印顾客点的所有配件"""
    """形参toppings会指示创建一个元组，所有的参数会放入这个元组中"""
    print("Making a " + str(size) + " inch pizza with the  following toppings:")
    for topping in toppings:
        print("--" + topping )


# make_pizza(7, "pepperoni")
# make_pizza(10, "mushrooms", "green peppers", "extra cheese")
