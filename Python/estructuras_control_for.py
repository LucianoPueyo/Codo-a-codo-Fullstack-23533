# for clasico
for i in range(0, 10): # [0, 10) | Incluye al 0 y no incluye al 10
    print(i)


#        0          1          2       3
frutas = ["Banana", "Manzana", "Pera", "Uva"]

# for each
for fruta in frutas:
    print(fruta)

print("----------------")
print(len(frutas))

for i in range(0, len(frutas)):
    print(i, frutas[i])