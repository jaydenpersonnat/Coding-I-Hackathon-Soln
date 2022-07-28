
def is_prime(number): 
    for div in range(2, number // 2):
        if number % div == 0:
            return False 
    return True  

def sum_primes(number): 
    sum = 0 
    for i in range(3, number, 2): 
        if is_prime(i): 
            sum += i 
    
    return sum

