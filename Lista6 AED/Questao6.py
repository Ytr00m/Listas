primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )

ultimo = primeiro + (2-1)*razao
ultimo = ultimo + 1

for var in range(primeiro, ultimo, razao):
    print(var)