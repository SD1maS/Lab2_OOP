import re

class TextOperations:

    @staticmethod
    def find_unique_word(text: str) -> str:
        if not text or not text.strip():
            raise ValueError("Текст не може бути порожнім.")

        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]

        if len(sentences) <= 1:
            raise ValueError("Текст повинен містити щонайменше два речення для порівняння.")

        def extract_words(sentence: str) -> list[str]:
            return [word.lower() for word in re.findall(r'\b\w+\b', sentence)]

        first_sentence_words = extract_words(sentences[0])
        
        if not first_sentence_words:
            raise ValueError("Перше речення не містить слів.")

        other_sentences_words = set()
        for sentence in sentences[1:]:
            other_sentences_words.update(extract_words(sentence))

        for word in first_sentence_words:
            if word not in other_sentences_words:
                return word

        return "Унікального слова не знайдено."


def main():
    sample_text = (
        "Lorem ipsum dolor sit amet, integer nec euismod magna."
        "Nunc vehicula orci at metus fringilla, eget posuere nunc blandit."
        "Etiam fringilla libero quis tempor semper."
    )

    try:
        print("\n\n\033[1mЗаданий текст:\033[0m")
        print(sample_text)
        print("\n\033[1mДія: Пошук унікального слова першого речення\033[0m")
        
        result = TextOperations.find_unique_word(sample_text)
        print(f"Результат: '{result}'\n\n")

    except ValueError as e:
        print(f"Помилка даних: {e}")
    except Exception as e:
        print(f"Непередбачувана помилка: {e}")


if __name__ == "__main__":
    main()