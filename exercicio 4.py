def converter_cm_para_m(cm):
    metros = cm / 100
    return metros

centimetros = float(input("Digite a quantidade em centímetros: "))
metros = converter_cm_para_m(centimetros)
print(f"{centimetros} centímetros é igual a {metros:.2f} metros.")
