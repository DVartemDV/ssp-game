from tkinter import *
from random import *
root = Tk()
root['bg'] = 'white'
root.title('КБН')
root.geometry('500x500')
root.resizable(width=False, height=False)

# Комбо
player_combo_count = 0
max_combo= 0
combo = 0
last_max_combo = 0

# Логика Результатов
rules = {
    'Ножницы': 'Бумага',
    "Камень": "Ножницы",
    "Бумага": "Камень"
}

# Функция выбора
def play_game(player_choice):
    global max_combo
    global combo
    global result_text_label
    computer_choice = choice(['Камень', 'Ножницы', "Бумага"])
    if computer_choice == player_choice:
        result = 'Ничья'
        result_text_label.configure(fg='orange')
    elif rules[player_choice] == computer_choice:
        result = 'Победа'
        combo += 1 # При победе счетчки комбо возрастает
        label_player_combo_count.configure(text=str(f'{combo}'))
        result_text_label.configure(fg='green')
        if combo > max_combo:
            max_combo_label.configure(text=(f'{combo}'))
            max_combo = combo
    else:
        result = 'Поражение'
        combo = 0 # При поражении комбо обнуляется
        label_player_combo_count.configure(text=str(f'{combo}'))
        result_text_label.configure(fg='red')
    result_label.configure(text=result)
    computer_choice_label.configure(text=computer_choice)

# Варианты
stone = Button(root,
               text='Камень',
               font=('', 20),
               fg= 'black',
               activebackground= 'gray',
               command = lambda: play_game("Камень")
               )


scissors = Button(root,
               text='Ножницы',
               font=('', 20),
               fg= 'black',
               activebackground= 'gray',
               command = lambda: play_game("Ножницы")
               )


paper = Button(root,
               text='Бумага',
               font=('', 20),
               fg= 'black',
               activebackground= 'gray',
               command = lambda: play_game("Бумага")
               )

# Создание объектов
result_label = Label(root, text='', font= ('', 20))
computer_choice_label = Label(root, text='', font=('', 30))
label_player_combo_count = Label(root, text=f'{player_combo_count}', font=('',20), bg='white')
result_text_label = Label(root, text='result', font=('', 20), bg='white', fg='blue')
label_combo_text = Label(root, text='combo', font=('', 20), bg='white')
max_combo_label = Label(root, text=f'{max_combo}', font=('',20), bg='white')
max_combo_text = Label(root, text='max_combo', font=('', 20), bg='white')

# Вывод объектов
result_label.place(x = 180, y = 100)
computer_choice_label.place(x = 180, y = 200)
label_player_combo_count.place(x=100,y=1)
result_text_label.place(x=100,y=100)
max_combo_label.place(x=475,y=1)
max_combo_text.place(x=320, y=1)

stone.place(x = 350, y = 327)
scissors.place(x = 10, y = 327)
paper.place(x = 200, y = 327)
label_combo_text.place(x=1,y=1)
root.mainloop() # работа программы