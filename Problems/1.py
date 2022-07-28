

def main(): 
    
    price = float(input("Price of item: "))
    tax = float(input("Tax percentage: ")) / 100 

    print(f"{format(price * (1 + tax), '.2f')}")
    
    return 



main() 

