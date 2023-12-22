from enum import Enum

class Machine:
    slots: list[list]
    item_inventory: dict
    item_position: dict
    
    def get_igem(self, id):
        pass
    
class NumPad:
    buttons: list
    
    def read():
        pass
    
class Display:
    def print_message():
        pass
    
class Item:
    id: int
    name: str
    price: float
    desctiption: str
    dimentions: list #[length, width, height]

class SlotType(Enum):
	SMALL = [1,2,3]
	MEDIUM = [4,5,6]
	LARGE = [5,6,7]
 
class Payment:
    def varify_payment():
        pass
    
    def amount_received():
        pass

class CashPayment(Payment):
    pass

class UPIPayment(Payment):
    pass
    