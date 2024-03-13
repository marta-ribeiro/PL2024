import re
import datetime


def lista_produtos(num):
    produtos = {'1': ('água', '50c'),
                '2': ('bolo', '70c'),
                '3': ('bolachas', '60c'),
                '4': ('sumo', '1e'),
                '5': ('batatas', '1e 10c')}

    if num == 1:
        print("id |nome |preço")

        for chave in produtos:
            print(f"{chave} {produtos[chave][0]} {produtos[chave][1]}")
    else:
        return produtos


def pagamento(lista, num):
    saldo_euro = 0
    saldo_centimo = 0
    flag = 0
    if num == -1:
        num = 0
        flag = 1

    saldo_euro += int(num)
    saldo_centimo += int((num % 1) * 100)

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


def escolher_produto(id_prod, saldo):

    produtos = lista_produtos(2)
    custo = produtos[id_prod][1]
    lista_custo = re.findall(r'\w+\d*', custo)

    saldo -= pagamento(lista_custo, -1)
    euro = int(saldo)
    centimo = int((saldo % 1) * 100)
    print(f"SALDO = {euro}e{centimo}c")

    return saldo


def sair(saldo):

    print(f"TROCO {int(saldo)}e{int((saldo % 1) * 100)}c")


def main():
    saldo = 0
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
            lista_produtos(1)
        elif x.upper() == 'MOEDA':
            er.pop(0)
            saldo = pagamento(er, saldo)
        elif x.upper() == 'SELECIONAR':
            er.pop(0)
            saldo = escolher_produto(er[0], saldo)
        else:
            print("O comando que introduziu não é aceite. Tente outra vez.")
        opcao = input("\n>> ")
        er = re.findall(r'\w+\d*', opcao)
        x = er[0]
    sair(saldo)


if __name__ == "__main__":
    main()
