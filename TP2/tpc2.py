import re


def cabecalho(header):

    ans = re.sub(r"#([\w\s]*)", r"<h1>\1</h1>", header)
    return ans


def negrito(bold):

    ans = re.sub(r"\*\*([\w\s]*)\*\*", r"<b>\1</b>", bold)
    return ans


def italico(italic):
    ans = re.sub(r"\*{1}([\w\s]+)\*{1}", r"<i>\1</i>", italic)
    return ans


def endereco(link):

    ans = re.sub(r"\[([\w\s]+)]\(([\w.:/]+)\)", r'<a href="\2">\1</a>', link)
    return ans


def imagem(image):
    ans = re.sub(r"!\[([\w\s]+)]\(([\w.:/]+)\)", r'<img src="\2" alt="\1"/>', image)
    return ans


def main():

    print(cabecalho("#Exemplo de titulo"))
    print(negrito("** Olha que lindo **"))
    print(italico("*Fica em italicooooo *"))
    print(endereco("[página da UC](http://www.uc.pt)"))
    print(imagem("![imagem dum coelho](http://www.coellho.com)"))


if __name__ == "__main__":
    main()
