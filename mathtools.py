import numpy as np

def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    elif x == 3:
        return True
    elif x % 2 == 0:
        return False
    elif x % 3 == 0:
        return False
    elif x < 9:
        return True
    elif not x % 6 == 5 and not x % 6 == 1:
        return False
    else:
        biggest_possible_factor = int(np.floor(np.sqrt(x)))
        check = 5
        while check <= biggest_possible_factor:
            if x % check == 0 or x % (check+2) == 0:
                return False
            check += 1
        return True

def factors(num):
    import numpy as np
    max_probe = int(np.floor(np.sqrt(num)))
    fcts = set()
    for probe in range(max_probe):
        probe += 1
        if num % probe == 0:
            fcts.add(probe)
            fcts.add(int(num/probe))
    return fcts

def is_relatively_prime(n1, n2):
    return len(factors(n1).intersection(factors(n2))) == 1

def eulers_totient(n):
    #find factors of n
    target_facs = factors(n)
    target_facs.remove(1)
    
    #if n is prime, totient is n-1
    if len(target_facs) == 1:
        return n-1

    #otherwise, need to use brute force
    #sieve with factors of n to identify numbers that are not relatively prime with n
    notrp = []
    for f in target_facs:
        # don't need to check nonprime factors
        if any([f % otherfac == 0 and not f == otherfac for otherfac in target_facs]):
            continue 
        notrp.append([x for x in range(f, n, f)])
    return n-1 - len(set([x for sub in notrp for x in sub]))