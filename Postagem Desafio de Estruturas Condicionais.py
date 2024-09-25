from ast import parse


def main():
    salario = float(input("Qual é o seu salário: "))
    fazercalculo(salario)

def fazercalculo(salario):
    inflacao = 3.8 / 100
    if (salario <= 280):
        percentual = 20/100
        aumento = percentual * salario
        salarioAjustado = aumento + salario
        salarioDecInflacao = salarioAjustado - (salarioAjustado * inflacao)

    if (salario > 280 & (salario <= 700)):
        percentual = 15/100
        aumento = percentual * salario
        salarioAjustado = aumento + salario
        salarioDecInflacao = salarioAjustado - (salarioAjustado * inflacao)

    if (salario > 700 & (salario <= 1500)):
        percentual = 10/100
        aumento = percentual * salario
        salarioAjustado = aumento + salario
        salarioDecInflacao = salarioAjustado - (salarioAjustado * inflacao)

    if (salario > 1500):
        percentual = 5/100
        aumento = percentual * salario
        salarioAjustado = aumento + salario
        salarioDecInflacao = salarioAjustado - (salarioAjustado * inflacao)

    impressao(salario, percentual, aumento, salarioAjustado, salarioDecInflacao)

def impressao(salario, percentual, aumento, salarioAjustado, salarioDecInflacao):
    print(f'O salário antes do reajuste era de R${salario}')
    print(f'Percentual aplicado: {percentual*100}%')
    print(f'O valor do reajuste R${aumento}')
    print(f'O salário total com reajuste R${salarioAjustado}')
    print(f'O salário real com desconto da inflação R${salarioDecInflacao}')

if __name__ == "__main__":
    main()