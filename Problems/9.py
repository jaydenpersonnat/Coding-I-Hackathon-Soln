

def change(amount): 
    numCoins = 0
    coins = [500,100,25,10,5,1]
    for value in coins:
        while amount >= value:
            amount -= value
            numCoins += 1
    return numCoins 

print(change(468))