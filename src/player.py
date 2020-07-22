from src.room import Room


# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name=name
        self.current_room = current_room
        self.items = []

    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.current_room.get_item(item)
        self.items.remove(item)

     def inventory(self):
        if len(self.items) == 0:
            print("You have nothing")

        for item in self.items:
            print(item.name)