def countdown(number) -> bool: 

    # base case number equals zero
    if number < 1:
        return
    
    print(number)
    countdown(number-1)
    print(number)

countdown(5)