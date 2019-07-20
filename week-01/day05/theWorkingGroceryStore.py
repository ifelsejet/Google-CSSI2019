#class defines a new type
#init is a constructor, pass properties to that type
class Item(object):
    def __init__(self, name, price, inventory, isTaxable):
        self.price = price
        self.name = name
        self.inventory = inventory
        self.isTaxable = isTaxable

#banana = Item("banana", 8, 10, False)
#bread = Item("bread", 3, 10, False)
#eggs = Item("eggs", 10, 1, True)

inventory = {
'banana' : Item("banana", 8, 10, False),
'bread' : Item("bread", 3, 10, False),
"eggs" : Item("eggs", 10, 1, True)


}

"""
prices = {
    'banana' : 8,
    'watermelon' : 1,
    'chocolate milk' : 5,
    'nutrional yeast' : 8,
    'eggs' : 10,
    'bread' : 3

}

store = {
    'banana' : 10,
    'watermelon' : 10,
    'chocolate milk' : 10,
    'nutrional yeast' : 10,
    'eggs' : 10,
    'bread' : 10

}

taxable = ["chocolate milk", "eggs"]
"""

shopping_list = raw_input('Shopping List: ').split(",")

total = 0
for item in shopping_list:
    if item in store and store[item].inventory > 0:
        if store[item].is_taxable:
            total += store[item].price * 1.1
        store[item].inventory -= 1
