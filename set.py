import tkinter
from tkinter import*
from tkinter.filedialog import askopenfile, asksaveasfile #функции сохранить как  и открыть как файл
from tkinter.messagebox import showerror #показ всех ошибок
from tkinter import messagebox #уведомления приложения

from settings import* #импортируем настройки

app = tkinter.Tk() #создаю окно приложения
app.title(APP_NAME) #указываем название нашего приложения
app.minsize(width = WIDTH,height = HEIGHT)
app.maxsize(width = WIDTH,height = HEIGHT)

text = tkinter.Text(app, width = WIDTH - 100, height = HEIGHT, wrap = 'word' ) #ввод текста(размеры, wrap - обертка для написания слов)
class Text_editor():
    def __init__(self):
        self.file_name = tkinter.NONE
    
    def new_file(self):
        self.file_name = 'Без названия'
        text.delete('1.0', tkinter.END)

    def open_file(self):
        inp = askopenfile(mode="r", filetypes =[('txt File', '*.py')])
        if inp is None:
            return
        data = inp.read()
        text.delete('1.0', tkinter.END)
        text.insert('1.0', data)


    def save_file(self):
        data = text.get('1.0', tkinter.END)
        output = open(self.file_name, 'w', encoding='utf-8')
        output.write(data)
        output.close()

    def save_as_file(self):
        output = asksaveasfile(mode='w', defaultextension='txt') #выводим окно
        data = text.get('1.0', tkinter.END) #считываем все, что есть в поле 
        try:
            output.write(data.rstrip()) #если поле пустое
        except Exception:
            showerror(title='Ошибка!', message='Ошибка при сохранении файла')

    def get_info(self):
        messagebox.showinfo('Справка', 'Информация о нашем приложении! Спасибо, что его используете:)')