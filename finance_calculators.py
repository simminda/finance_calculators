''' 
A lightweight program with the option of 2 financial calculators: 
Investment or Bond
'''

import math

program_loop = True
while (program_loop):
    # Welcome Screen
    print("\nChoose either 'investment' or 'bond' from the menu below to proceed: ")
    print("\ninvestment     - to calculate the amount of interest you'll earn on an investment")
    print("bond           - to calculate the amount you'll have to pay on a home loan")
    print("exit           - to close the program")

    selector = input("\nEnter text here -> ").lower()   # Defensive handling

    # Evaluate user input and launch applicable calculator or error message
    if selector == "investment":
        principal   = float(input("\nEnter deposit amount e.g. '10000'\t\t: "))                
        rate        = float(input("Enter annual interest rate e.g. '10'\t\t: "))
        period      = float(input("Enter investment duration (years) e.g. '5'\t: "))
        
        # Defensive handling for interest selection
        interest_validator = True
        while (interest_validator) :
            interest    = input("Enter whether you want 'simple' or 'compound' interest:\t").lower()
            if interest == "simple":
                # Simple interest formula: A = P(1+r * t)
                amount = round(principal * (1+ (rate/100 * period)),2)    

                print("\nInvestment Details:")
                print(f"\nDeposit\t\t: R{principal}")                         
                print(f"Interest Rate\t: {rate} %")
                print(f"Investment Term\t: {period} Years")
                print(f"Interest Earned\t: R{(amount-principal):,}") # Round up and format accordingly for readability
                print(f"Closing Balance\t: R{amount:,}\n")
                print("\nThank you for using Calculator\n")

                # Exit inner & outer Loops
                interest_validator = False
                program_loop = False
            elif interest == "compound":
                # Compound interest formula: A = P* math.pow((1+r),t)
                amount = round(principal*math.pow((1 + rate/100),period),2)   
                
                print("\nInvestment Details:")
                print(f"\nDeposit\t\t: R{principal}")                           
                print(f"Interest Rate\t: {rate} %")
                print(f"Investment Term\t: {period} Years")
                print(f"Interest Earned\t: R{(amount-principal):,}")
                print(f"Closing Balance\t: R{amount:,}\n")
                print("\nThank you for using Calculator\n")
                
                interest_validator = False
                program_loop = False
            else:            
                print(f"\nYou have made an invalid entry: '{interest}'.\nPlease enter either 'simple' or 'compound' for interest type.\n")
    elif selector == "bond":
        house_price  = float(input("Enter the price of the house e.g. '500000'\t: "))
        int_rate     = (float(input("Enter the interest rate e.g. '7'\t\t: ")))/12/100    # /12/100  - Convert perc to num and monthly rate
        payment_term = (float(input("Enter payment term (years) e.g. '20'\t\t: ")))*12    
        # formula: x = L * ((I * ((1+I) ** n)) / ((1+I) ** n - 1))
        repayment    = round(house_price * (int_rate * (1 + int_rate) ** payment_term)/ ((1+ int_rate) ** payment_term -1), 2) 
        
        print("\nBond Details:")
        print(f"\nBond\t\t\t: R{round(house_price):,}")                                      
        print(f"Interest rate\t\t: {round(int_rate * 12 * 100)} %")
        print(f"Payment Term\t\t: {payment_term / 12} Years")
        print(f"Monthly Repayment\t: R{repayment:,}\n")
        print("\nThank you for using Calculator\n")

        program_loop = False
    elif selector == "exit":
        print("\nThank you for using Calculator\n")
        exit()
    else:
        print(f"\n{selector} is an invalid selection. Please enter either 'investment' or 'bond' to choose a calculator.\n")


