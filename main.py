import random
import re

def virar_cartas():
    return [random.randint(1, 20) for _ in range(5)]

def jogar_dados():
    return random.randint(1, 10), random.randint(1, 6)

def verificar_expressao(expressao, cartas, resultado):
    try:
        valor = eval(expressao)
        if valor != resultado:
            return False, "O resultado da expressão não corresponde ao valor dos dados."
        
        numeros_usados = [int(num) for num in re.findall(r'\b\d+\b', expressao)]
        cartas_temp = cartas.copy()
        for numero in numeros_usados:
            if numero in cartas_temp:
                cartas_temp.remove(numero)
            else:
                return False, f"O número {numero} não está nas cartas viradas ou já foi usado."
        
        return True, "Expressão válida!"
    except Exception as e:
        return False, f"Erro ao avaliar a expressão: {e}"

def jogar():
    cartas = virar_cartas()
    dado1, dado2 = jogar_dados()
    resultado_dados = dado1 + dado2
    
    print(f"Cartas viradas: {cartas}")
    print(f"Dados lançados: {dado1}, {dado2} (Resultado esperado: {resultado_dados})")
    
    while True:
        expressao = input("Digite uma expressão usando as cartas (ou 'sair' para terminar): ")
        if expressao.lower() == 'sair':
            break
        valida, mensagem = verificar_expressao(expressao, cartas, resultado_dados)
        print(mensagem)
        if valida:
            print("Parabéns! Você encontrou uma solução!")
            break

if __name__ == "__main__":
    jogar()
