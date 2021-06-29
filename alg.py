from random import randint

# public key
a = 5
b = 19

print("public key: {0} mod {1}".format(a, b))

# secret nums
s1 = randint(1, 50)
s2 = randint(1, 50)


def calc(a, b, c):
    return a ** c % b


# generate secret key
def genkey():
    bk = calc(a, b, s1)
    ak = calc(a, b, s2)

    key1 = calc(ak, b, s1)
    key2 = calc(bk, b, s2)

    if key1 == key2:
        return key1
    else:
        exit(1)


def encode(msg, key):
    enc = ""
    for i in msg:
        enc += chr(ord(i) + key)

    return enc


def decode(msg, key):
    dec = ""
    for i in msg:
        dec += chr(ord(i) - key)

    return dec


m = "Hello, world!"
k = genkey()
em = encode(m, k)

print("encoded message: {0}".format(em))
print("decoded message: {0}".format(decode(em, k)))
