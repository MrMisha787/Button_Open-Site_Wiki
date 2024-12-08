import webbrowser
from tkinter import *
from tkinter.ttk import Button

window= Tk()
window.title('Open Wiki')
window.geometry('500x330')
window.resizable(True, True)

font_header = ('Arial', 23)
font_entry = ('Arial', 23)
label_font = ('Arial', 23)
base_padding = {'padx': 23, 'pady':23}
header_padding = {'padx': 23, 'pady': 23}
remember_var = BooleanVar()

main_label = Label(window, text='Web-site Open', font=font_header, justify=CENTER, **header_padding)
main_label.pack()
def open_website():
    webbrowser.open("https://ru.wikipedia.org")
website_btn = Button(window, text='open web-site(wiki)', command=open_website)
website_btn.pack(**base_padding)

window.mainloop()