teclado = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))


for linha in teclado:
    for num in linha:
        print(num, end=" ")
    print()