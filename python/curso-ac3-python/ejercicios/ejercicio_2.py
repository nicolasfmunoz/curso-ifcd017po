lorem = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC,making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of 'de Finibus Bonorum et Malorum' (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum,'Lorem ipsum dolor sit amet..'"


# Ejercicio 1

# Ejercicio 2
text_lowercase = lorem.lower()

count_words_it = text_lowercase.count('it')
print('\n', f'La palabra "it" aparece {count_words_it} veces en el texto.')

word_to_search = 'ipsum'
print('\n', f'"{word_to_search}" encontrada:', word_to_search in text_lowercase)

lista = lorem.split(' ')
print('\n', 'Total de palabras: ', len(lista))

print('\n', 'la palabra "Richard" se encuentra en la posición', text_lowercase.index('richard'))

print('\n', text_lowercase)

print('\n', lista)
