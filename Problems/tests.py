
from colorama import Fore
import math 

four = __import__("4")   
five = __import__("5")
six = __import__("6")
seven = __import__("7")
eight = __import__("8")   
nine = __import__("9")
ten = __import__("10")
eleven = __import__("11")
twelve = __import__("12")
thirteen = __import__("13")
fourteen = __import__("14")
fifteen = __import__("15")
sixteen = __import__("16")
seventeen = __import__("17")
eighteen = __import__("18")
nineteen = __import__("19")
twenty = __import__("20")


boolean_lst = [] 

def unit_test(condition, msg):
    if condition:
        print(Fore.GREEN + msg + " passed")
        return True
    else:
        print(Fore.RED + msg + " failed")
        return False 

test_lst = ["hello", 2, 5, 3.6, "jayden", 7.5, True, False, True]
test_lst2 = ["hello", True, False, 6, 9, 3, 4]
condition1 = set(five.common(test_lst, test_lst2)) == set((["hello", True, False]))
condition2 = len(set(five.common(test_lst, test_lst2))) == 3


# Search unit tests 
search_true_input_lst = [
    [4, [5,6,7,4,8]], 
    ["hi",  [2, 3.5, "hi", "hello", "world", True, False, 5.7, 9.20, [5, 6]]]
]

search_false_input_lst = [
    [10, [3.6, 7.5, 12, 18, 25, 4, 3]],
    ["hello", []]
]


for element in search_true_input_lst:
    try: 
        boolean_lst.append(unit_test(four.search(element[0], element[1]), "search test"))
    except: 
        print(Fore.RED + "search test failed")
        boolean_lst.append(False)
  
for element in search_false_input_lst:
    try: 
        boolean_lst.append(unit_test(not four.search(element[0], element[1]), "search test"))
    except: 
        print(Fore.RED + "search test failed")
        boolean_lst.append(False)


# Common unit test 
common_lst = [
  [[], [], []], 
  [[], [2,4,5,8], []], 
  [[1,1,2,3,5,9,14,17,28,56], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1,2,3,5,9]], 
  [[2,5,7,9], [1, 9, 12, 14], [9]], 
]

for inputs in common_lst:
    try:
        boolean_lst.append(unit_test(set(five.common(inputs[0], inputs[1])) == set(inputs[2]), "common test"))
    except:
        print(Fore.RED + "common test failed")
        boolean_lst.append(False)

try:
    boolean_lst.append(unit_test(five.common([2,3,-5,6,7,3,3,2], [1,5,8,4,20,3,2,3,1]) == [2,3] or five.common([2,3,-5,6,7,3,3,2], [1,5,8,4,6,3,2,3,1]) == [3,2], "common test"))
except:
    print(Fore.RED + "common test failed")
    boolean_lst.append(False)

# luhn unit test 

luhn_valid = [378282246310005, 371449635398431, 6011111111111117, 3530111333300000, 4012888888881881, 4222222222222]

for credit_num in luhn_valid:
    try:
        boolean_lst.append(unit_test(six.luhn(credit_num), "luhn test"))
    except:
        print(Fore.RED + "luhn test failed")
        boolean_lst.append(False) 

try:
     boolean_lst.append(unit_test(not six.luhn("2418293121314"), "luhn test"))
except:
    print(Fore.RED + "luhn test failed")
    boolean_lst.append(False) 



# lettersum unit test 
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(26):
    try:
        boolean_lst.append(unit_test(seven.lettersum(letters[i]) == i + 1, "lettersum " + str(i)))
    except:
        print(Fore.RED + "luhn test failed")
        boolean_lst.append(False)

try:
    boolean_lst.append(unit_test(seven.lettersum("abc") == 6, "lettersum test"))
except:
    print(Fore.RED + "luhn test failed")
    boolean_lst.append(False)

try:
    boolean_lst.append(unit_test(seven.lettersum("excellent") == 100, "lettersum test"))
