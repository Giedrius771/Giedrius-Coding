from marketplace.phone import Phone
from marketplace.keyboard import Keyboard

"""from item import Item

item1 = Item("MyItem", 750, 6)"""
item1 = Phone("jscPhone", 1000, 3)
item2 = Keyboard("jscKeyboard", 1000, 3)

item1.apply_discount()

print(item1.price)
print(item2.price)
"""item1.send_email()"""