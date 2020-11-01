def sum(*dData):
        jum = 0
        for x in dData:
            jum = jum+x
        print(jum)

def average(*dData):
    i = 0
    j = 0
    for x in dData:
        i = i+x
        j+=1
    average = i/j
    print(average)

def max(*dData):
    max = dData[0]
    for i in dData:
        if (i>max):
            max=i
    print(max)

def min(*dData):
    min=dData[0]
    for i in dData:
        if (i<min):
            min=i
    print(min)



