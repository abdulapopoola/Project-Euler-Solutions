cache = { 1: 1}

def get_sequences(cache, n):
    if cache.get(n,0):#Will return n if true, else returns 0 which is False
        return cache[n]
    else:
        if not (n%2): #number is even
            cache[n] =  1 + get_sequences(cache,(n / 2))
        else:
            cache[n] = 1 + get_sequences(cache,(3*n + 1))
        return cache[n]

no, length = 0, 0
for i in xrange(1,1000000):
    leng = get_sequences(cache,i)
    if leng>length:
        length = leng
        no = i

print no
