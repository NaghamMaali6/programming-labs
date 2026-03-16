class Payment :
    def __init__(self) :  #Constructor : runs automatically when a new payment is made
        self.inserted_amount = 0  #default amount is zero (when the user hasn't inserted any money yet)
        
    def add_money(self , amount) :  
        self.inserted_amount += amount  #add the money that the user inserts
        print(f"Inserted : ${self.inserted_amount:.2f}") 
        
    def is_enough(self , price) :
        return (self.inserted_amount >= price)  #return True if the inserted money is enough to buy the item
        
    def calculate_change(self , price) :
        if self.inserted_amount > price :  #if the user inserts money more than the item's price
            return (self.inserted_amount - price)  #return the difference as change
        
        return 0  #no change
            
            
    def reset(self) :
        self.inserted_amount = 0  #reset the inserted amount back to 0 after finishing one purchase 
