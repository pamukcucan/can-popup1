import random

def generateNumbers() :
    lis = []
    for i in range(10) :
        
        r = random.randint(1,10)
        if r not in lis :
            lis.append(r)
        i+=1
    return lis


def main() :
    print(generateNumbers())
main()
