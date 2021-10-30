""" import random

import constants
for i in range(1,21):
    print(f"\n{i}")
    print(constants.LIBRARY[random.randint(1,1000)])
#print(random.choice(constants.LIBRARY)) """

""" list = [0,1,2,3,4,5,6]

print(list[1:]) """

""" class Actor():
    def __init__(self):
        self._item = ""
        self._position = 0
        self._price = 0

    def get_position(self):
        return self._position

    def get_item(self):
        return self._item

    def get_price(self):
        return self._price

    def set_item(self, item):
        self._item = item

    def set_position(self, position):
        self._position = position
    
    def set_price(self, price):
        self._price = price
    
    
class shopping(Actor):
    def __init__(self):
        super().__init__()
        self.shoping_list = []


    def make_shoping_list(self, item, position, price):
        Item = Actor()
        Item.set_item(item)
        Item.set_position(position)
        Item.set_price(price)
        self.shoping_list.append(Item)

    def get_shopping_list(self):
        return self.shoping_list

class master():

    def __init__(self):
        self.shoping = shopping()
           
    def start(self):
        self.shoping.make_shoping_list("apple", "Food", "15.99")
        self.shoping.make_shoping_list("cheese", "Food", "3.99")
        for item in range(len(self.shoping.shoping_list)):
            praduct = self.shoping.shoping_list[item]
            name = praduct.get_item()
            position = praduct.get_position()
            price = praduct.get_price()
            print(f"{name}: {position}, ${price}")



Master = master()
Master.start()
  """
