import tkinter as tk
import random

# Слова для угадывания
words = ['яблоко', 'апельсин', 'компьютер', 'мороженое', 'пицца', 'палач']

# Функция для выбора случайного слова
def choose_word():
    return random.choice(words)

# Функция для обновления отображения загаданного слова
def update_display(word, guesses):
    display_word = ''
    for letter in word:
        if letter in guesses:
            display_word += letter + ' '
        else:
            display_word += '_ '
    word_label.config(text=display_word)

# Функция для обработки попытки угадать букву
def guess_letter():
    letter = letter_entry.get()
    if len(letter) != 1:
        result_label.config(text="Введите одну букву!")
        return
    if letter in guesses:
        result_label.config(text="Вы уже угадали эту букву!")
        return
    guesses.append(letter)
    update_display(word, guesses)
    if letter not in word:
        wrong_guesses_left = 6 - len(wrong_guesses)
        wrong_guesses.append(letter)
        hangman_label.config(text='Ошибки: ' + ' '.join(wrong_guesses))
        result_label.config(text=f"Неправильно! Осталось {wrong_guesses_left} попыток.")
        if len(wrong_guesses) == 6:
            result_label.config(text=f"Вы проиграли! Загаданное слово: {word}.")
            letter_entry.config(state=tk.DISABLED)
            submit_button.config(state=tk.DISABLED)
    else:
        if all(letter in guesses for letter in word):
            result_label.config(text="Вы победили!")
            letter_entry.config(state=tk.DISABLED)
            submit_button.config(state=tk.DISABLED)

# Создание графического интерфейса
window = tk.Tk()
window.title("Палачи")

# Выбор случайного слова
word = choose_word()
guesses = []
wrong_guesses = []

# Элементы интерфейса
word_label = tk.Label(window, text='_ ' * len(word), font=('Arial', 24))
word_label.pack(pady=10)

letter_entry = tk.Entry(window, font=('Arial', 18))
letter_entry.pack(pady=10)

submit_button = tk.Button(window, text="Угадать", command=guess_letter)
submit_button.pack(pady=10)

hangman_label = tk.Label(window, text='Ошибки:', font=('Arial', 18))
hangman_label.pack()

result_label = tk.Label(window, text='', font=('Arial', 18))
result_label.pack()

# Запуск интерфейса
window.mainloop()