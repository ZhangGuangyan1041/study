# 不能写成def describe_pet(pet_name="ketty",animal_type):
def describe_pet(animal_type, pet_name="ketty"):
    """显示宠物的信息"""
    print("I have a " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name)


# 关键字实参顺序无关紧要，等价写法
describe_pet(animal_type='dog', pet_name='harry')
describe_pet(pet_name='harry', animal_type='dog')
# 以下两种为等价写法
describe_pet(animal_type='dog')
describe_pet('dog')