except:
    print(Fore.RED + "luhn test failed")
    boolean_lst.append(False)


# numcompare unit test 
numcompare_true = [["IV", "V"], ["XC", "C"], ["MDCLXV", "MDCLXVI"], ["IX","X"]]
numcompare_false = [["I", "I"], ["V", "IV"], ["V", "IIII"], ["MM", "MCMXIV"]]

for element in numcompare_true:
    try:
        boolean_lst.append(unit_test(eight.numcompare(element[0], element[1]), "numcompare test"))
    except:
        print(Fore.RED + "numcompare test failed")
        boolean_lst.append(False)


for element in numcompare_false:
    try:
        boolean_lst.append(unit_test(not eight.numcompare(element[0], element[1]), "numcompare test"))
    except:
        print(Fore.RED + "numcompare test failed")
        boolean_lst.append(False)

# change unit test 

change_lst = [ 
    [0,0],
    [12,3], 
    [468, 11],
    [123456, 254], 
    [23, 5],
    [167, 7]
]

for element in change_lst:
    try: 
        boolean_lst.append(unit_test(nine.change(element[0]) == element[1], "change"))
    except: 
        print(Fore.RED + "change test failed")
        boolean_lst.append(False)

# factorial unit test 
factorial_lst = [] 
for i in range(0,40, 1):
    try: 
        boolean_lst.append(unit_test(ten.factorial(i) == math.factorial(i), "factorial " + str(i)))
    except:
        print(Fore.RED + "factorial test failed")
        boolean_lst.append(True)

# tax unit test 
tax_lst = [
    [80000, "14500.00"],
    [35344, "3336.00"], 
    [125000, "29500.00"], 
    [10000, "0.00"], 
    [6573, "0.00"], 
    [14563, "456.30"],
    [30000, "2000.00"], 
    [100000, "19500.00"],
    [123459432.67, "49363273.07"]
]

for element in tax_lst:
    try:
        boolean_lst.append(unit_test(eleven.tax(element[0]) == element[1], "tax"))
    except:
        print(Fore.RED + "tax test failed")
        boolean_lst.append(False)

# sum_primes unit tests 
primes_lst = [[12, 28], [-2, 0], [2,0], [17390, 16274627], [72,639]]

for element in primes_lst:
    try:
        boolean_lst.append(unit_test(twelve.sum_primes(element[0]) == element[1], "sum_primes"))
    except:
        print(Fore.RED + "sum_primes test failed")
        boolean_lst.append(False)

# sundays test () 
try:
    boolean_lst.append(unit_test(thirteen.sundays() == 171, "correct ans"))
except:
    print(Fore.RED + "sundays test failed")
    boolean_lst.append(False)

# shiftRight unit tests () 
shift_lst = [["Hello", 3, "lloHe"], ["World", 2, "ldWor"], ["", 5, ""], ["hello", 2, "lohel"], ["abcd", 14, "cdab"]]

for test in shift_lst: 
    try: 
        boolean_lst.append(unit_test(fourteen.shiftRight(test[0], test[1]) == test[2], "shift"))
    except:
        print(Fore.RED + "shiftRight failed")
        boolean_lst.append(False)


# additive_persistence tests 
for i in range(10): 
    try:
        boolean_lst.append(unit_test(fifteen.additive_persistence(i) == 0, "ap test " + str(i)))
    except:
        print(Fore.RED + "ap test failed")
        boolean_lst.append(False)

ap_lst = [[199, 3], [-199, 3], [9786,2], [-9876, 2], [1254, 2], [-1254, 2]]

for item in ap_lst: 
    try:
        boolean_lst.append(unit_test(fifteen.additive_persistence(item[0]) == item[1], "ap test"))
    except:
        print(Fore.RED + "ap test failed")
        boolean_lst.append(False)

