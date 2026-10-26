# Desafio Nível 1 — PDV com Descontos

## O que o código faz
Simula um PDV (Ponto de Venda) que calcula o valor final de compras aplicando descontos progressivos: um por idade do cliente e outro pelo valor da compra. Permite registrar várias compras seguidas e, ao encerrar, exibe um resumo do dia com quantidade de compras, total bruto, total de descontos e total final.

## Como ele faz
1. Entra em um loop e pede o **valor da compra**. Se for `0`, o loop termina.
2. Se o valor for negativo, mostra um aviso e pede novamente (`if` + `continue`).
3. Pede a **idade** do cliente. Se for negativa, mostra um aviso e pede novamente.
4. Se a idade for **maior ou igual a 65**, aplica 20% de desconto (`× 0.80`).
5. Se o valor **já descontado pela idade** for **maior que 100**, aplica mais 10% (`× 0.90`).
6. Arredonda o resultado para 2 casas, calcula o desconto concedido e exibe o valor final como `R$ 144.00`.
7. Guarda a compra (valor, idade, desconto, final) em uma lista com `.append()`.
8. Ao encerrar, percorre a lista com `for`, soma os totais e mostra o resumo.

## Como rodar
```
python pdv.py
```

## Tabela de exemplos (casos de teste)

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|-----------|-------|----------------|----------------|----------------------|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |
