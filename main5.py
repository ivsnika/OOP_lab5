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
                if "програмування" in sentence:
                    print("Знайдено ключове слово 'програмування' у реченні")
                for i in range(len(sentence)):
                    if sentence[i] in replacements:
                        sentence[i] = replacements[sentence[i]]
                for word in words_to_delete:
                    sentence = sentence - word

                total_words_count += len(sentence)
                updated_lines.append(sentence)  

        for sentence_obj in updated_lines:
            print(sentence_obj)

        print(f"\nКількість слів: {total_words_count}")

        if updated_lines:
            print("\nЗЛИТТЯ РЕЧЕНЬ")
            extra_sentence = Sentence(["Це", "додаткові", "слова"])
            combined_sentence = updated_lines[0] + extra_sentence
            print(f"Початкове: {updated_lines[0]}")
            print(f"Додаткове: {extra_sentence}")
            print(f"Результат: {combined_sentence}")

    except FileNotFoundError:
        print(f"Помилка: Файл '{input_filename}' не знайдено")


if __name__ == "__main__":
    replacements_map = {"програмування": "Python"}
    delete_list = ["Це", "та"]
    filename = "text5.txt"

    process_text_file(filename, replacements_map, delete_list)
