import re
from collections import Counter

class WordCounter:
    def __init__(self, text):
        self.text = text

    def clean_text(self):
        """Приводим текст к нижнему регистру и удаляем знаки препинания"""
        cleaned_text = re.sub(r'[^\w\s]', '', self.text.lower())
        return cleaned_text

    def count_words(self):
        cleaned_text = self.clean_text()
        """Разделяем текст на слова и подсчитываем их количество"""
        word_count = Counter(cleaned_text.split())
        return word_count

    def get_top_10_words(self):
        word_count = self.count_words()
        """Сортируем слова по количеству встречаемости и возвращаем 10 самых часто встречающихся слов"""
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:10]

text = """Python is an interpreted high-level general-purpose programming language.
         Python's design philosophy emphasizes code readability with its notable use of significant indentation.
         Python has a large standard library, commonly cited as one of its greatest strengths,
         providing tools suited to many tasks."""

counter = WordCounter(text)
print(counter.get_top_10_words())
