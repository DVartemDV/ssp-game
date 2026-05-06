from tkinter import *
from random import *
root = Tk()
root['bg'] = 'white'
root.title('КБН')
root.geometry('500x500')
root.resizable(width=False, height=False)
labelText = Label(root, text='', fg='black', font=('', 20))
labelText.place(y = 200, x = 200)
# Логика Результатов
rules = {
    'Ножницы': 'Бумага',
    "Камень": "Ножницы",
    "Бумага": "Камень"
}
# Функция выбора

def play_game(player_choice):
    computer_choice = choice(['Камень', 'Ножницы', "Бумага"])
    if computer_choice == player_choice:
        result = 'Ничья'
    elif rules[player_choice] == computer_choice:
        result = 'Победа'
    else:
        result = 'Поражение'
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
stone.place(x = 350, y = 50)

scissors = Button(root,
               text='Ножницы',
               font=('', 20),
               fg= 'black',
               activebackground= 'gray',
               command = lambda: play_game("Ножницы")
               )
scissors.place(x = 10, y = 50)

paper = Button(root,
               text='Бумага',
               font=('', 20),
               fg= 'black',
               activebackground= 'gray',
               command = lambda: play_game("Бумага")
               )
paper.place(x = 200, y = 50)
# Вывод результатов
result_label = Label(root, text='', font= ('', 20))
result_label.place(x = 180, y = 400)
computer_choice_label = Label(root, text='', font=('', 20))
computer_choice_label.place(x = 200, y = 200)

root.mainloop()
