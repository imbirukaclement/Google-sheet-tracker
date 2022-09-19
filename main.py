from tkinter import*
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
today =datetime.now()
def save():
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Tutorial").sheet1
    company_name = company_entry.get()
    Product = Product_entry.get()
    quantity = int(Quantity_entry.get())
    new_data = [f"{today}",f"{company_name}", f"{Product}", quantity]
    sheet.insert_row(new_data, 2)


window = Tk()
window.title("Password")
window.minsize(height=300, width=300)
window.config(padx=2, pady=20)


canvas=Canvas(height=200, width=200)
# logo_image = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

company_label=Label(text="Company Name: ")
company_label.grid(column=0, row=1)
Product_label = Label(text="Product:")
Product_label.grid(row=2, column=0)
Quantity_label = Label(text="Quantity:")
Quantity_label.grid(row=3,column=0)

company_entry = Entry(width=35)
company_entry.grid(column=1,row=1)
company_entry.focus()
Product_entry = Entry(width=35)
Product_entry.grid(column=1, row=2, columnspan=2)
Product_entry.insert(0,"Fresh Produce")
Quantity_entry = Entry(width=35)
Quantity_entry.grid(column=1, row=3, columnspan=1)

add_button = Button(text="add", width=21,command=save)
add_button.grid(row=6, column=1, columnspan=2)


window.mainloop()