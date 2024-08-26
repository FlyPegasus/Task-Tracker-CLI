'''lst = []
while True:
    choice = int(input("1. add, 2. delete\nEnter choice: "))
    if choice == 1:
        ele = int(input("Item: "))
        lst.append(ele)
    elif choice == 2:
        ele = int(input("Item: "))
        for i in range(len(lst)):
            print("hi")
            if lst[i] == ele:
                del lst[i]
                break
    else:
        break
    print(lst)
'''

# using random
import random
'''lst = []

count = 8
i = 0
while i < count:
    rand_int = random.randint(0, 10)
    if rand_int not in lst:
        lst.append(rand_int)
        i += 1
print(lst)'''


def unique_key(main_dict):
    rand_int = random.randint(0, 100)
    while rand_int in main_dict:
        rand_int = random.randint(0, 100)
    return rand_int
