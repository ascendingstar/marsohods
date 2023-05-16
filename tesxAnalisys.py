import re
import pandas as pd

# Чтение файла
with open('Уэллс_-_Война_миров.txt', 'r') as f:
    data = f.read()

words = [word.lower() for word in re.findall(r'\b(?!(?:и|в|на|не|но|с|к|до|у|о|за|из|по|от|а|же|то|В)\b)[\w-]+\b', data)]
word_counts = pd.Series(words).value_counts()

# Отбор 20 наиболее употребительных слов
top_words = word_counts.head(20)

print(top_words)


# Построение гистограммы
top_words.plot(kind='bar')

# Сводка по файлу
num_chars = len(data)
num_chars_nospace = len(data.replace(' ', ''))
num_words = len(words)
num_lines = data.count('\n') + 1

print(f"Количество символов (с пробелами): {num_chars}")
print(f"Количество символов (без пробелов): {num_chars_nospace}")
print(f"Количество слов: {num_words}")
print(f"Количество строк: {num_lines}")