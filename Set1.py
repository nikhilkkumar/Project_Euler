#Problem 1
def fizzBuzz(n):
    # FizzBuzz
    # for i in range(1, n+1):
    #     if i%3 == 0 and i%5 == 0:
    #         print("FizzBuzz")
    #     elif i%3 == 0:
    #         print("Fizz")
    #     elif i%5 == 0:
    #         print("Buzz")
    #     else :
    #         print(i)
    sum = 0
    for i in range(1, n+1):
        if i%3 == 0 or i%5 == 0:
            sum += i

    return sum

#Problem 2
def fib2(n1, n2, n):
    temp = n1 + n2
    n1 = n2 #2nd # -> 1st #
    n2 = temp #new number
    print(temp)
    # if temp % 2 ==0:
    #     print(temp)
    if n == 1:
        return
    n-=1
    fib2(n1, n2, n)
def fib(n):
    if n == 2:
        print(1)
        print(2)
    if n == 1:
        print(1)
    elif n <= 0:
        print("Incorrect input")
    print(1)
    print(2)
    fib2(1, 2, n)

#Problem 3
def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n/2)+1) :
        if n%i == 0 :
            return False
        
    return True
def findFactors(n):
    factors = []
    for i in range(2, int(n/2)+1) :
        if n%i == 0 :
            factors.append(i)
    
    return factors
def largestPrimeFactor(n):
    factors = findFactors(n)
    primeFactors = []

    for i in factors :
        if isPrime(i) == True :
            primeFactors.append(i)
    
    if len(primeFactors) < 1:
        return 
    return primeFactors[len(primeFactors)-1]

#Problem 4
def isPalindrome(x):
    for i in range(0, int(len(x)/2), 1):
        if x[i] == x[len(x)-i-1] :
            continue
        else :
            return False
    
    return True
def palindromicProduct():
    max = 0
    for i in range(999, 100, -1):
        for r in range(999, 100, -1):
            product = i*r
            p = str(product)
            if isPalindrome(p) == True :
                if product > max :
                    max = product
                    n1 = i
                    n2 = r
    
    return max, n1, n2

print(palindromicProduct())