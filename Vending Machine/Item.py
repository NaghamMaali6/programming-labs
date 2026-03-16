"""Items in the vending machine"""

class Item :
    def __init__(self , code , name , price) :  #Constructor : runs automatically when a new item is created
        self.code = code  #save te item's code 
        self.name = name  #save the item's name 
        self.price = price  #save the item's price 
        
    def __str__(self) :  #special method decides how the item looks when it's printed
        return f"{self.code} : {self.name} - ${self.price:.2f}"    
