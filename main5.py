import re

from laba5_s import Sentence
def process_text_file(input_filename, replacements, words_to_delete):
    total_words_count = 0
    updated_lines = []

    try:

        with open(input_filename, 'r', encoding='utf-8') as file:
            for line in file:

                raw_words = re.findall(r'\w+', line, re.UNICODE)
                sentence = Sentence(raw_words)
                for i in range(len(sentence)):
                    if sentence[i] in replacements:
                        sentence[i] = replacements[sentence[i]]
                for word in words_to_delete:
                    sentence = sentence - word

                total_words_count += len(sentence)
                updated_lines.append(str(sentence))
        print(" ЗМІНЕНИЙ ТЕКСТ")
        for line in updated_lines:
            print(line)

        print(f"\nЗагальна кількість слів у тексті: {total_words_count}")

    except FileNotFoundError:
        print(f" Не вдалося знайти файл '{input_filename}'. Перевір")


if __name__ == "__main__":

    replacements_map = {"програмування": "Python"}
    delete_list = ["це", "та"]


    filename = "text5.txt"

    process_text_file(filename, replacements_map, delete_list)