matriz = [None] * 12
for i in range(0, 12):
    matriz[i] = [None] * 12

linha = int(input())
operacao = input()
for i in range(0, 12):
    for j in range(0, 12):
        matriz[i][j] = float(input())

soma = 0
for j in range(0, 12):
    soma += matriz[linha][j]
media = soma / 12

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{media:.1f}')
