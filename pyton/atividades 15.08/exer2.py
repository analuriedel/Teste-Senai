deslocamento = int(input("Digite o deslocamento: "))
# *int*=Transforma uma string em número inteiro
texto = input("Digite o texto a ser criptografado: ")
texto_criptografado = ""
for letra in texto:
    if letra.isupper():
        letra_criptografada = chr((ord(letra.lower()) + deslocamento - 97) % 26 + 65)
    elif letra.islower():
#*elif*=Usa o if e o else ao mesmo tempo
        letra_criptografada = chr((ord(letra) + deslocamento - 97) % 26 + 97)
    else: letra_criptografada = texto_criptografado + letra_criptografada
    print("Texto criptografado:", texto_criptografado)