import tkinter
from tkinter import*
from tkinter.filedialog import askopenfile, asksaveasfile #функции сохранить как  и открыть как файл
from tkinter.messagebox import showerror #показ всех ошибок
from tkinter import messagebox #уведомления приложения

from settings import* #импортируем настройки
from set import* #импортруем методы класса

app = tkinter.Tk() #создаю окно приложения
app.title(APP_NAME) #указываем название нашего приложения
app.minsize(width = WIDTH,height = HEIGHT)
app.maxsize(width = WIDTH,height = HEIGHT)

text = tkinter.Text(app, width = WIDTH - 100, height = HEIGHT, wrap = 'word' ) #ввод текста(размеры, wrap - обертка для написания слов)
scroll = Scrollbar(app, orient=VERTICAL, command=text.yview) #создание скроллбара (ориентир вертикальный, перемещает текст по оси y)
scroll.pack(side='right',fill='y') #размещаем скролл в приложении(справа, двигается по y)
text.configure(yscrollcommand=scroll.set) #привязка скролла к тексту
text.pack() #размещаем текст

menuBar = tkinter.Menu(app) #создаем меню

editor = Text_editor()

app_menu = tkinter.Menu(menuBar) #выпадающее меню у "Файл"
app_menu.add_command(label='Новый', command=editor.new_file)
app_menu.add_command(label='Открыть', command=editor.open_file)
app_menu.add_command(label='Сохранить', command=editor.save_file)
app_menu.add_command(label='Сохранить как', command=editor.save_as_file)



menuBar.add_cascade(label ='Файл', menu=app_menu)
menuBar.add_cascade(label ='Справка', command=editor.get_info)
menuBar.add_cascade(label ='Правка')
menuBar.add_cascade(label ='Выход', command=app.quit)

app.config(menu=menuBar)

app.mainloop() #бесконечный циклы while True: