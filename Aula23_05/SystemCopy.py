def getValue():
    return(input('Digite a quantidade de cópias: '))

def firstCost(copies):
    return (0.1 * copies)

def secondCost(copies):
    return (0.08 * copies)

def thirdCost(copies):
    return (0.06 * copies)

def fourthCost(copies):
    return (0.04 * copies)

def treatValue(copies):
    if(copies <= 2):
        return firstCost(copies)
    elif(2 < copies <= 10):
        return secondCost(copies)
    elif (10 < copies <= 100):
        return thirdCost(copies)
    else:
        return fourthCost(copies)

if __name__ == '__main__':
    copies = int(getValue())
    if(0 > copies):
        print('Não é possível fazer cópias negativas')
    else:
        print('As cópias sairão: ',treatValue(copies))


