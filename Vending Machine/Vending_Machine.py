""" Vending Machine """

from Item import Item  #import Item class from Item.py
from Payment import Payment  #import Payment class from Payment.py

class Vending_Machine :
        def __init__(self) :  #constructor
            self.Items = {}  #create an empty dictionary to store all the items inside the machine
            self.payment = Payment()  #create a Payment object to handle money operations for this machine
            
        #function to add new items to the machine:
        def addItem(self , item) :
            self.Items[item.code] = item  
            
        #function to show all available items:
        def displayItem(self) :
            print("Available Items:\n")
            for item in self.Items.values() :  #for loop goes through all items
                print(item)  #print each item
                
        #function to let user choose an item by it's code:
        def selectItem(self , code) :
            if code in self.Items :  #check if the entered code exists
                selected = self.Items[code]
                print(f"{selected.name} for ${selected.price:.2f}")  #show the item's name and price
                return selected
            else :  #if the code is invalid
                print("Invalid code!\n")
                return None
        
        #function to take the amount of money the user put in:
        def insertMoney(self , amount) :
            self.payment.add_money(amount)
        
        #function to give the item to the user if they paid enough:
        def item_out(self , item) :
            if self.payment.is_enough(item.price) :  #check if the inserted money is enough for the item's price
                print(f"here's your {item.name} :) Enjoy!")
                change = self.payment.calculate_change(item.price)  #calculate if there is any change to return
                if change > 0 :  #if there is extra money
                    print(f"your change: ${change:.2f}")  #reset(set the inserted money back to zero)
                self.payment.reset()
            else :  #if the user didn't insert enough money
                print(f"not enough money!!! please insert at least ${item.price:.2f}")            

if __name__ == "__main__" :
    vm = Vending_Machine()  #create vending machine object
    
    #add different items to the machine using the item class:
    vm.addItem(Item("A1" , "Potato Chips" , 2.50))
    vm.addItem(Item("A2" , "Chocolate Bar" , 3.00))
    vm.addItem(Item("A3" , "Oreo" , 1.500))
    vm.addItem(Item("B1" , "Water" , 2.00))
    vm.addItem(Item("B2" , "Cola" , 2.00))
    vm.addItem(Item("B3" , "Soda" , 2.00))
    vm.addItem(Item("C1" , "Iced Tea" , 2.50))
    vm.addItem(Item("C2" , "Tissues" , 4.00))
    vm.addItem(Item("C3" , "Mint Gum" , 2.00))
    
    vm.displayItem()  #show all items to the user
    
    code = input("ENTER THE CODE OF THE ITEM YOU WANT:\n")  #ask for item's code
    
    item = vm.selectItem(code)  #save the item that matches the entered code
    if item :  #if the item exists
        while not vm.payment.is_enough(item.price) :  #keep asking for more money until there is enough
            money = float(input(f"Insert ${item.price:.2f} please.\n")) 
            vm.insertMoney(money)  #add the inserted money to the machine
        
        vm.item_out(item)  #give the item to the user when enough money is inserted
