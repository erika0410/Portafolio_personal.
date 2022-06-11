nombre=[]
for x in range(5):
    nombre.append((input(f"Ingresar Nombre {x+1}: ")))
comodin=nombre[0]
for x in range(5):
    if nombre[x]<comodin:
        comodin=nombre[x]
cade=comodin
if cade[0]=="a" or cade[0]=="A" or cade[0]=="e" or cade[0]=="E" or cade[0]=="i" or cade[0]=="I" or cade[0]=="o" or cade[0]=="o" or cade[0]=="u" or cade[0]=="u":
    print("empieza en vocal")
else:
    print("No empieza en vocal ")
print(f"lista {nombre}/ Nombre menor: {comodin} ") 
print(cade)