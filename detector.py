from collections import defaultdict


tentativas = defaultdict(int)

LIMITE = int(input("Digite o número de tentativas para considerar suspeito: "))


with open("log.txt", "r") as file:
    for linha in file:
        if "Failed login" in linha:
            ip = linha.strip().split()[-1]
            tentativas[ip] += 1

LIMITE = 3

with open("relatorio.txt", "w") as relatorio:
    relatorio.write("IPs suspeitos:\n\n")

    for ip, count in tentativas.items():
        if count >= LIMITE:
            linha = f"{ip} -> {count} tentativas\n"
            print(linha.strip())
            relatorio.write(linha)
