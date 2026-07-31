import random

def gen_psw():
    caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    lun = 10
    password = ""
    for i in range(lun):
        password += random.choice(caratteri)

    return password