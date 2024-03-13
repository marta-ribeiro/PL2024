import re
import datetime
import json


def json_to_python():
    ficheiro = open("produtos.json", 'r')
    produtos = json.load(ficheiro)
    ficheiro.close()
    return produtos


def python_to_json(produtos):
    ficheiro = open("produtos.json", 'w')
    conteudo = json.dumps(produtos, indent=4)
    ficheiro.write(conteudo)
    ficheiro.close()


def lista_produtos(produtos):
    chave = produtos[0].keys()
    print(" | ".join(chave))
    for produto in produtos:
        print(" | ".join(str(produto[key]) for key in chave))


def pagamento(lista, num):
    saldo_euro = 0
    saldo_centimo = 0
    flag = 0
    if num == -1:
        num = 0
        flag = 1

    saldo_euro += int(num)
    saldo_centimo += (num % 1) * 100

    for moeda in lista:
        euro = re.match(r'\d+(?=e)', moeda)
        centimo = re.match(r'\d+(?=c)', moeda)

        if euro:
            saldo_euro += int(euro.group(0))
        elif centimo:
            saldo_centimo += int(centimo.group(0))

    while saldo_centimo >= 100:
        saldo_euro += 1
        saldo_centimo -= 100
    if flag == 0:
        print(f"SALDO = {saldo_euro}e{saldo_centimo}c")

    return saldo_euro + saldo_centimo * 0.01


def escolher_produto(produtos, id_prod, saldo):

    produto = produtos[int(id_prod) - 1]
    lista_custo = re.findall(r'\w+\d*', produto['preco'])

    saldo -= pagamento(lista_custo, -1)
    if saldo < 0:
        print("Não tem dinheiro suficiente.")
        saldo += pagamento(lista_custo, -1)
    elif produto['quant'] == 0:
        print("Este produto não está disponível")

    else:
        euro = int(saldo)
        centimo = (saldo % 1) * 100
        produto['quant'] -= 1
        print(f"SALDO = {euro}e{centimo}c")

    return saldo


def sair(saldo):

    troco = ['2e', '1e', '50c', '20c', '10c', '5c', '2c', '1c']
    valores = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    quantidade = [0, 0, 0, 0, 0, 0, 0, 0]
    i = 0

    for moeda in valores:
        while saldo >= moeda:
            saldo = round(saldo, 2)
            saldo -= moeda
            quantidade[i] += 1
        i += 1

    j = 0
    print("Pode retirar o troco: ", end=' ')
    while j < 8:
        if quantidade[j] != 0:
            print(f"{quantidade[j]}x {troco[j]}", end=' ')
        j += 1

    print("\nAté à próxima!")


def main():
    saldo = 0
    produtos = json_to_python()
    print("-----MÁQUINA DE VENDING-----")
    print(f"{datetime.datetime.now().strftime('%d-%m-%Y')}, Stock carregado, Estado atualizado.")
    print("Bom dia. Estou disponível para atender o seu pedido.\n")
    print("LISTAR - lista de produtos\n"
          "MOEDA (Xe, Xc). - dinheiro a inserir\n"
          "SELECIONAR X - escolher produto a comprar\n"
          "SAIR - finalizar compra")
    opcao = input("\n>> ")
    er = re.findall(r'\w+\d*', opcao)
    x = er[0]

    while x.upper() != 'SAIR':
        if x.upper() == 'LISTAR':
            lista_produtos(produtos)
        elif x.upper() == 'MOEDA':
            er.pop(0)
            saldo = pagamento(er, saldo)
        elif x.upper() == 'SELECIONAR':
            er.pop(0)
            saldo = escolher_produto(produtos, er[0], saldo)
        else:
            print("O comando que introduziu não é aceite. Tente outra vez.")
        opcao = input("\n>> ")
        er = re.findall(r'\w+\d*', opcao)
        x = er[0]
    sair(saldo)
    python_to_json(produtos)


if __name__ == "__main__":
    main()
