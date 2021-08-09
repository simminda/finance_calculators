import math

# setup opening screen and prompt user to select a calculator. Store selection in a variable
print("\nChoose either 'investment' or 'bond' from the menu below to proceed: ")
print("\ninvestment     - to calculate the amount of interest you'll earn on an investment")
print("bond           - to calculate the amount you'll have to pay on a home loan")
selector = input("\nEnter text here -> ").lower()                       # force input selection to always be recognized as one case (lower) for user convenience

# evaluate user input and launch applicable calculator or error message
if selector == "investment":
    principal   = float(input("\nEnter deposit amount e.g. '10000'\t\t: "))                 # Request input and cast to float to use in calculations
    
    rate        = float(input("Enter annual interest rate e.g. '10'\t\t: "))

    period      = float(input("Enter investment duration (years) e.g. '5'\t: "))

    interest    = input("Enter whether you want 'simple' or 'compound' interest:\t").lower()# Request selection input. Force lower case. Evaluate selection and launch applicable calculation
    if interest == "simple":
        amount = round(principal * (1+ (rate/100*period)),2)            # Simple interest formula: A = P(1+r * t)

        print(f"\nDeposit\t\t: R{principal}")                           # print output feedback based on user input. Round up and format accordingly for readability
        print(f"\nInterest Rate\t: {rate} %")
        print(f"\nInvestment Term\t: {period} Years")
        print(f"\nInterest Earned\t: R{(amount-principal):,}")
        print(f"\nClosing Balance\t: R{amount:,}\n")

    elif interest == "compound":
        amount = round(principal*math.pow((1+rate/100),period),2)       # Compound interest formula: A = P* math.pow((1+r),t)
        
        print(f"\nDeposit\t\t: R{principal}")                           # print output feedback based on user input. Round up and format accordingly for readability
        print(f"\nInterest Rate\t: {rate} %")
        print(f"\nInvestment Term\t: {period} Years")
        print(f"\nInterest Earned\t: R{(amount-principal):,}")
        print(f"\nClosing Balance\t: R{amount:,}\n")

    elif interest != "simple" or interest != "compound":                # Print error message for Invalid entry made
        print("\nYou have made an invalid entry '{}'. Please restart the program and enter either 'simple' or 'compound' for interest type.")


elif selector == "bond":
    house_price  = float(input("Enter the price of the house e.g. '500000'\t: "))

    int_rate     = (float(input("Enter the interest rate e.g. '7'\t\t: ")))/12/100    # manupulate int to monthly (/12) & number format (/100) as opposed to percantage to use in calculation 
    
    payment_term = (float(input("Enter payment term (years) e.g. '20'\t\t: ")))*12    # multiply by 12/convert to months to save user from doing a separate calculation
    
    repayment    = round(house_price * (int_rate * (1 + int_rate) ** payment_term)/ ((1+ int_rate) ** payment_term -1), 2) # formula: x = L * ((I * ((1+I) ** n)) / ((1+I) ** n - 1))
    
    
    print(f"\nBond\t\t\t: R{round(house_price):,}")                     # print output feedback based on user input. Round up and format accordingly for readability                   
    print(f"\nInterest rate\t\t: {round(int_rate*12*100)} %")
    print(f"\nPayment Term\t\t: {payment_term/12} Years")
    print(f"\nMonthly Repayment\t: R{repayment:,}\n")


elif selector != "investment" or selector == "bond":
    print(f"\n{selector} is an invalid selection. Please enter either 'investment' or 'bond' to choose a calculator.")

