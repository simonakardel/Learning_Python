
def sharpshooter(func):
    def wrapper():
        return func() + ", the sharpshooter"
    return wrapper

def stealthy(func):
    def wrapper():
        return func() + " and stealthy character"
    return wrapper

def healer(func):
    def wrapper():
        return func() + ", the healer"
    return wrapper

def berserker(func):
    def wrapper():
        return func() + " and berserker character"
    return wrapper

def mage(func):
    def wrapper():
        return func() + " with magic abilities"
    return wrapper


@mage
@stealthy
@sharpshooter
def player():
    return "I'm the player character"

print(player())

