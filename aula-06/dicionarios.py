capitais = {"EUA": "Washington D.C.",
            "India": "Nova Deli",
            "China": "Pequim",
            "Russia": "Moscou"}

dir(capitais)
help(capitais)
print(capitais.get("India"))

if capitais.get("Japão"):
    print("Essa capital existe!")
else:
    print("Essa capital não existe!")

capitais.update({"Alemanha": "Berlim"})
capitais.pop("China")
# Remove o último valor
capitais.popitem()
capitais.clear()

keys = capitais.keys()

for key in capitais.keys():
    print(key)

values = capitais.values()

for value in values:
    print(value)


items = capitais.items()
for key, value in capitais.items():
    print(f"{key}: {value}")

