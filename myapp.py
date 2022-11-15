import math
def numerical_integration(lower, upper) :
    result=[]
    
    N=[10, 100, 100, 1000, 10000, 100000, 1000000]
        
    for num in N:
        x=lower
        total=0
        dx = abs(upper-lower)/num
        
        while x <= upper:
            total+=abs(math.sin(x))*dx
            x=x+dx
        result.append(total)
        
    
    print(result)
    return result

