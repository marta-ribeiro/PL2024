import sys
import re


def somador(linha, total, ligado):

    matches = re.finditer(r'-?\b\d+\b|\bon\b|\boff\b|(?<=\s)=(?=\s)', linha, re.IGNORECASE)
    for match in matches:
        match = match.group()
        if match == '=':
            print(total)
        elif match.upper() == 'ON':
            ligado = True
        elif match.upper() == 'OFF':
            ligado = False
        elif ligado:
            total += int(match)

    return total, ligado


def main():
    total, ligado = 0, False

    for linha in sys.stdin:
        total, ligado = somador(linha, total, ligado)


if __name__ == "__main__":
    main()
