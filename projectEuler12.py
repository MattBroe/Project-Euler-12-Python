#Project Euler 12
#Matt Broe

#Prompt: Find the least triangular number with more than 500 divisors.

#The solution iteratively fills a dictionary that maps each positive integer n
#to its number of divisors, d(n).

#It relies on the fact that d(a*b) = d(a)d(b) when gcd(a, b) = 1. To find
#d(n(n+1)/2), it suffices to find d(n) and d((n+1)/2) (or d(n/2) and d(n+1),
#if n is even), since the factors n and (n+1)/2 are coprime. It also
#uses the expression of d(n) in terms of the prime factorization of n: d(n) =
#product of (a_i + 1), where a_i is the highest power of the i_th prime
#that divides n.


primeList = [2]
numDivisorDict = {1:1, 2:2}

#numDivisors(n, primeList) fills in numDivisorDict[n] with the value of d(n).
#The primeList must contain all the primes less than n for the function to
#work properly.

def numDivisors(n, primeList):
    originalValue = n
    currentNumDivisors = 1
    
    for p in primeList:
        #Find the highest power of p dividing n, and use it to compute d(n)
        power = 0
        while n % p == 0:
            n = n//p
            power += 1
        currentNumDivisors *= (power + 1)

    if currentNumDivisors == 1:
        #meaning n is prime
        currentNumDivisors = 2
        primeList += [n]
    
    numDivisorDict[originalValue] = currentNumDivisors

x = 2

while True:
    x += 1
    numDivisors(x, primeList)
    if x%2 == 0:
        a = numDivisorDict[x//2]
        b = numDivisorDict[x-1]
    else:
        a = numDivisorDict[x]
        b = numDivisorDict[(x-1)//2]
    if a*b > 500:
        print("The least triangular number with more than 500 divisors is ({}*{})/2 = {}.".format(str(x-1), str(x), str(((x-1)*x)//2)))
        break
    

    
            
    
