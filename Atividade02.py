def contar_letras_a(texto):
    contador = texto.lower().count('a')
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vezes.")
    else:
        print("A letra 'a' não aparece no texto.")

texto = input("Informe uma string: ")
contar_letras_a(texto)
