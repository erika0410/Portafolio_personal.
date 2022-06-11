lista=[]
con=0
for x in range(5):
    lista.append(int(input(f"Ingresar Número entero {x+1}: ")))
    
comodin=lista[0]
for x in range(5):
    if lista[x]<comodin:
        comodin=lista[x]

for x in range(5):
    if lista[x]==comodin:
        con=con+1


print(f"lista {lista} ")
print(f"Numero mayor: {comodin} ") 
print(f"se repite {con}")