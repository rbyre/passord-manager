from tkinter import *
from tkinter import messagebox
import random as r




window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

def generate_password():
  characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø','å','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' 'Æ', 'Ø', 'Å','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', '|', ':', '<', '>', '.', '?', '/', '`', '~']
  password = []
  passwordstring =""
  for x in range(16):
    char = r.choice(characters)
    password.append(char)
  password_entry.insert(0, passwordstring.join(password))


def save_password():
  website = website_entry.get()
  username = user_entry.get()
  password = password_entry.get()
  mydata = f"{website} | {username} | {password}"
  if len(website) > 0 and len(password) > 0:
    is_ok = messagebox.askokcancel(title=website,message=f"Du prøve å lagra følgande: {mydata} e det ok å lagra?")

    if is_ok:
      with open('data.txt', 'a') as f:
        f.write(mydata)
        f.write("\n")
      website_entry.delete(0, END)
      password_entry.delete(0,END)
  else:
    messagebox.showerror(title="Manglende data", message="Et nødvendig felt er tomt. Vennligst legg inn.")

  
  
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image((100,100), image=logo_img )
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)


user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
user_entry.insert(0, "runar@email.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2, sticky="EW")

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")




window.mainloop()