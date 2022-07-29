
def main(): 
    
    min_wage = float(input("Enter a minimum wage: "))
    num_of_years = float(input("Enter a year: "))
    num_of_children = int(input("Enter number of children: "))

    print(f"{format(min_wage + (num_of_years * 20) + (num_of_children * 30), '.2f')}")

    return 

main() 

