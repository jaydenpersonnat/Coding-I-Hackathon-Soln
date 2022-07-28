

def main(): 
    
    age = int(input("Enter an age: "))

    if age >= 90: 
        print(2022 - (age - 90))
    else:
        print((90 - age) + 2022)

    return 


main() 

