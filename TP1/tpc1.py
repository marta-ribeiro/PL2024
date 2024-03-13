def ler_ficheiro(idade,modalidade,resultado):
    ficheiro = open("emd.csv")
    ficheiro.readline()  # passa à frente o cabeçalho
    for linha in ficheiro:
        campos = linha.split(",")
        idade.append(int(campos[5]))
        modalidade.append(campos[8])
        resultado.append(campos[12].rstrip()) # para tirar o new line

    ficheiro.close()

def mod_ordenadas(modalidade):
    ordenado = []
    for n in modalidade:
        if n not in ordenado:
            ordenado.append(n)
    ordenado.sort()
    print("\n----- Aqui estão as modalidades ordenadas: -----\n")
    for mod in ordenado:
        print(f"- {mod}")


def perc_aptos(resultado):
    i = 0
    for n in resultado:
        if n == 'true':
            i+=1
    aptos = (i / len(resultado)) * 100
    print("\n----- Percentagem de atletas aptos e inaptos para a prática desportiva. -----\n")
    print(f"{aptos}% dos atletas estão aptos e {100-aptos}% dos atletas estão inaptos para a pŕatica desportiva.")

def dist_idades(idade):
    distribuicao = {}

    for i in range(len(idade)):
        decisao = (idade[i] // 5) * 5
        if decisao in distribuicao:
            distribuicao[decisao] +=1
        else:
            distribuicao.update({decisao: 1})

    ordem = dict(sorted(distribuicao.items()))

    print("\nDistribuição dos atletas pela faixa etária: ")
    print(">----------------|--------------<")
    print(">-[Faixa etária]-|-[Nº Atletas]-<")
    print(">----------------|--------------<")
    for key, valor in ordem.items():
        if valor < 10:
            print(f">    [{key},{key + 4}]     |      {valor}       <")
        elif valor < 100:
            print(f">    [{key},{key + 4}]     |      {valor}      <")
        else:
            print(f">    [{key},{key + 4}]     |      {valor}     <")
    print(">----------------|--------------<")


def main():
    idade = []
    modalidade = []
    resultado = []
    ler_ficheiro(idade,modalidade,resultado)

    print("O que pretende obter? ")
    print("1. Lista das modalidades ordenada alfabeticamente.\n"
          "2. Percentagem de atletas aptos e inaptos para a prática desportiva.\n"
          "3. Distribuição de atletas por escalão etário.\n"
          "0. Sair.")
    opcao = int(input("\nEscolha: "))

    while opcao!=0 :
        if opcao == 1:
            mod_ordenadas(modalidade)
        elif opcao == 2:
            perc_aptos(resultado)
        elif opcao == 3:
            dist_idades(idade)
        else:
            print("O valor que introduziu não é aceite. Tente outra vez.")
        opcao = int(input("\nEscolha: "))

if __name__ == "__main__":
    main()