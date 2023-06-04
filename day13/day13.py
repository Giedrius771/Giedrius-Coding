### 2 UZDUOTIS #####
from tkinter import Tk, Label, Entry, Button


def generate_leap_years():
    start_year = int(start_entry.get())
    end_year = int(end_entry.get())

    leap_years = []
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            leap_years.append(year)

    output_label.config(text="Keliamieji metai: " + ', '.join(map(str, leap_years)))


root = Tk()
root.title("Keliamieji metai")
root.iconbitmap("/Users/giedriuspranevicius/Downloads/icona.ico")

start_label = Label(root, text="Metai nuo:")
start_label.pack()

start_entry = Entry(root)
start_entry.pack()

end_label = Label(root, text="Metai iki:")
end_label.pack()

end_entry = Entry(root)
end_entry.pack()

generate_button = Button(root, text="Generuoti", command=generate_leap_years)
generate_button.pack()

output_label = Label(root)
output_label.pack()

root.mainloop()
###### 3 UZDUOTIS ######
