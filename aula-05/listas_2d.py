frutas = ["maçã","laranja","banana","cocô"]
vegetais = ["salsão","cenoura","batata"]
carnes = ["frango","peixe","peru"]

mantimentos = [frutas,vegetais,carnes]

# print(mantimentos[1][1])

for i in mantimentos:
    print("")
    for comida in i:
        print(comida, end=" ")