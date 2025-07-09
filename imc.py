# -- coding: utf-8 --
"""
Projeto: Cálculo de Índice de Massa Corporal (IMC)

Este programa calcula o IMC de uma pessoa com base na altura (em metros)
e peso (em quilogramas) fornecidos pelo usuário, e classifica o resultado
de acordo com a tabela da Organização Mundial da Saúde (OMS).
"""

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).

    Args:
        peso (float): Peso em quilogramas.
        altura (float): Altura em metros.

    Returns:
        float: O valor do IMC calculado.
    """
    if altura <= 0:
        raise ValueError("A altura deve ser um valor positivo e maior que zero.")
    return peso / (altura ** 2)

def classificar_imc(imc):
    """
    Classifica o IMC de acordo com a tabela da OMS.

    Args:
        imc (float): O valor do IMC.

    Returns:
        str: A classificação do IMC.
    """
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso adequado"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 34.9:
        return "Obesidade grau I"
    elif 35 <= imc <= 39.9:
        return "Obesidade grau II"
    else: # imc >= 40.0
        return "Obesidade grau III"

def main():
    """
    Função principal do programa para interagir com o usuário.
    """
    print("Bem-vindo(a) ao Calculador de IMC!")

    while True:
        try:
            altura_str = input("Por favor, digite sua altura em metros (ex: 1.75): ")
            altura = float(altura_str.replace(',', '.')) # Substitui vírgula por ponto para aceitar ambos
            if altura <= 0:
                print("Erro: A altura deve ser um número positivo.")
                continue # Volta para o início do loop

            peso_str = input("Por favor, digite seu peso em quilogramas (ex: 70.5): ")
            peso = float(peso_str.replace(',', '.')) # Substitui vírgula por ponto para aceitar ambos
            if peso <= 0:
                print("Erro: O peso deve ser um número positivo.")
                continue # Volta para o início do loop

            break # Sai do loop se ambos os inputs forem válidos

        except ValueError:
            print("Entrada inválida. Por favor, digite números para altura e peso.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    try:
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print(f"\nSeu IMC é: {imc:.2f}") # Formata para duas casas decimais
        print(f"Classificação: {classificacao}")
        print("\nObservação: Para uma avaliação mais detalhada, consulte um profissional de saúde.")

    except ValueError as e:
        print(f"Erro no cálculo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante o cálculo: {e}")

if __name__ == "__main__":
    main()