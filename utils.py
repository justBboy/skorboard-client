import random

def generate_id(length):
    dig = "123456789abcdefghijklmnopqrstuvwxyz_?/."
    new_id = ""
    for i in range(length):
        ch = dig[random.randrange(len(dig))]
        new_id += ch

    return new_id