import pyautogui
import time
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cv2
import pymongo
import numpy as np
import platform
import hashlib
# from pynput.keyboard import Listener, KeyCode
# # // lupoongf
# from threading import Thread
from threading import Thread
import threading




# // get id
def get_computer_id():
    machine = platform.machine()
    node = platform.node()
    processor = platform.processor()

    computer_id = machine + node + processor
    computer_id_hash = hashlib.sha256(computer_id.encode()).hexdigest()
    # print(' 250936eb5a536a41862031cca327524de93e51e5d39a75d66c59e6d5c546dd70')
    return(computer_id_hash)


def nolan_click(x,y):
    pyautogui.click(x, y, clicks=1, interval=0, button='left')
def nolan_img(tmp):
    global check_btn
    # target_image = Image.open(tmp)
    # print('okkk')
    # while True:
    #     screenshot = pyautogui.screenshot("nolannn.PNG")
    #     if pyautogui.locate(target_image, screenshot, grayscale=True) is not None:
    #         position = pyautogui.locateCenterOnScreen(target_image, grayscale=True)
    #         pyautogui.click(position)
    #         print('yyyy')
    #     time.sleep(0.5)

    image = cv2.imread(tmp, 0)
    threshold = 0.9
    while(True):
        if (check_btn== False):
            return
        threshold-=0.05
        screen = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screen, image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val > threshold:
            x, y = max_loc
            w, h = image.shape[::-1]
            # print("Image found at: ", x, y)
            # print(tmp)
            nolan_click(x+w/2,y+h/2)
            break
        # else:
            #print("Image not found.")
        time.sleep(0.5)
        if(threshold<0.4): break












def select_choice(value):
    messagebox.showinfo("Selected choice:", value)

def help_clicked():
    messagebox.showinfo("Help button clicked")


def login_clicked():
    messagebox.showinfo("server chậm", "đồ chùa nên hơi kùi ae thông cảm\n liên hệ snolan: trongsonne(fb)\n 0349749854(zalo)")
    username = username_entry.get()
    password = password_entry.get()
    # print("Username:", username)
    # print("Password:", password)

    # print(get_computer_id()=='250936eb5a536a41862031cca327524de93e51e5d39a75d66c59e6d5c546dd70')
    myclient = pymongo.MongoClient("mongodb+srv://ntson:Trongson2000@cluster0.mxtmb9h.mongodb.net")
    mydb = myclient["nolan_1647"]
    mycol = mydb["acc"]

    x = mycol.find_one({"uid":username,"pass":password})
    # sai pass
    if x==None:
        messagebox.showinfo("Đăng nhập không thành công" , "tài khoản hoặc mật khẩu không chính xác\n liên hệ nolan ")
        return
    # check id pc
    pc_id = x['pc_id']
    # print(pc_id)
    # acc mới thì cập nhật idpc
    if pc_id =='nolan':
        messagebox.showinfo("login thành công", "đây là lần đầu bạn login\n hãy lick vào button help để được hướng dẫn nhé\n liên hệ nolan nếu lỗi")
        pc_id=get_computer_id()
        myquery = {"uid":username,"pass":password}
        newvalues = {"$set": {"uid":username,"pass":password,"pc_id":pc_id}}
        mycol.update_one(myquery, newvalues)
    # nếu sai idpc
    if pc_id!=get_computer_id():
        messagebox.showinfo('không copy', "mỗi acc chỉ log trên 1 máy duy nhất\n liên hệ nolan để được hỗ trợ")
        return
    login_frame.pack_forget()
    main_frame.pack()


check_btn= True
check_exit= True
arr_glb=[]


def luc_clicked():
    global check_btn,arr_glb
    check_btn = True
    arr_glb = ['search', 'army', 'search_btn', 'army_pick', select_var.get(), 'quick', 'done_att']
    messagebox.showinfo("Title", "This is a message box.")
    thread_start = threading.Thread(target=start_search, args=())

    thread_start.start()


def thuy_clicked():
    global check_btn,arr_glb
    check_btn = True
    # print("Thuy button clicked")
    arr_glb = ['search', 'navy', 'search_btn', 'navy_pick', select_var.get(), 'quick', 'done_att']
    thread_start = threading.Thread(target=start_search, args=())

    thread_start.start()

def air_clicked():
    # print("Thuy button clicked")
    global check_btn,arr_glb
    check_btn=True
    arr_glb = ['search', 'air', 'search_btn', 'air_pick', select_var.get(), 'quick', 'done_att']
    thread_start = threading.Thread(target=start_search, args=())

    thread_start.start()

def start_search():
    global check_btn,arr_glb
    so_dao = int(so_dao_var.get()) + 1
    a = int(time_sleep_var.get())
    while(True):
        if (check_btn== False):
            # print("2222222222222222")
            # running_threads = threading.enumerate()
            # for thread in running_threads:
                # print(thread.getName())
            break
        else:
            for i in range(1, so_dao):
                for element in arr_glb:
                    str_tmp = element + '.PNG'
                    nolan_img(str_tmp)
                    # print(str_tmp)
                    time.sleep(0.8)
                # print(i)
            time.sleep(a)
    return

