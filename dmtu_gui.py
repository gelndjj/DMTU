import tkinter as tk, os
from tkinter import filedialog, messagebox, ttk, END
from datetime import datetime
import customtkinter as ck
from cryptography.fernet import Fernet, InvalidToken
from PIL import ImageTk, Image

# ~~~CODE~~~ #

def encrypt_folder_10():
    src_folder = filedialog.askdirectory(title="Select Folder")
    if src_folder:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        encrypt_file = os.getcwd() + "/" + timestamp + "_10.txt"
        original_path = os.getcwd() + "/" + timestamp + "_10p.txt"

        key = Fernet.generate_key()
        fernet = Fernet(key)

        with open(os.getcwd() + "/" + timestamp + "_10.mu", 'wb') as thekeyE:
            thekeyE.write(key)

        for root, dirs, files in os.walk(src_folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if file_size <= 10485760:
                    with open(file_path, 'rb') as file:
                        file_data = file.read()

                    encrypted_data = fernet.encrypt(file_data)

                    with open(file_path, 'wb') as f:
                        f.write(encrypted_data)

        with open(encrypt_file, 'wb') as t:
            t.write(encrypted_data)

        with open(original_path, 'w') as fp:
            fp.write(f"{src_folder}")

        messagebox.showinfo('Success', 'Files 10MB size have been encrypted successfully')
    else:
        messagebox.showinfo('Aborted', 'Operation Aborted')

def encrypt_folder_50():
    src_folder = filedialog.askdirectory(title="Select Folder")
    if src_folder:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        encrypt_file = os.getcwd() + "/" + timestamp + "_50.txt"
        original_path = os.getcwd() + "/" + timestamp + "_50p.txt"

        key = Fernet.generate_key()
        fernet = Fernet(key)

        with open(os.getcwd() + "/" + timestamp + "_50.mu", 'wb') as thekeyE:
            thekeyE.write(key)

        for root, dirs, files in os.walk(src_folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if file_size <= 52428800:
                    with open(file_path, 'rb') as file:
                        file_data = file.read()

                    encrypted_data = fernet.encrypt(file_data)

                    with open(file_path, 'wb') as f:
                        f.write(encrypted_data)

        with open(encrypt_file, 'wb') as t:
            t.write(encrypted_data)

        with open(original_path, 'w') as fp:
            fp.write(f"{src_folder}")

        messagebox.showinfo('Success', 'Files 50MB size have been encrypted successfully')
    else:
        messagebox.showinfo('Aborted', 'Operation Aborted')
def encrypt_folder():
    src_folder = filedialog.askdirectory(title="Select Folder")
    if src_folder:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        encrypt_file = os.getcwd() + "/" + timestamp + ".txt"
        original_path = os.getcwd() + "/" + timestamp + "p.txt"

        key = Fernet.generate_key()
        fernet = Fernet(key)

        with open(os.getcwd() + "/" + timestamp + ".mu", 'wb') as thekeyE:
            thekeyE.write(key)

        for root, dirs, files in os.walk(src_folder):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as file:
                    file_data = file.read()

                encrypted_data = fernet.encrypt(file_data)

                with open(file_path, 'wb') as f:
                    f.write(encrypted_data)

        with open(encrypt_file, 'wb') as t:
            t.write(encrypted_data)

        with open(original_path, 'w') as fp:
            fp.write(f"{src_folder}")

        messagebox.showinfo('Success', 'Files have been encrypted successfully')
    else:
        messagebox.showinfo('Aborted', 'Operation Aborted')

def encrypt_files():
    src_folder = filedialog.askopenfilenames(title="Select File(s)")
    if src_folder:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        encrypt_file = os.getcwd() + "/" + timestamp + "_f.txt"
        original_path = os.getcwd() + "/" + timestamp + "_fp.txt"

        key = Fernet.generate_key()
        fernet = Fernet(key)

        with open(os.getcwd() + "/" + timestamp + "_f.mu", 'wb') as thekeyE:
            thekeyE.write(key)

        for file in src_folder:
            with open(file, 'rb') as f:
                file_data = f.read()

            encrypted_data = fernet.encrypt(file_data)

            with open(file, 'wb') as f:
                f.write(encrypted_data)

        with open(encrypt_file, 'wb') as t:
            t.write(encrypted_data)

        with open(original_path, 'w') as fp:
            fp.write(f"{src_folder}")

        messagebox.showinfo('Success', 'Selected files have been encrypted successfully')
    else:
        messagebox.showinfo('Aborted', 'Operation Aborted')

def decrypt_files():
    folder_path = textbox2.get()
    index = combo.current()
    paths = [os.path.join(os.getcwd() + '/', item) for item in combo['values']]
    key_path = paths[index]

    with open(key_path, "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as enc_file:
                    encrypted = enc_file.read()
                decrypted_password = f.decrypt(encrypted)
                with open(file_path, "wb") as dec_file:
                    dec_file.write(decrypted_password)

            except InvalidToken:
                pass

    messagebox.showinfo('Success', 'All encrypted files have been decrypted successfully')
def location(event):
    directory_path = filedialog.askdirectory()
    if directory_path:
        textbox2.delete(0, tk.END)
        textbox2.insert(0, directory_path)
        textbox2.selection_clear()
    else:
        messagebox.showinfo('Aborted', 'Operation Aborted')

def update_canvas():
    filename = images[current_image]
    image = tk.PhotoImage(file=filename)
    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    canvas.image = image

def change_image(event):
    global current_image
    current_image = (current_image + 1) % len(images)
    update_canvas()

def main_file_list(event):
    dir_path = os.getcwd()
    file_list = os.listdir(dir_path)
    combo['values'] = []
    for file_name in file_list:
        if file_name.endswith('.mu'):
            combo['values'] = (*combo['values'], file_name)

def show_path(event):
    file_name = combo.get()[:-3] + "p.txt"
    with open(file_name, "r") as f:
        first_line = f.readline()
        textbox2.delete(0, 'end')
        textbox2.insert(0, first_line)

def del_entries(event):
    combo.set("Select Secret Key")
    textbox2.delete(0, 'end')
    textbox2.insert(0, '')
    textbox.delete(0, 'end')
    textbox.insert(0, 'Select Another Location')

# ~~~GUI~~~ #
window = tk.Tk()
window.title('DMTU')
width = 480
height = 800
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/4) - (height/4)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(0, 0)

frame = tk.Frame(window, width=480, height=800, borderwidth=0, highlightthickness=0)
frame.pack()
image = Image.open("img_soft/main.png")
img = ImageTk.PhotoImage(image)

canvas = tk.Canvas(frame, width=480, height=800, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=img)

image2 = Image.open("img_soft/ban.png")
img2 = ImageTk.PhotoImage(image2)

banner = tk.Canvas(frame, width=480, height=100, highlightthickness=0)
banner.place(x=0, y=-20)
banner.create_image(0, 0, anchor=tk.NW, image=img2)

menu = tk.Canvas(frame, width=240, height=225, highlightthickness=0)
menu.create_rectangle(0, 0, 240, 225, outline="black", width=7)
menu.configure(background='#191d12')
menu.create_text(135, 35, text="Encrypt anything inside a folder\nand its content", fill="red")
menu.create_text(130, 88, text="Encrypt anything smaller than\n50MB size inside a folder\nand its content", fill="red")
menu.create_text(130, 147, text="Encrypt anything smaller than\n10MB size inside a folder\nand its content", fill="red")
menu.create_text(121, 195, text="Encrypt only selected files", fill="red")
menu.place(x=10, y=150)

menu2 = tk.Canvas(frame, width=205, height=152, highlightthickness=0)
menu2.create_rectangle(0, 0, 205, 152, outline="black", width=7)
menu2.configure(background='#191d12')
menu2.place(x=260, y=150)

menu2.create_text(70, 25, text="Free Files", fill="red")

mush_up_img = ck.CTkImage(light_image=Image.open("img_soft/Mushroom1up.png"), size=(16, 16))
mario_img = ck.CTkImage(light_image=Image.open("img_soft/Mario.png"), size=(16, 16))
mush_img = ck.CTkImage(light_image=Image.open("img_soft/Mushroom.png"), size=(16, 16))
coin_img = ck.CTkImage(light_image=Image.open("img_soft/Coin.PNG"), size=(16, 16))
fire_img = ck.CTkImage(light_image=Image.open("img_soft/Fire.png"), size=(16, 16))

btn_mush1up = ck.CTkButton(canvas, text="", width=1, height=1, image=mush_up_img, fg_color="#191d12", hover_color="white", bg_color="#202717", border_width=1, border_color='#87b23f', command=decrypt_files)
btn_mush1up.place(x=388, y=581)
btn_mario = ck.CTkButton(canvas, text="", width=1, height=1, image=mario_img, fg_color="#191d12", hover_color="white" ,bg_color="#202717", border_width=1, border_color='#87b23f', command=encrypt_folder)
btn_mario.place(x=340, y=581)
btn_mush = ck.CTkButton(canvas, text="", width=1, height=1, image=mush_img, fg_color="#191d12", hover_color="white" ,bg_color="#202717", border_width=1, border_color='#87b23f', command=encrypt_folder_50)
btn_mush.place(x=340, y=628)
btn_coin = ck.CTkButton(canvas, text="", width=1, height=1, image=coin_img, fg_color="#191d12", hover_color="white" ,bg_color="#202717", border_width=1, border_color='#87b23f', command=encrypt_folder_10)
btn_coin.place(x=340, y=677)
btn_fire = ck.CTkButton(canvas, text="", width=1, height=1, image=fire_img, fg_color="#191d12", hover_color="white" ,bg_color="#202717", border_width=1, border_color='#87b23f', command=encrypt_files)
btn_fire.place(x=388, y=677)

btn_m_mario = ck.CTkButton(menu, text="", width=1, height=1,  image=mario_img, compound='left', fg_color="#191d12", hover_color="#191d12")
btn_m_mario.place(x=10, y=10)
btn_m_mush = ck.CTkButton(menu, text="", width=1, height=1,  image=mush_img, compound='left', fg_color="#191d12", hover_color="#191d12")
btn_m_mush.place(x=10, y=55)
btn_m_coin = ck.CTkButton(menu, text="", width=1, height=1,  image=coin_img, compound='left', fg_color="#191d12", hover_color="#191d12")
btn_m_coin.place(x=10, y=115)
btn_m_mush1up = ck.CTkButton(menu2, text="", width=1, height=1,  image=mush_up_img, compound='left', fg_color="#191d12", hover_color="#191d12")
btn_m_mush1up.place(x=10, y=10)
btn_m_fire = ck.CTkButton(menu, text="", width=1, height=1,  image=fire_img, compound='left', fg_color="#191d12", hover_color="#191d12")
btn_m_fire.place(x=10, y=176)

images = ["img_soft/main.png",
          "img_soft/main_night.png",
          "img_soft/main_grey.png",
          "img_soft/main_cosmic.png",
          "img_soft/main_chroma.png"]
current_image = 0

style = ttk.Style()
style.theme_use('clam')
style.configure('TCombobox', bordercolor='white', lightcolor='white')

combo = ttk.Combobox(menu2, style='TCombobox', width=18)
combo.set("Select Secret Key")
combo.place(x=103, y=55,  anchor=tk.CENTER)
textbox2 = tk.Entry(menu2, highlightbackground='#191d12', width=19)
textbox2.insert(0,"")
textbox2.place(x=103, y=90, anchor=tk.CENTER)
textbox = tk.Entry(menu2, highlightbackground='#191d12', width=19, highlightcolor='yellow')
textbox.insert(0,"Select Another Location")
textbox.place(x=12, y=111)

# ~~~GUI~~~ #
update_canvas()
window.bind('<Control-t>', change_image)
window.bind('<Control-Return>', del_entries)
window.bind("<Button-1>", lambda event: window.focus_set())
combo.bind("<Button-1>", main_file_list)
combo.bind("<<ComboboxSelected>>", show_path)
textbox.bind("<Button-1>", lambda event: location)
textbox.bind("<FocusIn>", location)

window.mainloop()