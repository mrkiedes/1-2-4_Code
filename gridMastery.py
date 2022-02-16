import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

frame1 = tk.Frame(window, width=200, height=200, background="Purple")
frame1.grid(row= 0, column=0)

frame2 = tk.Frame(window, width=200, height=200, background="Pink")
frame2.grid(row= 1, column=0)

frame3 = tk.Frame(window, width=200, height=200, background="Red")
frame3.grid(row= 0, column=1)

frame4 = tk.Frame(window, width=200, height=200, background="Yellow")
frame4.grid(row= 1, column=1)

window.mainloop()