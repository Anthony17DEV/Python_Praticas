import random #Biblioteca de seleção aleatoria

Local = input("Para qual local será essa senha? :")

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

for_pass = lower_case + upper_case + numbers #Concatenação das strings

tamanho = 8

senha = "".join(random.sample(for_pass, tamanho)) #Seleção aleatoria de caracteres

print(f"Sua senha é: {senha}")

arquivo = open("Senhas.txt", "a")
arquivo.write(f"\n\nLocal = {Local}\nSenha = {senha}")

print("Sua senha foi criada e armazenada")
