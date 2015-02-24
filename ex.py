from sys import argv
from math import sqrt

# I am doing this because I have a class
# about this topic. So, I need to practice
# for exams and I need to practice python.

# I really don't care about the class. Learn
# python is more important. :)

# Enjoy sums
def sum_n(n):
    return n*(n+1)//2

# Exercise 1
# To run: python euler-ex.py 1
def ex1():
    upper_bound = 999
    sum = 3*sum_n(upper_bound//3) + \
          5*sum_n(upper_bound//5) - \
          15*sum_n(upper_bound//15)
    print(sum)

# Exercise 2
# To run: python euler-ex.py 2
def ex2():
    total = 0
    last, before, twice_before = 1, 0, 0
    while last < 4000000:
        twice_before, before, last = before, last, last+before
        if not (last&1):
            total += last
    print(total)

def erathostenes(n):
    l = [i for i in range(n+1)]
    ret = list()
    for i in range(2, n):
        if l[i] == -1:
            continue
        ret.append(i)
        l[i::i] = [-1] * (n//i)
    return ret

# Exercise 3
# To run: python euler-ex.py 3
def ex3():
    n = 600851475143
    primes = erathostenes(int(sqrt(n)))
    for prime in reversed(primes):
        if n%prime == 0:
            print(prime)
            break

# Exercise 4
# To run: python euler-ex.py 4
def ex4():
    max = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            tmp = i*j
            if tmp > max and str(tmp) == str(tmp)[::-1]:
                max = tmp
    print(max)

# Exercise 5
# To run: python euler-ex.py 5
def ex5():
    print(2*2*2*2*3*3*5*7*11*13*17*19)

# Sum of squares defined here.
# Why classes are not simple as code?
def sum_squares(n):
    return n*(n+1)*(2*n+1)//6

# Exercise 6
# To run: python euler-ex.py 6
def ex6():
    n = 10
    print(sum_n(n)**2 - sum_squares(n))

# Exercise 7
# To run: python euler-ex.py 7
def ex7():
    n = 10000
    l = list()
    while len(l) < 10001:
        n *= 2
        l = erathostenes(n)
        print(n)
    print(l[10000])

# Exercise 8
# To run: python euler-ex.py 8
def ex8():
    max = 0
    # I love this one :)
    # Easy to remember.
    n = "73167176531330624919225119674426574742355349194934" \
        "96983520312774506326239578318016984801869478851843" \
        "85861560789112949495459501737958331952853208805511" \
        "12540698747158523863050715693290963295227443043557" \
        "66896648950445244523161731856403098711121722383113" \
        "62229893423380308135336276614282806444486645238749" \
        "30358907296290491560440772390713810515859307960866" \
        "70172427121883998797908792274921901699720888093776" \
        "65727333001053367881220235421809751254540594752243" \
        "52584907711670556013604839586446706324415722155397" \
        "53697817977846174064955149290862569321978468622482" \
        "83972241375657056057490261407972968652414535100474" \
        "82166370484403199890008895243450658541227588666881" \
        "16427171479924442928230863465674813919123162824586" \
        "17866458359124566529476545682848912883142607690042" \
        "24219022671055626321111109370544217506941658960408" \
        "07198403850962455444362981230987879927244284909188" \
        "84580156166097919133875499200524063689912560717606" \
        "05886116467109405077541002256983155200055935729725" \
        "71636269561882670428252483600823257530420752963450"
    for i in range(len(n)-13):
        mult = 1
        for k in range(13):
            mult *= int(n[i+k])
        if mult > max:
            max = mult
    print(max)

# Exercise 9
# To run: python euler-ex.py 9
def ex9():
    max = 0
    for i in range(1000):
        for j in range(1000-i):
            k = 1000-i-j
            if i*i + j*j == k*k and i*j*k > max:
                max = i*j*k
    print(max)

# Exercise 10
# To run: python euler-ex.py 10
def ex10():
    print(sum(erathostenes(2000000)))

if __name__ == "__main__":
    if len(argv) != 2:
        # Check comments to know how to run every exercise.
        print("Error: you must precise the exercise (ex : python3 {} 1)" \
              .format(argv[0]))
    else:
        # Yay!
        print("executing exercise {} :".format(argv[1]))
        exec("ex{}()".format(argv[1]))
