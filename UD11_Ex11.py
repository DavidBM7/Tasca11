def imprimir_fitxer(m):
    a = []
    with open(m,"r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)

def afagir_fitxer(m,llista):
    with open(m,"a+") as f:
        for e in llista:
            f.write(e+"\n")

#PP
fitxer = "/home/david/AO/Unidad11/ex11.txt"
llista = ["Jordi","Claudia","David","Ayoub","Oscar","Paula","Sebas","Anas"]
afagir_fitxer(fitxer,llista)
imprimir_fitxer(fitxer)