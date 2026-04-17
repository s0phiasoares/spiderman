import random
import time

saldo = float(input("Digite o valor que deseja apostar: R$"))  # saldo inicial



simbolos = ["🍒", "⭐", "🔔", "7️⃣", "🍋", "🍉"]

def girar_rolo():
    for _ in range(10):  # quantidade de "giros" antes do final
        print(" | ".join(random.choices(simbolos, k=3)), end="\r")
        time.sleep(0.1)
    return [random.choice(simbolos) for _ in range(3)]

while True:
    print("\n===================================")
    print(f"💰 Saldo: R$ {saldo}")
    print("===================================\n")

    aposta = int(input("Quanto deseja apostar? R$ "))
    if aposta <= 0:
        print("A aposta deve ser maior que zero!")
        continue

    if aposta > saldo:
        print("Saldo insuficiente!")
        continue

    saldo -= aposta

    print("\n🎰 Girando...\n")
    time.sleep(0.5)

    resultado = girar_rolo()

    print(" | ".join(resultado))

    # Verificação de vitória
    if resultado[0] == resultado[1] == resultado[2]:
        ganho = aposta * 5
        saldo += ganho
        print(f"\n🎉 JACKPOT! Três iguais! Você ganhou R$ {ganho}!")
    elif resultado.count(resultado[0]) == 2 or resultado.count(resultado[1]) == 2:
        ganho = aposta * 2
        saldo += ganho
        print(f"\n✨ Dois iguais! Você ganhou R$ {ganho}!")
    else:
        print("\n❌ Você perdeu!")

    if saldo <= 0:
        print("\n💀 Você ficou sem saldo! Fim de jogo.")
        break

    jogar_novamente = input("\nQuer jogar de novo? (s/n): ").lower()
    if jogar_novamente != "s":
        break
    