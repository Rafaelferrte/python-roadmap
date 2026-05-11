# Loop while
i=0
numero=4

while i<numero:
    print(f"O número é {i}")
    i += 1

# Loop for
for i in range(1,10):
    print(i)

for i in range(1,10,2):
    print(i)


cartao_credito = "1234-5678-9012-3456"

for x in cartao_credito:
    print(x)

for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)