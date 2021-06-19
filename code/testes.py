
def total_seconds():
    return 0.3


word = "now"

palavras = []
for _ in range(5):
    palavra = "\"" + word + "\"" + " : [" + str(total_seconds()) + ", " + str(total_seconds()) + "],"
    palavras.append(palavra)

# print(palavras[0])


def save_in_text_file(all_words):
    with open('all_words.py', 'w') as f:
        for element in all_words:
            f.write(element + "\n")


save_in_text_file(palavras)
