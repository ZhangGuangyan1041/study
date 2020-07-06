message = input("请输入一个数字：")
print("你输入的数字是：" + message)

age = input("How old are you ?")
age = int(age)
if age >= 18:
    print("一个成年人")
else:
    print("一个未成年人")

number = input("Enter a number ,and I'll tell you if it's even or odd:")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even")
else:
    print("\nThe number " + str(number) + " is odd")
