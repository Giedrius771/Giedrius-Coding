import re


def split_names(name):
    pattern = re.compile(r'^([A-Z]\w{1,3}\.)\s([A-Z]\w+)\s([A-Z]\w+)$')
    result = pattern.search(name)
    if result:
        print(f'Visa eilute: {result.group(0)}')
        print(f'Kreipinys: {result.group(1)}')
        print(f'Vardas: {result.group(2)}')
        print(f'Visa Pavarde: {result.group(3)}')
        print('------------------------------------')
        print(result.group())
        print(result.groups())
    else:
        print('Ivestis neatitinka sablono')


split_names('Mr. Clint Eastwood')

pattern = re.compile(r'\+370\s\d{3}\s\d{5}')

tekstas = '''Pirmas telefono numeris yra +370 123 12321, antras +370 321 10101'''
res = pattern.search(tekstas)
print(res)
print((res.group()))

res = pattern.findall(tekstas)
print(res)


def validate_email(input):
    email_regex = re.compile(r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$')
    result = email_regex.search(input)
    if result:
        return True
    return False


print(validate_email('kazkoks@email.lt'))
print(validate_email('blogas@@email.com'))

card_number = "card1: 0452 6544 0004 4456, card2: 1234 4567 8910 1112"
pattern = re.compile(r'\b\d{4}\s\d{4}\s\d{4}\s\d{4}\b')
res = pattern.sub('**** **** **** ****', card_number)
print(res)
card_number = "card1: 0452 6544 0004 4456, card2: 1234 4567 8910 1112"
pattern = re.compile(r'\b(\d{4})\s\d{4}\s\d{4}\s\d{4}\b')
res = pattern.sub('\g<1> **** **** ****', card_number)
print(res)
tekstas = '''Trumpas tekstas
apie beleką'''
pattern = re.compile(r't\w+', re.I)
res = pattern.findall(tekstas)
print(res)

# ['Trumpas', 'tekstas']
tekstas = '''Trumpas tekstas
apie beleką'''

pattern = re.compile(r'^\w+')
res = pattern.findall(tekstas)

pattern2 = re.compile(r'^\w+', re.M)
res2 = pattern2.findall(tekstas)

print(res)
print(res2)
tekstas = 'Jonas Jonaitis +370 622 01234'
pattern = re.compile(r'''
                    [A-Z]\w+              # vardas
                    \s                    # tarpas
                    [a-z]\w+              # pavardė
                    \s                    # tarpas
                    \+370\s6\d{2}\s\d{5}  # telefono numeris
                    ''', re.X | re.I)
res = pattern.findall(tekstas)
print(res)

#############
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
