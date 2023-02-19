def gcd(num1, num2):
    maximum, minimum = max(num1,num2), min(num1,num2)
    if maximum%minimum == 0:
        return minimum
    else:
        return gcd(minimum, maximum%minimum)

print(gcd(25,13)) # Output: 1
print(gcd(13,26)) # Output: 13
print(gcd(6,15))  # Output: 3


''' Euclids algorithm :

-> Useful for finding GCD of a number

-> Takes time proportional to number of digits

-> Proof:
    Let us take 2 numbers m and n. We have to find the gcd of these two numbers
    Consider n does not divide m perfectly
    -> m = quotient(n) + remainder (dividend = divisor*quotient + remainder) -- (i)

    Now a number 'd' divides both m and n
    -> m = (const c1)*d and n = (const c2)*d -- (ii)

    Substituting the values of equation (ii) in equation (i)
    c1*d = quotient*(c2*d) + remainder -- (iii)

    Since LHS is a factor of d.
    For equation (iii) to hold true RHS should also be a factor of d
    
    RHS consists of 2 terms -> term 1: quotient*(c2*d) which is already a factor of d
                               term 2: remainder
    So now remainder should be a factor of d i.e remainder = (const c3)*d

    In short m%n also has a factor of d
'''