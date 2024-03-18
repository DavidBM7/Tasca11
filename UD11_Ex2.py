from functools import reduce
def praula_a_numero(llista):

    a = list(map(lambda x:str(x), llista))
    b = reduce(lambda x,y:x+y,a)
    print("La llista {} es el numero {}".format(llista,b))

#PP
l=[3, 5, 7, 9, 1]
praula_a_numero(l)