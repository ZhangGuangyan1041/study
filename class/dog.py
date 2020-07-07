class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " is now sitting|")

    def roll_over(self):
        """模拟小狗滚动"""
        print(self.name.title() + " rolled over!")

    def set_name(self, name):
        self.name = name


my_dog = Dog("xiaohei", 5)
print("my dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.name = "xiaohua"
print(my_dog.name)

my_dog.set_name("xiaobai")
print(my_dog.name)


class SmallDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)


small_dog = SmallDog("xiaohei", 1)
print(small_dog.name)
print(small_dog.age)
