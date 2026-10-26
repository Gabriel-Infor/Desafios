# PDV com descontos progressivos (Nível 1)
# Regras: 20% se idade >= 65; depois +10% se o valor já descontado for > 100.

historico = []

print("=== PDV - Ponto de Venda ===")
print("Digite 0 no valor da compra para encerrar.\n")

while True:
    valor = float(input("Valor da compra (R$): "))

    if valor == 0:
        break

    if valor < 0:
        print("Aviso: o valor não pode ser negativo. Tente novamente.\n")
        continue

    idade = int(input("Idade do cliente: "))

    if idade < 0:
        print("Aviso: a idade não pode ser negativa. Tente novamente.\n")
        continue

    valor_final = valor

    # Regra 1: desconto por idade
    if idade >= 65:
        valor_final = valor_final * 0.80

    # Regra 2: desconto por valor (sobre o valor já descontado pela idade)
    if valor_final > 100:
        valor_final = valor_final * 0.90

    valor_final = round(valor_final, 2)
    desconto = round(valor - valor_final, 2)

    historico.append({
        "valor": valor,
        "idade": idade,
        "desconto": desconto,
        "final": valor_final,
    })

    print(f"Valor final: R$ {valor_final:.2f}\n")

# Resumo do dia
total_bruto = 0
total_descontos = 0
total_final = 0

for compra in historico:
    total_bruto += compra["valor"]
    total_descontos += compra["desconto"]
    total_final += compra["final"]

print("\n=== RESUMO DO DIA ===")
print(f"Quantidade de compras: {len(historico)}")
print(f"Total bruto:           R$ {total_bruto:.2f}")
print(f"Total de descontos:    R$ {total_descontos:.2f}")
print(f"Total final:           R$ {total_final:.2f}")
