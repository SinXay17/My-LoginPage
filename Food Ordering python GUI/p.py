import tkinter as tk
from tkinter import messagebox


menu = [
    ("ເຂົ້າຂາໝູ", 45),
    ("ເຂົ້າຂາໝາ", 50),
    ("ແກງຈືດ", 80),
    ("ແກງເຄັມ", 35),
    ("ເສສວນ", 55),
    ("ຍໍາສະລັດ", 60),
    ("ພັດກະເພົາ", 40),
    ("ປິ້ງຂາໝາ", 35),
    ("ທອດຂາໝາ", 70),
    ("ໝາລ່າ", 65)
]


window = tk.Tk()
window.title("food der")
window.geometry("450x500")

label = tk.Label(window, text="click food to add amount")
label.pack()


quantities = []
for i in range(len(menu)):
    quantities.append(0)


listbox = tk.Listbox(window, width=45, height=12)
listbox.pack()


def show_list():
    listbox.delete(0, tk.END)
    for i in range(len(menu)):
        name = menu[i][0]
        price = menu[i][1]
        qty = quantities[i]
        listbox.insert(tk.END, name + " - " + str(price) + " ກີບ  | ຈໍານວນ: " + str(qty))


def add_qty(event):
    sel = listbox.curselection()
    if sel:
        idx = sel[0]
        quantities[idx] = quantities[idx] + 1
        show_list()

listbox.bind("<<ListboxSelect>>", add_qty)

show_list()


def calculate():
    total = 0
    text = ""

    for i in range(len(menu)):
        if quantities[i] > 0:
            name = menu[i][0]
            price = menu[i][1]
            qty = quantities[i]
            total += price * qty
            text += name + " x " + str(qty) + " = " + str(price * qty) + " ກີບ\n"

    if total == 0:
        messagebox.showinfo("total", "ບໍ່ມີການເລືອກ")
    else:
        messagebox.showinfo("total", text + "\nລວມ: " + str(total) + " ກີບ")

btn = tk.Button(window, text="ຄໍານວນ", command=calculate)
btn.pack(pady=20)

window.mainloop()

