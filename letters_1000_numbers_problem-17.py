'''
The way the program works
'''

letters ={1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13:8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8}

sums = 0

for i in xrange(1,1001):
    if i == 1000:
        sums = sums + 11 #length of chars in one thousand
    
    hundreds_value = i/100 #append the value for hundreds
    rem = i%100   #get the remainder after removing hundred
    tens_value = rem/10
    unit_value = rem%10

    if(hundreds_value > 0):
        sums = sums + letters.get(hundreds_value)+ letters.get(100) + 3 #The three is the length of and
    if(tens_value > 0):
        sums = sums + letters.get((tens_value*10))
    if(unit_value > 0):
        sums = sums + letters.get(unit_value)

print sums

