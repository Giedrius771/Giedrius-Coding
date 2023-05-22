### 1 uzduotis
import tkinter as tk


def pasveikintit():
    name = name_entry.get()
    result_label.config(text="Labas, {}!".format(name))


window = tk.Tk()
window.title("Sveikinimo programa")

input_frame = tk.Frame(window)
input_frame.pack(pady=10)

name_label = tk.Label(input_frame, text="Įveskite vardą:")
name_label.pack(side="left")

name_entry = tk.Entry(input_frame, width=30)
name_entry.pack(side="left")

button = tk.Button(window, text="Patvirtinti", command=pasveikintit)
button.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack()

window.mainloop()
##### 2 uzduotis ######
import tkinter as tk


def greet():
    name = name_entry.get()
    result_label.config(text="Labas, {}!".format(name))


def handle_enter(event):
    greet()


# Create the main window
window = tk.Tk()
window.title("Sveikinimo programa")

# Create a frame for the input elements
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# Create the name label and entry
name_label = tk.Label(input_frame, text="Įveskite vardą:", font=("Arial", 14))
name_label.pack(side="left")

name_entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
name_entry.pack(side="left")
name_entry.bind("<Return>", handle_enter)  # Bind the Enter key to the handle_enter function

# Create the button
button = tk.Button(window, text="Patvirtinti", command=greet, font=("Arial", 14, "bold"))
button.pack(pady=10)

# Create the result label
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack()

# Set focus on the name entry field
name_entry.focus()

# Start the main loop
window.mainloop()
## uzduotis 3 ########
import tkinter as tk


def greet():
    name = name_entry.get()
    result_label.config(text="Labas, {}!".format(name))
    last_greeting = result_label.cget("text")


def handle_enter(event):
    greet()


def clear_text():
    result_label.config(text="")


def restore_text():
    result_label.config(text=last_greeting)


def exit_program():
    window.destroy()


# Create the main window
window = tk.Tk()
window.title("Sveikinimo programa")

# Create a frame for the input elements
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# Create the name label and entry
name_label = tk.Label(input_frame, text="Įveskite vardą:", font=("Arial", 14))
name_label.pack(side="left")

name_entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
name_entry.pack(side="left")
name_entry.bind("<Return>", handle_enter)  # Bind the Enter key to the handle_enter function

# Create the button
button = tk.Button(window, text="Patvirtinti", command=greet, font=("Arial", 14, "bold"))
button.pack(pady=10)

# Create the result label
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack()

# Set focus on the name entry field
name_entry.focus()

# Create the menu
meniu = tk.Menu(window)
window.config(menu=meniu)

submeniu = tk.Menu(meniu, tearoff=0)
submeniu.add_command(label="Išvalyti", command=clear_text)
submeniu.add_command(label="Atkurti", command=restore_text)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=exit_program)

meniu.add_cascade(label="Meniu", menu=submeniu)

# Start the main loop
window.mainloop()
##### 3 uzduotis ###
import tkinter as tk


def pasveikinimas():
    name = name_entry.get()
    result_label.config(text="Labas gero pirmadienio".format(name))
    global paskutinis
    paskutinis = result_label.cget("text")


def paspaudus_enter(event):
    pasveikinimas()


def isvalymas_teksto():
    result_label.config(text="")


def atgrazinti():
    result_label.config(text=paskutinis)


def iseiti():
    langas.destroy()


langas = tk.Tk()
langas.geometry("200x150")
langas.title("Sveikinimo programa")

input_frame = tk.Frame(langas)
input_frame.pack(pady=10)

name_label = tk.Label(input_frame, text="Įveskite vardą:", font=("Arial", 14))
name_label.pack(side="left")

name_entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
name_entry.pack(side="left")
name_entry.bind("<Return>", paspaudus_enter)

button = tk.Button(langas, text="Patvirtinti", command=pasveikinimas, font=("Arial", 14))
button.pack(pady=10)

result_label = tk.Label(langas, text="", font=("Arial", 14))
result_label.pack()

name_entry.focus()

meniu = tk.Menu(langas)
langas.config(menu=meniu)

submeniu = tk.Menu(meniu, tearoff=0)
submeniu.add_command(label="Išvalyti", command=isvalymas_teksto)
submeniu.add_command(label="Atkurti", command=atgrazinti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

meniu.add_cascade(label="Meniu", menu=submeniu)

langas.mainloop()
### 4 UZDUOTIS ########
import tkinter as tk


class Pasisveikinimas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Sveikinimo programa")
        self.last_greeting = ""
        self.status_text = tk.StringVar(value="Pradinė būsena")

        self.create_widgets()
        self.create_menu()
        self.bind_events()

        self.name_entry.focus()

    def create_widgets(self):
        input_frame = tk.Frame(self, padx=10, pady=10)
        input_frame.pack()

        tk.Label(input_frame, text="Įveskite vardą:", font=("Arial", 14)).pack(side="left")
        self.name_entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
        self.name_entry.pack(side="left")

        tk.Button(self, text="Patvirtinti", command=self.pasveikinimas, font=("Arial", 14)).pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 14))
        self.result_label.pack()

        self.status_bar = tk.Label(self, textvariable=self.status_text, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_menu(self):
        meniu = tk.Menu(self)
        self.config(menu=meniu)

        submeniu = tk.Menu(meniu, tearoff=0)
        submeniu.add_command(label="Išvalyti", command=self.isvalyti_teksta)
        submeniu.add_command(label="Atkurti", command=self.atkurti_teksta)
        submeniu.add_separator()
        submeniu.add_command(label="Išeiti", command=self.baigti_programa)

        meniu.add_cascade(label="Meniu", menu=submeniu)

    def bind_events(self):
        self.name_entry.bind("<Return>", self.handle_enter)
        self.bind("<Escape>", self.baigti_programa)

    def pasveikinimas(self):
        vardas = self.name_entry.get()
        pasisveikinimas = "Labas, {}!".format(vardas)
        self.result_label.config(text=pasisveikinimas)
        self.status_text.set("Sukurta")
        self.last_greeting = pasisveikinimas

    def handle_enter(self, event):
        self.pasveikinimas()

    def isvalyti_teksta(self):
        self.result_label.config(text="")
        self.status_text.set("Išvalyta")

    def atkurti_teksta(self):
        self.result_label.config(text=self.last_greeting)
        self.status_text.set("Atkurta")

    def baigti_programa(self, event=None):
        self.destroy()


if __name__ == "__main__":
    program = Pasisveikinimas()
    program.mainloop()
