#lists = arrays
#list() -> characters
#split() -> array
"""
TODO:
1) Get shopping list from user
2) Include taxes
3) Keep track of inventory after every purchase
4) Prevent negative purchasing (purchases that have no inventory)
"""
#this is a dictronary
prices = {
    'banana' : 8,
    'watermelon' : 1,
    'chocolate milk' : 5,
    'nutrional yeast' : 8,
    'eggs' : 10,
    'bread' : 3

}

inventory = {
    'banana' : 8,
    'watermelon' : 1,
    'chocolate milk' : 5,
    'nutrional yeast' : 8,
    'eggs' : 10,
    'bread' : 3
}

def get_shopping_list():
    items  = raw_input("Please enter the items you wish to buy: ")
    listOfItems = items.split()
    quantityOfItems = raw_input("Please enter the quanity of items you wish to buy: ")
    qItems  = quantityOfItems.split()

    return qItems, listOfItems

def check_inventory(item, quantity):
    in_stock = inventory[item]
    if(quantity < in_stock):
        inventory[item] = in_stock - quantity
    else:
        quantity = in_stock
        inventory[item] = 0
    print quantity



#get total price after taxes
def get_price(list, quantity):
    taxes = 1.95
    total = 0

    for item in items:
        check_inventory(item, quanity[item])
    for item in list:
        if item in prices:
            total += prices[item]
    print total * taxes



list = get_shopping_list()
inventory = check_inventory()

get_price(list)

"""
shopping_list = ['bread','eggs','kale']
total = 0
for item in shopping_list:
    if item in prices:
    total += prices[item]

print total
"""
