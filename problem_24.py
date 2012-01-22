import itertools

numbers = [0,1,2,3,4,5,6,7,8,9]

permutations_list = list(itertools.permutations(numbers))
permutations_list.sort()

print permutations_list[999999]

