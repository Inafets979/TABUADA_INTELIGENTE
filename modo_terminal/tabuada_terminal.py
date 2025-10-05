import random

# Dicionário de erros para sugerir treino depois do modo desafio
erros = {}

def mostrar_menu():
    print("\n=== TABUADA INTELIGENTE ===")
    print("1 - Ver tabuada completa de um número")
    print("2 - Ver uma conta específica da tabuada")
    print("3 - Ver como soma repetida")
    print("4 - Ver dica de memorização")
    print("5 - Modo desafio")
    print("0 - Sair")

def escolher_numero():
    while True:
        try:
            numero = int(input("Digite um número entre 1 e 10: "))
            if 1 <= numero <= 10:
                return numero
            else:
                print("⚠️ Apenas números de 1 a 10 são permitidos.")
        except ValueError:
            print("⚠️ Entrada inválida. Digite um número inteiro.")

def tabuada_completa(numero):
    print(f"\n📘 Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def conta_especifica(numero):
    while True:
        try:
            multiplicador = int(input(f"Escolha um número de 1 a 10 para multiplicar com {numero}: "))
            if 1 <= multiplicador <= 10:
                print(f"\n🔍 Resultado: {numero} x {multiplicador} = {numero * multiplicador}")
                break
            else:
                print("⚠️ Apenas números de 1 a 10 são permitidos.")
        except ValueError:
            print("⚠️ Entrada inválida. Digite um número inteiro.")

def soma_repetida(numero):
    while True:
        try:
            multiplicador = int(input(f"Escolha um número de 1 a 10 para multiplicar com {numero}: "))
            if 1 <= multiplicador <= 10:
                soma = " + ".join([str(numero)] * multiplicador)
                resultado = numero * multiplicador
                print(f"\n🧠 Soma repetida:\n{numero} x {multiplicador} = {soma} = {resultado}")
                break
            else:
                print("⚠️ Apenas números de 1 a 10 são permitidos.")
        except ValueError:
            print("⚠️ Entrada inválida. Digite um número inteiro.")

def dica_memorizacao(numero):
    dicas = {
        1: "🎯 Tabuada do 1: Qualquer número × 1 = o próprio número!\n💡 Dica: É como não fazer nada, o número fica igual.",
        2: "🎯 Tabuada do 2: É dobrar o número!\n💡 Dica: 2×3 = 3+3 = 6. Sempre some o número com ele mesmo.\n🔢 Padrão: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20",
        3: "🎯 Tabuada do 3: Use os dedos para contar!\n💡 Dica: 3×4 = conte 3, 6, 9, 12 (pule de 3 em 3).\n🔢 Padrão: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30",
        4: "🎯 Tabuada do 4: É dobrar duas vezes!\n💡 Dica: 4×3 = (2×3) + (2×3) = 6 + 6 = 12\n🔢 Padrão: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40",
        5: "🎯 Tabuada do 5: Termina sempre em 0 ou 5!\n💡 Dica: 5×4 = 20, 5×7 = 35. Conte de 5 em 5!\n🔢 Padrão: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50",
        6: "🎯 Tabuada do 6: Use a tabuada do 3 e dobre!\n💡 Dica: 6×4 = (3×4) × 2 = 12 × 2 = 24\n🔢 Padrão: 6, 12, 18, 24, 30, 36, 42, 48, 54, 60",
        7: "🎯 Tabuada do 7: A mais difícil, mas tem truques!\n💡 Dica: 7×2 = 14, 7×3 = 21. Use os dedos para contar!\n🔢 Padrão: 7, 14, 21, 28, 35, 42, 49, 56, 63, 70",
        8: "🎯 Tabuada do 8: É dobrar 3 vezes!\n💡 Dica: 8×3 = (4×3) × 2 = 12 × 2 = 24\n🔢 Padrão: 8, 16, 24, 32, 40, 48, 56, 64, 72, 80",
        9: "🎯 Tabuada do 9: Truque dos dedos!\n💡 Dica: 9×3 = 27. A soma dos dígitos (2+7) = 9!\n🔢 Padrão: 9, 18, 27, 36, 45, 54, 63, 72, 81, 90",
        10: "🎯 Tabuada do 10: Só adicionar um zero!\n💡 Dica: 10×4 = 40. É o número original + 0 no final!\n🔢 Padrão: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100",
    }
    texto = dicas.get(numero, "Essa tabuada não tem uma dica especial.")
    print(f"\n💡 Dicas para o {numero}:\n{texto}")

def sugerir_treino():
    if erros:
        mais_errado = max(erros, key=erros.get)
        numero, multiplicador = mais_errado
        print(f"\n📌 Sugestão de treino:\nVocê errou bastante {numero} x {multiplicador}. Que tal praticar essa conta?")

def modo_desafio():
    numero = random.randint(1, 10)
    multiplicador = random.randint(1, 10)
    try:
        resposta = int(input(f"Quanto é {numero} x {multiplicador}? "))
        correto = numero * multiplicador
        if resposta == correto:
            print(f"✅ Acertou! {numero} x {multiplicador} = {correto}")
        else:
            print(f"❌ Errou. Resposta correta: {numero} x {multiplicador} = {correto}")
            erros[(numero, multiplicador)] = erros.get((numero, multiplicador), 0) + 1
            sugerir_treino()
    except ValueError:
        print("⚠️ Entrada inválida. Digite um número inteiro.")