def is_prime(n: int) -> bool: 

    if n == 0 or n == 1:
        return False

    if n == 2: 
        return True 
    
    # only check up to square root of n
    if n > 2: 
        for number in range(2, int(n ** 0.5) + 1):
            if n % number == 0: 
                return False
        
    return True # Only reaches this line if NONE of the above returns happened


print(is_prime(100))