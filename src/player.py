# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
     def __init__(self, name, current_room, inventory):
          self.name = name
          self.current_room = current_room
          self.items_in_inventory = inventory           #ability to add items into inventory 

     def take_item(self, item):
          for i in self.current_room.items_in_room:
               print('comparing items in the room~~>', i.item)
               print('this is the item you are trying to pick up ~~>', item)
               if item == i.item:
                    self.items_in_inventory.append(i)
                    self.current_room.items_in_room.remove(i)
                    print(f'you have picked up {item}')
                    print(f'you have {self.items_in_inventory} in your inventory')
               else:
                    print(f'you were unable to pick up the item')


     def throw_item(self, item):
          print('this is the item you are trying to drop ~~>', item)
          if(item in self.items_in_inventory):
               self.items_in_inventory.remove(item)
               print(f'you have removed {item} from your inventory')
          else:
               print(f'you do not have {item} in your inventory')