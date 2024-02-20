import re
import sys


def parse_html(linha):
    # HEADER
    linha = re.sub(r"\B### (.+)", r"<h3>\1</h3>", linha)
    linha = re.sub(r"\B## (.+)", r"<h2>\1</h2>", linha)
    linha = re.sub(r"\B# (.+)", r"<h1>\1</h1>", linha)
    # ITALIC
    linha = re.sub(r"[^\*]\*(\w[\w\s]+\w)\*", r"<i>\1</i>", linha)
    # BOLD
    linha = re.sub(r"\*\*(\w[\w\s]*\w)\*\*", r"<b>\1</b>", linha)
    # IMAGEM
    linha = re.sub(r"!\[([\w\s]+)]\(([\w.:/]+)\)", r'<img src="\2" alt="\1"/>', linha)
    # ENDEREÇO
    linha = re.sub(r"\[([\w\s]+)]\(([\w.:/]+)\)", r'<a href="\2">\1</a>', linha)
    # LISTA
    linha1 = re.sub(r"\d*\. ([\w ]+)", r"<li>\1</li>", linha)
    linha = re.sub(r"(<li>.*</li>[\n]?)+", r"<ol>\n\g<0></ol>", linha1)
    return linha


def main():

    ficheiro_html = open("example.html", "w")
    ficheiro_html.write(parse_html(sys.stdin.read()))
    ficheiro_html.close()


if __name__ == "__main__":
    main()
