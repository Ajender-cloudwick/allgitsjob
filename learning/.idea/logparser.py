def mydict():
    f=open('/Users/AjenderNeelam/logfile')
    lines=f.readlines()
    mydict = {}
    mydict1 = {}
    for line in lines:
        word = line.split()[0]
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1
    for line in lines:
        word = line.split()[0]
        word1 = line.split()[3]
        word2 = word +" "+ word1
        if word2 in mydict1:
            mydict1[word2] += 1
        else:
            mydict1[word2] = 1
    print mydict1

l = [[0, 2, 'f'], [4, 1, 't'], [9, 4, 'afsd']]
print l
for i in range(0,len(l)-1):
    if l[i][1] > l[i+1][1]:
        temp = l[i+1]
        l[i+1]= l[i]
        l[i]=temp

print l
