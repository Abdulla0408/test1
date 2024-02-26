
import time
def calculate(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res= func(*args, **kwargs)
        print(f"{time.time() - start} vaqt ketti!")
        return res
    return wrapper


@calculate
def start():
    users = []
    while True:
        username = input("Enter username: ")
        if username == "stop":
            break
        users.append(username)
    return users
print(start())

# @calculate
# def multiplay(x,y):
#     for i in range(5000000000000000000):
#         pass
#     return x * y

# print(multiplay(4,5))

print("Hello World!")
for i in range(5):
    print("Hello World!")
    