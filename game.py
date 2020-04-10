from tkinter import *
import random

words = {
    'Транспорт': ['автобус', 'троллейбус', 'метро', 'самолет', 'трамвай', 'автомобиль', 'катер', 'велосипед', 'самокат',
                  'вертолет'],
    'Зимние вид спорта': ['хоккей', 'кёрлинг', 'биатлон', 'фристайл', 'бобслей', 'скелетон'],
    'Летние виды спорта': ['гребля', 'футбол', 'волейбол', 'дзюдо', 'плавание', 'фехтование'],
    'Обезьянки': ['макака', 'примат', 'арангутанг', 'горилла', 'бонобо', 'павиан', 'мартышка', 'шимпанзе', 'носач',
                  'мандрил', 'капуцин'],
    'Собаки': ['хаски', 'овчарка', 'корги', 'самоед', 'такса', 'дворняга', 'боксер', 'пудель', 'далматинец', 'шпиц',
               'эрдельтерьер', 'мопс', 'балонка'],
    'Крупа': ['гречка', 'булгур', 'пшено', 'рис', 'манка', 'овсянка', 'перловка', 'чечевица', 'горох', 'ячневая'],
    "Геометрические фигуры": ["прямоугольник", "параллелепипед", "цилиндр", "пирамида", "спираль", "октаэдр",
                              "параллелограмм"],
    'Стили изобразительного искусства': ["абстракционизм", "авангардизм", "андеграунд", "импрессионизм",
                                         "экспрессионизм", "сюрреализм", "символизм", "модерн", "неоклассицизм"],
    "Физика": ['дифракция', 'интерференция', 'парообразование', 'радиоактивность', 'сверхпроводимость', 'античастица',
               'дуальность', 'теплопроводность'],
    'HARD': ["превысокомногорассмотрительствующий", "рентгеноэлектрокардиографический", "человеконенавистничество",
             "высокопревосходительство",
             "одиннадцатиклассница", "делопроизводительница", "электрофотополупроводниковый",
             "водогрязеторфопарафинолечение"],
}
lst_theme = list(words.keys())
print(lst_theme)
# lst_theme = ['Транспорт', 'Зимние вид спорта', 'Летние виды спорта', 'Обезьянки', 'Собаки', 'Крупа',
# 'Геометрические фигуры', 'Стили изобразительного искусства', 'Физика', 'HARD']
coor_line = [[100, 50, 100, 300], [100, 50, 230, 50], [100, 80, 130, 50], [70, 300, 130, 300], [230, 50, 230, 80],
             ['oval', 210, 80, 250, 120], ['oval', 210, 120, 250, 200], [240, 130, 280, 100], [220, 130, 180, 100],
             [240, 190, 280, 240], [220, 190, 180, 240]]
mistake_count = 0
root = Tk()
root.title("Виселица")
root.geometry('950x480+250+100')


def main():
    # нажали на "Начать игру"
    def change(event):
        theme = str(lst_theme[r_var.get()])
        print(theme)
        word = words[theme]
        sec_lst = random.choice(word)
        print(sec_lst)
        game_lst = ['_ '] * len(sec_lst)
        # clear
        label_name_game.destroy()
        label_change_theme.destroy()
        button_start.destroy()
        radio_theme.destroy()
        line.destroy()
        game(sec_lst, game_lst)

    # оформляем начальный экран
    label_name_game = Label(text="Виселица", font=("Comic Sans MS", 24, "bold"), fg='#220078')
    label_change_theme = Label(text='Выберите тему', font=("Comic Sans MS", 14), fg='#220078')
    button_start = Button(text="Начать игру", width=15, height=3, fg='#220078')
    button_start.bind('<Button-1>', change)

    # Радиокнопки для выбора темы
    r_var = IntVar()
    i = 0  # для размещения кнопок
    j = 0  # для значений кнопок

    for theme in lst_theme:
        radio_theme = Radiobutton(root, text=theme, variable="r_var", value=j)
        radio_theme.place(x=510, y=150 + i)
        i += 20
        j += 1

    # размещаем все, что смогли написать
    label_name_game.place(x=500, y=30)
    label_change_theme.place(x=510, y=100)
    button_start.place(x=500, y=400)

    # рисуем висельника, чтобы было красивешно
    line = Canvas(root, width=480, height=480, bg='white')
    for coor in coor_line:
        if coor[0] == 'oval':
            line.create_oval(coor[1], coor[2], coor[3], coor[4], fill='white', outline='#220078', width=5)
        else:
            line.create_line(coor[0], coor[1], coor[2], coor[3], fill='#220078', width=5)
        line.place(x=0, y=0)


def game(sec_lst, game_lst):
    def word(game_lst):
        global encrypted_word
        encrypted_word = Label(game_canvas, text=''.join(game_lst), font=("Comic Sans MS", 24, "bold"),
                               fg='#220078')
        encrypted_word.place(x=20, y=400)

    def change_ok(event):
        global mistake_count

        def victory():

            # Нажали "Сыграть еще раз"
            def change_win(event):
                canvas_win.destroy()
                label_win.destroy()
                button_alive.destroy()

                game_canvas.destroy()
                encrypted_word.destroy()
                en_let.destroy()
                button_ok.destroy()
                label_info.destroy()

                main()

            canvas_win = Canvas(root, bg="white", width=920, height=480)
            label_win = Label(text="Вы победили", font=("Comic Sans MS", 72), fg='black')
            label_win.place(x=50, y=200)
            button_alive = Button(text="Сыграть еще раз")
            button_alive.place(x=360, y=400)
            button_alive.bind('<Button-1>', change_win)
            canvas_win.place(x=0, y=0)

        def mistake(n):
            coor = coor_line[n - 1]
            if coor[0] == 'oval':
                game_canvas.create_oval(coor[1], coor[2], coor[3], coor[4], fill='white',
                                        outline='#220078', width=5)
            else:
                game_canvas.create_line(coor[0], coor[1], coor[2], coor[3], fill='#220078',
                                        width=5)

        def losing():

            # Нажали "Попробовать еще раз"
            def change_los(event):
                canvas_los.destroy()
                label_dead.destroy()
                button_alive.destroy()

                game_canvas.destroy()
                encrypted_word.destroy()
                en_let.destroy()
                button_ok.destroy()
                label_info.destroy()

                main()

            canvas_los = Canvas(root, bg="red", width=950, height=480)
            label_dead = Label(canvas_los, text="you died", font=("Comic Sans MS", 72), fg='black',
                               bg='red')
            label_dead.place(x=200, y=200)
            button_alive = Button(canvas_los, text="Попробовать еще раз")
            button_alive.place(x=480, y=360)
            button_alive.bind('<Button-1>', change_los)
            canvas_los.place(x=0, y=0)

        let = en_let.get()
        if let in sec_lst:
            for i, sym in enumerate(sec_lst):
                if sym == let:
                    game_lst[i] = sym
            if '_ ' not in game_lst:
                victory()
        else:
            mistake_count += 1
            mistake(mistake_count)
            if mistake_count == 11:
                losing()

        encrypted_word.destroy()
        word(game_lst)

    # оформление игры
    game_canvas = Canvas(root, width=1000, height=1000)
    game_canvas.pack()
    word(game_lst)
    en_let = Entry(width=1)
    en_let.place(x=430, y=350)
    button_ok = Button(game_canvas, text="ok")
    button_ok.place(x=450, y=350)
    label_info = Label(game_canvas,
                       text="Введите одну любую букву, которая как вы считаете есть в этом слове: ")
    label_info.place(x=200, y=300)
    button_ok.bind('<Button-1>', change_ok)


main()
root.mainloop()
