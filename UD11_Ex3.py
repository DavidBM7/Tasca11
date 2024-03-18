def filtrer (llista,c):
    f =(list(filter(lambda x: x[0]==c, llista)))
    print("De la llista {}, les paraules que comencen per {} son {}".format(llista,c,f))

#PP
llista = ["Josep","Joan","Jordi","Maria","Marc","Pere","Paula"]
c = "p"
filtrer(llista,c)
