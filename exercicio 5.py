def calcular_area(base, altura):
    return base * altura

print("Cálculo da área de um retângulo")
base = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

area = calcular_area(base, altura)
print(f"A área do retângulo é: {area:.2f}")
