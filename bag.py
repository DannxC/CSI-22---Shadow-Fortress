import pygame

class Item:
    def __init__(self, name, quantity=1):
        self.name = name
        self.quantity = quantity

    def use(self):
        pass

class HealthPotion(Item):
    def __init__(self, name="Health Potion", quantity=1):
        super().__init__(name, quantity)
        self.name = "Health Potion"
        self.icon = pygame.image.load('assets/health_potion_icon.png').convert_alpha()
        self.quantity = quantity

    def use(self):
        self.quantity -= 1
        if self.quantity <= 0:
            self.quantity = 0

class Bag:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.items = [None] * capacity

    def add_item(self, item, index):
        if self.items[index] is None:
            self.items[index] = item
            return True
        elif self.items[index].name == item.name:
            self.items[index].quantity += 1
            return True
        return False  # Bag is full

    def remove_item(self, index):
        if 0 <= index < self.capacity:
            removed_item = self.items[index]
            self.items[index] = None
            return removed_item
        return None  # Invalid index

    def get_item(self, index):
        if 0 <= index < self.capacity:
            return self.items[index]
        return None  # Invalid index

    def is_full(self):
        return all(slot is not None for slot in self.items)
    
    def check_and_remove_empty_items(self):
        for (index, item) in enumerate(self.items):
            if item is not None and item.quantity <= 0:
                self.remove_item(index)

