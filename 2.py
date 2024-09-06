def contar_a(string):
    count = string.lower().count('a')
    return count

string = input("Informe uma string: ")
quantidade = contar_a(string)
print(f"A letra 'a' aparece {quantidade} vezes na string.")