# zip unit tests 
zip_lst = [[[], [], []], [[1,2,3], [2,4,5], [[1,2], [2, 4], [3,5]]], [[4,5,7,8], [3,7,8,9], [[4,3], [5, 7], [7,8], [8,9]]]]

for test in zip_lst:
    try: 
        boolean_lst.append(unit_test(sixteen.zip(test[0], test[1]) == test[2], "zip test"))
    except:
        print(Fore.RED + "zip_test failed")
        boolean_lst.append(False)


# unzip unit test 
unzip_lst = [
    [[], [[], []]],
    [[[4,3], [5,7], [7,8], [8,9]], [[4,5,7,8], [3,7,8,9]]], 
]


for element in unzip_lst: 
    try: 
        boolean_lst.append(unit_test(seventeen.unzip(element[0]) == element[1], "unzip test"))
    except:
        print(Fore.RED + "unzip test failed")
        boolean_lst.append(False)

# comptus tests 

comptus_lst = [
    [2022, {"month": "April", "day": 17, "year": 2022}],
    [2018, {"month": "April", "day": 1, "year": 2018}],
    [2093,  {"month": "April", "day": 12, "year": 2093}],
    [1826, {"month": "March", "day": 26, "year": 1826}]
]

for lst in comptus_lst:
    try:
        boolean_lst.append(unit_test(eighteen.comptus(lst[0]) == lst[1], "comptus test"))
    except:
        boolean_lst.append(False)
        print(Fore.RED + "comptus test failed")


# largest tests 
largest_lst = [ 
    [[[1,2,3], 6, "hello world", 7.5, True, False], "hello world"],
    [[5, {"hello" : 5, 3: 4, 7: 8, 9:2}, 3.7, 12,4, list(range(40))],  list(range(40))],
    [[4,-5,9, 11, "hello world", {5,7,8,3,2,1,9, 10, 11, 12, 14, 15, 6}], {5,7,8,3,2,1,9, 10, 11, 12, 14, 15, 6}]
]

for large_lst in largest_lst:
    try: 
        boolean_lst.append(unit_test(nineteen.largest(large_lst[0]) == large_lst[1], "largest"))
    except:
        boolean_lst.append(False)
        print(Fore.RED + "large test failed")



# sort tests 
try: 
    boolean_lst.append(unit_test(twenty.sort2([[1,2,3], 6, "hello world", 7.5, True, False]) == [True, False, [1,2,3], 6, 7.5, "hello world"], "sort2 1"))
except:
    boolean_lst.append(False)
    print(Fore.RED + "sort test failed")

try: 
    boolean_lst.append(unit_test(twenty.sort2([5, {"hello" : 5, 3: 4, 7: 8, 9:2}, 3.7, 12,4, list(range(40))]) == [3.7, {"hello" : 5, 3: 4, 7: 8, 9:2}, 4,5, 12,list(range(40))] or twenty.sort2([5, {"hello" : 5, 3: 4, 7: 8, 9:2}, 3.7, 12,4, list(range(40))]) == [3.7, 4, {"hello" : 5, 3: 4, 7: 8, 9:2}, 5, 12,list(range(40))] , "sort2 2"))
except:
    boolean_lst.append(False)
    print(Fore.RED + "sort test failed")

try: 
    boolean_lst.append(unit_test(twenty.sort2([4,-5,9, 11, "hello world", {5,7,8,3,2,1,9, 10, 11, 12, 14, 15, 6}]) == [-5, 4, 9, 11, "hello world", {5,7,8,3,2,1,9, 10, 11, 12, 14, 15, 6}] or twenty.sort2([4,-5,9, 11, "hello world", {5,7,8,3,2,1,9, 10, 11, 12, 14, 15, 6}]) == [-5, 4, 9, "hello world", 11, {5,7,8,3,2,1,9, 10, 11, 12, 14, 15, 6}] , "sort2 3"))
except:
    boolean_lst.append(False)
    print(Fore.RED + "sort test failed")

