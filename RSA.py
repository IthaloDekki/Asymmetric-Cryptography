# Ex1: Realize a encriptação e decriptação usando o algoritmo RSA, para o seguinte: 

# Take user input for the day of the week
# option = input("Enter the option: ")

# # Match the day to predefined patterns
# match option:
#     case "a":
#         p = 3
#         q = 11
#         e = 7
#         m = 5
#     case "b":
#         p = 5
#         q = 11
#         e = 3
#         m = 9
#     case "c":
#         p = 7
#         q = 11
#         e = 17
#         m = 8
#     case "d":
#         p = 11
#         q = 13
#         e = 11
#         m = 7
#     case "e":
#         p = 17
#         q = 31
#         e = 7
#         m = 2


def calculo_lambda(p, q): 
    value = (p-1)*(q-1)
    return value


def encryption_rsa(m, e, n):
    value = (m**e) % n
    return value 

def decryption_rsa(c, d, n):
    return pow(c, d, n)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Atualiza a e b: a recebe b, b recebe o resto de a dividido por b
    return a  

def is_coprime(e, phi):
    return gcd(e, phi) == 1  # Dois números são coprimos se o MDC for 1


def mod_inverse(e, phi):  # Função para calcular o inverso modular usando o Algoritmo Estendido de Euclides
    for d in range(2, phi):  # Tentando valores de d entre 2 e phi-1
        if (e * d) % phi == 1:  # Verifica se e * d é congruente com 1 módulo phi
            return d  # Retorna o valor de d como inverso modular
    return -1  # Caso não encontre nenhum inverso, retorna -1


# n = p * q
# phi = calculo_lambda(p, q)
# verify_coprime = is_coprime(e, phi)

# if(verify_coprime):
#     public_ex = e;

# private_ex = mod_inverse(e, phi)  # Calcula o inverso modular
# C = encryption_rsa(m, public_ex, n)
# M = decryption_rsa(C, private_ex, n)

# print(f'Esse é o n: {n}')
# print(f'Esse é o phi: {phi}')
# print(f'Esse é o expoente publico: {public_ex}')
# print(f'Esse é a chave privada: {private_ex}')
# print(f'Essa é a mensagem cifrada: {C}')
# print(f'Essa é a mensagem desifrada: {M}')


# Ex2: Em um sistema de chave pública usando RSA, você intercepta o texto cifrado C = 
# 10 enviado a um usuário cuja chave pública é e = 5, n = 35. Qual é o texto claro M? 

def factorize_n(n):
    for i in range(2, int(n**0.5) + 1):  # Itera de 2 até √n
        if n % i == 0:  # Verifica se i é um divisor
            p = i
            q = n // i
            return p, q  # Retorna os fatores primos
    return None  # Caso não encontre fatores

# n = 35
# p, q = factorize_n(n)
# e = 5
# phi = calculo_lambda(p, q)
# d = mod_inverse(e, phi)
# M = decryption_rsa(10, d, 35)

# print(f'n fatorado: {p, q}')
# print(f"phi: {phi}")
# print(f'd: {d}')
# print(f'Texto Claro: {M}')


# Ex3:  Realize a encriptação e decriptação RSA da mensagem binária m = 0111001. 
# Considere p = 11, q = 23, e = 3. 

# p = 11
# q = 23
# e = 3
# m = '0111001'
# m = int(m, 2)

# n = p * q
# phi = calculo_lambda_n(p, q)
# verify_coprime = is_coprime(e, phi)

# if(verify_coprime):
#     public_ex = e;

# private_ex = mod_inverse(e, phi)  # Calcula o inverso modular
# C = encryption_rsa(m, public_ex, n)
# M = decryption_rsa(C, private_ex, n)

# print(f'Esse é o n: {n}')
# print(f'Esse é o m em decimal: {m}')
# print(f'Esse é o phi: {phi}')
# print(f'Esse é o expoente publico: {public_ex}')
# print(f'Esse é a chave privada: {private_ex}')
# print(f'Essa é a mensagem cifrada: {C}')
# print(f'Essa é a mensagem desifrada: {M}')


# Ex4: Utilizando a codificação ASCII, realize a encriptação e decriptação RSA da 
# mensagem "HELLO" Primos: p=11, q=17 Chave Pública: e=7

p = 11
q = 17
e = 7
n = p * q

phi = calculo_lambda(p, q)
d = mod_inverse(e, phi)

message = "HELLO"
ascii_values = [ord(char) for char in message]  # Codificar em ASCII

# Encriptação
encrypted = [encryption_rsa(m, e, n) for m in ascii_values]

# Descriptação
decrypted = [decryption_rsa(c, d, n) for c in encrypted]
decoded_message = ''.join(chr(m) for m in decrypted)  # Decodificar para texto


print(f"ASCII da mensagem: {ascii_values}")
print(f"Mensagem criptografada: {encrypted}")
print(f"Mensagem descriptografada: {decrypted}")
print(f"Mensagem descriptografada: {decoded_message}")