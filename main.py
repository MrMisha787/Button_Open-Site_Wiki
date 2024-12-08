import webbrowser
from http.client import responses
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Button

import requests
from bs4 import BeautifulSoup

# главное окно приложения
window= Tk()# заголовок окна
window.title('Авторизация')# размер окна
window.geometry('900x1000')# можно ли изменять размер окна - нет
window.resizable(False, False)

# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}
remember_var = BooleanVar()
selected_option = StringVar(value='Выберете вариант')

# обработчик нажатия на клавишу 'Войти'
def clicked():    # получаем имя пользователя и пароль
    username = username_entry.get()
    password = password_entry.get()
    remember_me = remember_var.get()
    phone = phone_entry.get()
    option_men = selected_option.get()
    # выводим в диалоговое окно введенные пользователем данные
    messagebox.showinfo('Заголовок',f'Имя: {username},пароль: {password},Телефон: {phone} , {option_men}, Запомнить меня: {remember_me}')



# функция для открытия нового окна после успешной авторизации
def open_new_window():
    new_window = Toplevel (window) # создаем новое окно
    new_window. title("Главное Окно") # заголовок нового окна
    new_window. geometry("300x150") # размер нового окна

    # Добавим текст в новое окно
    label = Label (new_window, text="Добро пожаловать!", font=font_header)
    label. pack(pady=20)

    # Кнопка для закрытия нового окна
    close_btn = Button(new_window, text="Закрыть", command=new_window.destroy)
    close_btn.pack(pady=10)



# для всех остальных виджетов настройки делаются также
main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
# помещаем виджет в окно по принципу один виджет под другим
main_label.pack()



# метка для поля ввода имени
username_label = Label(window, text='Имя пользователя', font=label_font , **base_padding)
username_label.pack()
# поле ввода имени
username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()



# метка для поля ввода пароля
password_label = Label(window, text='Пароль', font=label_font , **base_padding)
password_label.pack()
# поле ввода пароля
password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry, show="*")
password_entry.pack()



# метка для поля ввода телефона
password_label = Label(window, text='Телефон', font=label_font , **base_padding)
password_label.pack()
# поле ввода телефона
phone_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
phone_entry.pack()



# чекбокс 'Запомнить меня'
remember_me_checkbox= Checkbutton(window, text='Запомнить меня', variable=remember_var, font=label_font)
remember_me_checkbox.pack(**base_padding)



# метка для выбора варианта
option_label = Label(window, text = 'Чем есть МЯСО?', font=label_font, **base_padding)
option_label.pack()
# список вариантов для выбора
options = ['Вилка','Ложка','Нож']
option_menu = OptionMenu(window, selected_option, *options)
option_menu.pack(**base_padding)



# кнопка отправки формы
send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)



# функция для увилечения размера шрифта
def increase_font_size():
    global font_header, font_entry, label_font
    #увеличение размера шрифта на 2
    font_header = ('Arial', font_header[1] + 2)
    font_entry = ('Arial', font_entry[1] + 2)
    label_font = ('Arial', label_font[1] + 2)
    # обнавляем текстовые элементы интерфейса
    main_label.config(font=font_header)
    username_entry.config(font=label_font)
    password_entry.config(font=label_font)
    phone_entry.config(font=label_font)
    remember_me_checkbox.config(font=label_font)
    option_label.config(font=label_font)
    option_menu.config(font=font_entry)
    send_btn.config(font=label_font)
gb_button = Button (window, text='Смена размера', command=increase_font_size)
gb_button.pack(**base_padding)



# функция для загрузки изображения
class ImageTk:
    pass


def load_image():
    fila_path = filedialog.askopenfilename(title='Выберите изображение',
                                           filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if fila_path:
        # Загружаем изображение с помощью Pillow
        img = Image.open(fila_path)
        img.thumbnail((150, 150)) # Изменяем размер изображение
        img_tk = ImageTk.PhotoImage(img)

        # отображаем изображение в метке
        image_label.config(image=img_tk)
        image_label.image = img_tk # сохроняем ссылку на изображение



# кнопка для загрузки изображений
load_image_btn = Button(window, text='Загрузить фото/изображение', command=load_image)
load_image_btn.pack(**base_padding)
# метка для отображения изображения
image_label = Label(window)
image_label.pack(pady=(10, 0))



# функция для открытия веб-сайта
def open_website():
    webbrowser.open("https://ru.wikipedia.org")



# функция для парсинга данных с веб-сайта
def parse_website():
    url = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0" # замените на нужный вам URL

    response = requests.get(url) #  выполняем GET-запрос к сайту

    if response.status_code == 200: # проверяем статус ответа
        soup = BeautifulSoup(response.text, 'html.parser') # парсим HTML-код страницы

        # Пример: извлекаем все заголовки h1 на странице

        headers = soup.find_all('title')

        for header in headers:
            print(header.text) # выводим заголовки в конслоль



# кнопка для открытия веб-сайта
website_btn = Button(window, text='открытие web-site', command=open_website)
website_btn.pack(**base_padding)




# кнопка для парсинга сайта
parse_btn = Button(window, text='Парсить сайт', command=parse_website)
parse_btn.pack(**base_padding)



window.mainloop()
