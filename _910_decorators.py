from icecream import ic

def deco(func):
    def inner_deco(*args):
        print("El resultado de la suma es: ")
        #ic(args[0])
        #ic(args[1])
        ret = func(*args)
        print(ret)
        print("Finalizando...")
    return inner_deco


@deco
def addittion(a, b) -> int:
    return a + b


addittion(1, 9)
