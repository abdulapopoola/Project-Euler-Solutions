nums = open('100_rows_triangle_problem', 'r')

arry = []
for line in nums:
    arry.append(line)

for i in xrange(0,len(arry)):
    arry[i] =  [int(y) for x in arry[i].split('\n') for y in x.split()]

sums = arry[1]

#update first row below the peak of the triangle
for x in xrange(0,len(sums)):
    sums[x] += arry[0][0]

for i in xrange(2,len(arry)): #start from the third row as the first two have been handled
    tmp = arry[i]
    tmp_sum = sums[:] #copy of sums to avoid overwriting the sums leading to erros
    tmp_sum[0] = sums[0] + tmp[0]
    new_last = sums[-1] + tmp[-1]
    tmp_sum.append(new_last)
    for j in xrange(1,len(tmp)-1): #start comparing from the second element of this row up to the element before the last
       tmp_sum[j] = max(sums[(j-1):j+1]) + tmp[j]  
    sums = tmp_sum
 
print max(sums)

