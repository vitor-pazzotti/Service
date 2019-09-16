import re
import sys

def conta_texto(txt):
        text = re.findall(r'0+', txt)
        var = max(text)
        cont = var.count('0')
        print(f'A maior sequencia de zeros é: {cont}')
       
        return str(cont)