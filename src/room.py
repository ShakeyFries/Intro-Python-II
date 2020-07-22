from src.item import Item

# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
      self.name = name
      self.description = description
      self.n_to = None
      self.s_to = None
      self.w_to = None
      self.e_to = None
      self.items = []

  def __str__(self):
    return f"Room: {self.name}, Description: {self.description}"

  def Items(self):
    return self.items

  def get_item(self,item):
    self.items.append(item)

  def drop_item(self, item):
    self.items.remove(item)
