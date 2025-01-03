def is_prime(n: int) -> bool: 

    # base case 
    if n == 0 or n == 1:
        return False

    # base case
    if n == 2: 
        return True 
    
    if n > 2: 
        for number in range(2,n):
            if n % number == 0: 
                return False
        
    return True # Only reaches this line if NONE of the above returns happened


print(is_prime(6))