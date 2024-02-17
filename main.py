import json
from tkinter import *
from random import *
from tkinter import messagebox
import pyperclip

# TODO ---------------------------------------- Functions --------------------------------------------

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    """This will generate a random password from list above"""
    pass_letters = [choice(letters) for item in range(6)]
    pass_numbers = [choice(numbers) for item in range(3)]
    pass_symbols = [choice(symbols) for item in range(2)]
    final_pass = (pass_symbols + pass_numbers + pass_letters)
    shuffle(final_pass)
    final_pass = "".join(final_pass)
    pyperclip.copy(final_pass)
    password_text.delete(0, END)
    password_text.insert(index=0, string=final_pass)


def add_data():
    """This will Get the datas from Website and password and turn it into a Dictionary"""
    website_data = website_text.get()
    email_data = email_text.get()
    password_data = password_text.get()

    data = {
        website_data: {
            "Email": email_data,
            "Password": password_data
        }
    }
    if website_text == '' or password_text == '' or len(password_text.get()) < 6:
        messagebox.showinfo(title=" Empty Fields", message=" fill all the empty spaces \n password must "
                                                           "be at least 6 characters")
    try:
        with open('data.json', mode='r') as read_data:
            loaded_data = json.load(read_data)

    except FileNotFoundError or ValueError:
        with open('data.json', mode="w") as data_file:
            json.dump(data, data_file, indent=3)
    else:
        print(type(loaded_data))
        loaded_data.update(data)
        with open('data.json', mode='w') as update_data:
            json.dump(loaded_data, update_data, indent=4)
    finally:
        website_text.delete(0, END)
        password_text.delete(0, END)


def search_data():
    with open('data.json') as reading_file:
        searching_file = json.load(reading_file)
        web_entry = website_text.get().title()
        if website_text.get() not in searching_file:
            messagebox.showinfo(title='Item not Found', message=f"{web_entry} was not found in data base")
        else:
            messagebox.showinfo(title="Info", message=f"website name: {web_entry} \n"
                                                      f"email:{searching_file[web_entry]['Email']}\n"
                                                      f"password: {searching_file[web_entry]['Password']}")

# TODO ----------------------------------------------- tk inter ---------------------------------


win = Tk()
win.title("Password Manager")
win.config(pady=50, padx=50)

my_canvas = Canvas(width=200, height=200, bg="white")
my_image = PhotoImage(file='logo.png')
my_canvas.create_image(100, 100, image=my_image)
my_canvas.grid(column=2, row=1)

website = Label(text='Website:')
website.grid(column=1, row=2)
website_text = Entry(width=33)
website_text.focus()
website_text.grid(column=2, row=2)

email = Label(text="Email/Username:")
email.grid(column=1, row=3)
email_text = Entry(width=59)
email_text.insert(index=0, string="Mojtabaparvizi19@gmail.com")  # TODO : enter a text as a default
email_text.grid(column=2, columnspan=2, row=3)

password = Label(text="Password:")
password.grid(column=1, row=4)
password_text = Entry(width=33)
password_text.grid(column=2, row=4)

generate_button = Button(text='Generate Password', width=20, command=generate_password)
generate_button.grid(row=4, column=3)

add_button = Button(width=50, text="Add", command=add_data)
add_button.grid(column=2, columnspan=2, row=5)

search_button = Button(text="search", width=20, command=search_data)
search_button.grid(column=3, row=2)

win.mainloop()
