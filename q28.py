nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
valor_vendas = float(input("Digite o valor total de vendas efetuadas pelo vendedor: "))
valor_comissao = valor_vendas * 0.15
total_receber = salario_fixo + valor_comissao
print("O total a receber pelo vendedor {} é de R$ {:.2f}".format(nome, total_receber))
