import tkinter as tk

def create():
    number = int(input_number.get())
    if number == 0:
        return time_table.configure(text='ยังไงก็ได้ 0')
    
    show_off = ''
    for item in range(1, 13):
        show_off += str(number) + ' x ' + str(item) + ' = ' + str(number * item) +'\n'

    time_table.configure(text=show_off)


    
window = tk.Tk()
window.title('สูตรคูณ')
window.minsize(width=400, height=600)

title_lebel = tk.Label(master=window, text='สูตรคูณ')
title_lebel.pack(pady=10)
input_number = tk.Entry(master=window, width=25)
input_number.pack(pady=10)
input_button = tk.Button(master=window, text='คลิก', width=10, command=create)
input_button.pack(pady=10)
time_table = tk.Label(master=window)
time_table.pack()


window.mainloop()
