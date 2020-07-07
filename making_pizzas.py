import pizza

"""模块导入初次"""
pizza.make_pizza("mushrooms", "green peppers", "extra cheese")

from pizza2 import make_pizza

make_pizza(11, "mushrooms")

from pizza2 import make_pizza as make

make(11, "mushrooms")

from pizza import *

make_pizza("mushrooms", "green peppers")
