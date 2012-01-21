letters = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def alphabetical_value(word):
    return sum(letters.get(char.lower()) for char in word)

names = open('names.txt').read().replace('"','').split(',')
names.sort()

print sum(((i+1) * alphabetical_value(names[i])) for i in xrange(0,len(names)))


