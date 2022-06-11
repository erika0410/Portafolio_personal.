lista=[]
for x in range(5):
    lista.append(int(input(f"Ingresar Número {x+1}: ")))
comodin=lista[0]
for x in range(5):
    if lista[x]<comodin:
        comodin=lista[x]
valor=""
if comodin%2==0:
    valor="Par"
else:
    valor="Impar"
print(f"lista {lista} / Numero menor: {comodin} ") 
print(valor)