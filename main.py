#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_my_button():
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_auth.config(text=password)

# main window
root = tk.Tk()
root.title('Authorization')
root.wm_geometry("200x150")

frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky='news')

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)



ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)

btn_login = tk.Button(frame_login, text='Login', command=test_my_button)
btn_login.pack()


frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky='news')

lbl_auth = tk.Label(frame_auth, text='Temp')
lbl_auth.pack()

frame_login.tkraise()

root.mainloop()