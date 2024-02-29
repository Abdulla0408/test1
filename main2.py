def test_decaration(func):
    def wrapper():
        print("Nimadur ish qilinadi")
        func()
        print("Yana nimadir qilindi")
    return wrapper

@test_decaration
def say_hello(name):
    return f"Assalomu alaykum {name}"

say_hello("Abdulla")