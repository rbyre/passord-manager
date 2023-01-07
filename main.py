from tkinter import *
from tkinter import messagebox
import random as r
import pyperclip
import json




window = Tk()
window.title("Passord Manager")
window.config(padx=50, pady=50)

def generate_password():
  characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø','å','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' 'Æ', 'Ø', 'Å','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', '|', ':', '<', '>', '.', '?', '/', '`', '~']
  password = [r.choice(characters) for _ in range(16)]
  passwordstring =""
  new_password = passwordstring.join(password)
  password_entry.insert(0, new_password)
  pyperclip.copy(new_password)


def save_password():
  website = website_entry.get()
  username = user_entry.get()
  password = password_entry.get()
  new_data = {
    website: {
      "username": username,
      "password": password,
    }
  }
  if len(website) > 0 and len(password) > 0:
    try:
        with open('data.json', 'r') as f:
          data = json.load(f)
          data.update(new_data)

        with open('data.json', 'w') as f:
          json.dump(data, f, indent=4)
          
          website_entry.delete(0, END)
          password_entry.delete(0,END)
    except FileNotFoundError:
      with open('data.json', 'w') as f:
        json.dump(new_data, f, indent=4)
  else:
    messagebox.showerror(title="Manglende data", message="Et nødvendig felt er tomt. Vennligst legg inn.")


# søk etter passord
def search(website):
  try:
    with open('data.json', 'r') as f:
      data = json.load(f)
      user_entry.delete(0,END)
      user_entry.insert(0, data[website]['username'])
      password_entry.insert(0, data[website]['password'])
  except:
    messagebox.showerror(title="Feil", message="Nettsted ikke funnet")


  
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image((100,100), image=logo_img )
canvas.grid(row=0, column=1)

website_label = Label(text="Nettsted:", anchor='w')
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

search_button = Button(text="Søk", command=lambda: search(website_entry.get()))
search_button.grid(row=1, column=2, sticky="EW")

user_label = Label(text="Brukernavn:", anchor='w')
user_label.grid(row=2, column=0)


user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
user_entry.insert(0, "runar@email.com")

password_label = Label(text="Password:", anchor='w')
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

generate_password_btn = Button(text="Generer passord", command=generate_password)
generate_password_btn.grid(row=3, column=2, sticky="EW")

add_btn = Button(text="Legg til/Oppdater", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")





window.mainloop()