def bua_clicked():
    messagebox.showinfo("note","Bua button clicked")


def tap_ket_terro_clicked():
    messagebox.showinfo("note","Tap ket terro button clicked")
    
def cong_terro_clicked():
    messagebox.showinfo("note","Tap ket terro button clicked")

def donate_clicked():
    messagebox.showinfo("note","Donate button clicked")

def stop_clicked():

    messagebox.showinfo("tạm dừng", "dừng chương trình")
    thread_stop = threading.Thread(target=stop_clickedd, args=())
    thread_stop.start()
    # print("Donate button clicked")
def stop_clickedd():
    global check_btn
    check_btn=False
    # print("stopp")
    return


# giao dieenj
root = tk.Tk()
root.title("nolan_1647")

# Login frame
login_frame = ttk.Frame(root)
login_frame.pack(pady=5)
login_frame.pack(padx=7)

# user 
username_frame = ttk.Frame(login_frame)
username_frame.pack(pady=5)
username_var = tk.StringVar()
username_var.set("Enter your username")
username_entry = ttk.Entry(username_frame, textvariable=username_var)
username_entry.pack(side="left")
def clear_username(*args):
    username_var.set("")
username_entry.bind("<FocusIn>", clear_username)

# pass 
password_frame = ttk.Frame(login_frame)
password_frame.pack(pady=5)
password_var = tk.StringVar()
password_var.set("Enter your password")
password_entry = ttk.Entry(password_frame, textvariable=password_var)
password_entry.pack(side="left")
def clear_password(*args):
    password_var.set("")
password_entry.bind("<FocusIn>", clear_password)

#  button
button_frame = ttk.Frame(login_frame)
button_frame.pack(pady=5)
login_button = ttk.Button(button_frame, text="Login", command=login_clicked)
login_button.pack(side="left", padx=5)
help_button = ttk.Button(button_frame, text="Help", command=help_clicked)
help_button.pack(side="left", padx=5)

# Main frame
main_frame = ttk.Frame(root)

# Select box
select_frame = ttk.Frame(main_frame)
select_frame.pack(pady=5)
select_var = tk.StringVar()
select_var.set("x1")
select_box = ttk.Combobox(select_frame, textvariable=select_var, values=["x1", "x5"], state="readonly")
select_box.pack(side="left",pady=5)
# so dao

so_dao_var = tk.StringVar()
so_dao_var.set("số đạo")
so_dao_entry = ttk.Entry(select_frame, textvariable=so_dao_var)
so_dao_entry.pack(side="left",pady=5)

# time_sleep
time_sleep_var = tk.StringVar()
time_sleep_var.set("thời gian chờ")
time_sleep_entry = ttk.Entry(select_frame, textvariable=time_sleep_var)
time_sleep_entry.pack(side="left",pady=5)
def clear_time_sleep(*args):
    time_sleep_var.set("")
time_sleep_entry.bind("<FocusIn>", clear_time_sleep)
# //clear so dao
def clear_so_dao(*args):
    so_dao_var.set("")
so_dao_entry.bind("<FocusIn>", clear_so_dao)

# First row of buttons
first_row_frame = ttk.Frame(main_frame)
first_row_frame.pack(pady=5)

luc_button = ttk.Button(first_row_frame, text="army", command=luc_clicked)
luc_button.pack(side="left", padx=5)

thuy_button = ttk.Button(first_row_frame, text="navy", command=thuy_clicked)
thuy_button.pack(side="left", padx=5)

air_button = ttk.Button(first_row_frame, text="Air", command=air_clicked)
air_button.pack(side="left", padx=5)

# Second row of buttons
second_row_frame = ttk.Frame(main_frame)
second_row_frame.pack(pady=5)

bua_button = ttk.Button(second_row_frame, text="Bua", command=bua_clicked)
bua_button.pack(side="left", padx=5)

tap_ket_terro_button = ttk.Button(second_row_frame, text="Tap ket terro", command=tap_ket_terro_clicked)
tap_ket_terro_button.pack(side="left", padx=5)

cong_terro_button = ttk.Button(second_row_frame, text="Cong terro", command=cong_terro_clicked)
cong_terro_button.pack(side="left", padx=5)
# Donate button
hehe_frame = ttk.Frame(main_frame)
hehe_frame.pack(pady=5)

donate_button = ttk.Button(hehe_frame, text="Donate", command=donate_clicked)
donate_button.pack(side="left", padx=5)

stop_button = ttk.Button(hehe_frame, text="stop",command=stop_clicked)
stop_button.pack(side="left", padx=5)

help_button = ttk.Button(hehe_frame, text="Help", command=help_clicked)
help_button.pack(side="left", padx=5)
root.mainloop()
