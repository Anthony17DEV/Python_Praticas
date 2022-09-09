import random #Biblioteca de seleção aleatoria

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

for_pass = lower_case + upper_case + numbers #Concatenação das strings

tamanho = 8

password = "".join(random.sample(for_pass, tamanho)) #Seleção aleatoria de caracteres

print(f"Sua senha é: {password}")
