import random
import string
import re
import hashlib

def geraSenha():
    
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(10))

def valida_senha(senha):

    nivel = -1
    
    if len(senha) == 0:
        nivel == -1
        print(nivel)
        return nivel

    if len(senha) <= 5:
        if re.findall(r"[A-Za-z]", senha) and re.findall(r"[@#$%^&]", senha):
            nivel += 2
            print(nivel)
        else:
            nivel += 1
            print(nivel)
        return nivel
    
    if len(senha) <= 8:
        if re.findall(r"[A-Za-z]", senha) and re.findall(r"[0-9]", senha):
            nivel += 2
            print(nivel)
        else:
            nivel += 1
            print(nivel)
        return nivel

    if len(senha) > 8:
        if re.findall(r"[A-Za-z]", senha) and re.findall(r"[0-9]", senha) and re.findall(r"[@#$%^&]", senha):
            nivel += 3
            print(nivel)
        else:
            nivel += 2
            print(nivel)
        return nivel

def hash_md5(pwd):
    pwd.encode('utf-8')
    cripto = hashlib.md5()
    # cripto.update(pwd)
    return cripto.hexdigest()