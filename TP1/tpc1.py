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
    return ordenado

def perc_aptos(resultado):
    i = 0
    for n in resultado:
        if n == 'true':
            i+=1

    return i
def main():
    idade = []
    modalidade = []
    resultado = []
    ler_ficheiro(idade,modalidade,resultado)

    print(mod_ordenadas(modalidade))
    print(perc_aptos(resultado))



if __name__ == "__main__":
    main()

#   _id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado