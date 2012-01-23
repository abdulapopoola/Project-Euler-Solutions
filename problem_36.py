def isPalindrome(no_as_list):
    tmp = no_as_list[:]
    no_as_list.reverse()
    return tmp == no_as_list

sums = 0
for i in xrange(1,1000000):
    binary = bin(i).split('b')[1]
    decimal_no_as_str = str(i)
    bin_list = [j for j in binary]
    decimal_list = [k for k in decimal_no_as_str]
    if isPalindrome(bin_list) and isPalindrome(decimal_list):
        sums = sums + i

print sums
    
