class Item:
     def __init__(self, item, item_description):
          self.item = item
          self.item_description = item_description

     def on_take(self):
          print(f'You have picked up {self.item}')
     
     def on_drop(self):
          print(f'You have dropped {self.item}')


          # .on_take() is a method on each item object