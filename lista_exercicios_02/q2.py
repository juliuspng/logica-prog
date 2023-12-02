salario = float(input("digite o salário do funcionário: "))

if salario > 1250.00:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
novo_salario = salario + aumento 
print(f"o valor do aumento é: R$ {aumento: .2f}")
print(f"o novo salário é: R$ {novo_salario: .2f}")