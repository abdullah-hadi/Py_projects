import random

while 1:
    print(random.randint(1,6))
    s=input("roll again?(y/n): ")
    if s=='y':
        continue
    else:
        break