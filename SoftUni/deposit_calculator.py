def deposit_calc():
    deposited_sum = float(input("Enter deposit value [100.00 - 10000.00] $: "))
    if 100.00 < deposited_sum > 10000.00:
        print("Invalid deposit value!")
        return()
    term = int(input("Enter deposit term [1-12] months: "))
    if 1 < term > 12:
        print("Invalid term!")
        return()
    annual_interest_rate = float(input("Enter annual interest rate [0.00 - 100.00] %: "))
    if 0.00 < annual_interest_rate > 100.00:
        print("Invalid Annual Interest rate!")
        return()
    return_sum = deposited_sum + term*((deposited_sum * annual_interest_rate)/12)
    print(f"End deposit value: {return_sum}$ for {term} months with {annual_interest_rate}% Annual rate!")
deposit_calc()