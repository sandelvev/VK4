from tkinter import *
import webbrowser
import os

#===================== ГЛАВНОЕ ОКНО ======================
root = Tk()
root.title("VK")
root.geometry("900x700")
root.resizable(width=True, height=True)
root.configure(bg="#EEEEEE")

#========================= ШАПКА =========================

#Внешняя граница шапки
border = Frame(root, bg="#42996e", padx=2, pady=2)
border.pack(fill="x", side="top")

#Внутренняя граница шапки
inner = Frame(border, bg="#eafff0", height=60)
inner.pack(fill="both", expand=True)
inner.pack_propagate(False)

#Логотип
logo_img = PhotoImage(file = "logo.png")
logo_label = Label(root, bg="#eafff0")
logo_label.image = logo_img
logo_label['image'] = logo_label.image
logo_label.place(x=8, y=5)

#Текст "ВКОНТАКТЕ"
title_label = Label(text="вконтакте", bg="#eafff0", font=("Arial", 23, "bold"))
title_label.place(x=55, y=8)

#Поле поиска
search_entry = Entry(inner, font=("Arial", 12), fg='#555555', bg='#EEEEEE', bd=0, highlightthickness=0)
search_entry.insert(0, "🔍 ПОИСК")

def update_search_position(event=None):
    # Отступ слева: 250 пикселей от левого края
    # Ширина: 30% от ширины шапки или минимум 200 пикселей
    width = max(250, inner.winfo_width() // 5)
    search_entry.place(x=230, y=11, width=width, height=40)

# Устанавливаем начальное положение
inner.update_idletasks()
update_search_position()

# Обновляем позицию при изменении размера окна
root.bind("<Configure>", update_search_position)

def on_focus_in(event):
    if search_entry.get() == "🔍 ПОИСК":
        search_entry.delete(0, END)
        search_entry.config(fg='black')

def on_focus_out(event):
    if search_entry.get() == "":
        search_entry.insert(0, "🔍 ПОИСК")
        search_entry.config(fg='#555555')

search_entry.bind("<FocusIn>", on_focus_in)
search_entry.bind("<FocusOut>", on_focus_out)

#Кнопка уведомлений

bell_img = PhotoImage(file = "bell.png")
bell_img = bell_img.subsample(4, 4)

def on_bell_img_click():
    print("Уведомления")

bell_btn = Button(inner, image=bell_img, bg="#eafff0", activebackground="#eafff0", borderwidth=0,  highlightthickness=0, cursor="hand2", command=on_bell_img_click )
bell_btn.image = bell_img  # обязательно сохранить ссылку на изображение
bell_btn.place(relx=1.0, x=-15, y=15, anchor="ne")

#Кнопка профиля (справа в шапке)

profile_img = PhotoImage(file = "Stathem.png")
profile_btn = Button(root, text="ПРОФИЛЬ  ", image=profile_img, compound="right", font=("Arial", 13), bg="#eafff0", bd=0, highlightthickness=0, relief="flat", fg="#000000", activebackground="#eafff0", cursor="hand2")
profile_btn.image = profile_img
profile_btn.place(relx=1.0, x=-65, y=5, anchor="ne")

#==================== БОКОВАЯ ПАНЕЛЬ =========================

#ПРОФИЛЬ
user_profile = PhotoImage(file = "user_profile.png")
user_btn = Button(root, text="ПРОФИЛЬ", image=user_profile, compound="left", font=("Arial", 13), bg="#EEEEEE", fg="#333333", bd=0, padx=8, pady=3, activebackground="#c9c9c9", cursor="hand2")
user_btn.image = user_profile
user_btn.place(x=10, y=80)

#ЛЕНТА
news = PhotoImage(file = "news.png")
news = news.subsample(4, 4)
news_btn = Button(root, text="ЛЕНТА", image=news, compound="left", font=("Arial", 13), bg="#EEEEEE", fg="#333333", bd=0, padx=8, pady=3, activebackground="#c9c9c9", cursor="hand2")
news_btn.image = news
news_btn.place(x=10, y=115)

#ДРУЗЬЯ
users = PhotoImage(file = "users.png")
users = users.subsample(2, 2)
users_btn = Button(root, text="ДРУЗЬЯ", image=users, compound="left", font=("Arial", 13), bg="#EEEEEE", fg="#333333", bd=0, padx=8, pady=3, activebackground="#c9c9c9", cursor="hand2")
users_btn.image = users
users_btn.place(x=10, y=150)

#МЕССЕНДЖЕР
chats = PhotoImage(file = "chats.png")
chats = chats.subsample(4, 4)
chats_btn = Button(root, text="МЕССЕНДЖЕР", image=chats, compound="left", font=("Arial", 13), bg="#EEEEEE", fg="#333333", bd=0, padx=8, pady=3, activebackground="#c9c9c9", cursor="hand2")
chats_btn.image = chats
chats_btn.place(x=10, y=185)

#Ссылки внизу
def on_enter(event):
    event.widget.config(fg="#2B2B2B") #Цвет при наведении на ссылку

def on_leave(event):
    event.widget.config(fg="#555555") #Исходный цвет ссылки
    
link = Label(root, text="Блог, Разработчикам,\nДля бизнеса, Авторам,\nДействия, Ещё", fg="#555555", bg="#EEEEEE", font=("Arial", 9, "underline"), cursor="hand2", anchor="w", justify="left")
link.pack(pady=30)

link.bind("<Enter>", on_enter)
link.bind("<Leave>", on_leave)
link.place(x=14, y=230)

link2 = Label(root, text="Применяются\nрекомендательные технологии", fg="#555555", bg="#EEEEEE", font=("Arial", 9, "underline"), cursor="hand2", anchor="w", justify="left")
link2.pack(pady=30)

link2.bind("<Enter>", on_enter)
link2.bind("<Leave>", on_leave)
link2.place(x=14, y=310)


#====================== ЦЕНТРАЛЬНЫЙ КОНТЕНТ ========================

#Синее поле "ЛЕНТА НОВОСТЕЙ"
blue_bar = Canvas(root, bg="#2d76a6", highlightthickness=0)
blue_bar.place(relx=0.5, y=100, relwidth=0.51, relheight=0.065, anchor="center")

#фон и текст
rect_id = blue_bar.create_rectangle(0, 0, 0, 0, fill="#1976d2", outline="")
text_id = blue_bar.create_text(0, 0, text="ЛЕНТА НОВОСТЕЙ", fill="white", font=("Arial", 14, "bold"))

def resize_rect(event):
    # Обновляем размер фона (если нужно)
    blue_bar.coords(rect_id, 0, 0, event.width, event.height)
    # Центрируем текст
    blue_bar.coords(text_id, event.width // 2, event.height // 2)

blue_bar.bind("<Configure>", resize_rect)

# Белый контент-фрейм под синим заголовком
white_frame = Frame(root, bg="white", highlightbackground="#cccccc", highlightthickness=0)
white_frame.place(relx=0.5, rely=0.183, relwidth=0.51, relheight=0.90, anchor="n")

#Пост внутри контента
post_frame = Frame(white_frame, bg="#f5f5f5", padx=15, pady=15)
post_frame.pack(fill="x", padx=20, pady=10)

#=================== РЕКЛАМНЫЕ БЛОКИ (СПРАВА) ======================

#Изображение 1
pic1 = PhotoImage(file = "pic1.png")
pic1_btn = Label(root, image=pic1, bg="#EEEEEE", cursor="hand2")
pic1_btn.image = pic1

def open_link(event):
    webbrowser.open("https://www.bedhead.com/")
    
pic1_btn.bind("<Button-1>", open_link)
pic1_btn.place(relx=0.98, rely = 0.12, anchor="ne")

#Изображение 2
pic2 = PhotoImage(file = "pic2.png")
pic2_btn = Label(root, image=pic2, bg="#EEEEEE", cursor="hand2")
pic2_btn.image = pic2

def open_link(event):
    webbrowser.open("https://ru.wikipedia.org/wiki/%D0%A5%D1%83%D0%BB%D0%B8%D0%B3%D0%B0%D0%BD_(%D0%B6%D1%83%D1%80%D0%BD%D0%B0%D0%BB)?ysclid=mlgh5wqvjg272145097")
    
pic2_btn.bind("<Button-1>", open_link)
pic2_btn.place(relx=0.98, rely = 0.55, anchor="ne")

#======================== ЗАПУСК ПРИЛОЖЕНИЯ ============================

root.mainloop()
