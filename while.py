unconfirmed_users = ['alice', 'brain', 'candance']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user)
    confirmed_users.append(current_user)
print(str(unconfirmed_users) + "\n")
print(str(confirmed_users))

pets = ['dog', 'dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?yes/no")
    if repeat == 'no':
        polling_active = False

for name, response in responses.items():
    print(name + " like to climb " + response+".")
