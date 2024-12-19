N = 360  # 30-year fixed rate mortgage, 30 years * 12 monthly payments
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 6.68
while True:
    print("\nMORTGAGE PLANNING CALCULATOR\n============================ ")
    print("\nEnter a value for each of the following items or type 'NA' if unknown \n")
    location = input("\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)?")
    if location == 'Seattle':
        property_tax_rate = SEATTLE_PROPERTY_TAX_RATE
        price_per_sq_foot = SEATTLE_PRICE_PER_SQ_FOOT
    elif location == 'San Francisco':
        property_tax_rate = SAN_FRANCISCO_PROPERTY_TAX_RATE
        price_per_sq_foot = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
    elif location == 'Austin':
        property_tax_rate = AUSTIN_PROPERTY_TAX_RATE
        price_per_sq_foot = AUSTIN_PRICE_PER_SQ_FOOT
    elif location == 'East Lansing':
        property_tax_rate = EAST_LANSING_PROPERTY_TAX_RATE
        price_per_sq_foot = EAST_LANSING_PRICE_PER_SQ_FOOT
    else:
        property_tax_rate = AVERAGE_NATIONAL_PROPERTY_TAX_RATE
        price_per_sq_foot = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT

    square_footage = input("\nWhat is the maximum square footage you are considering?")
    MAX_MONTHLY_PAYMENT = input("\nWhat is the maximum monthly payment you can afford?")
    DOWN_PAYMENT = input("\nHow much money can you put down as a down payment?")
    APR = input("\nWhat is the current annual percentage rate?")
    if location != "Seattle" and location != "San Francisco" and location != "Austin" and location != "East Lansing":
        print("\nUnknown location. Using national averages for price per square foot and tax rate.")


    if MAX_MONTHLY_PAYMENT == "NA" and APR == "NA" and square_footage != "NA":
        square_footage = float(square_footage)
        DOWN_PAYMENT = float(DOWN_PAYMENT)
        home_cost = square_footage * price_per_sq_foot
        APR = float(APR_2023)
        property_tax = home_cost * property_tax_rate
        monthly_taxes = property_tax / 12
        principal_amount = home_cost - DOWN_PAYMENT
        Interest = APR_2023 / 1200
        a = (1 + Interest) ** N
        monthly_payment = (principal_amount * Interest * a) / (a - 1)
        total = monthly_payment + monthly_taxes
        final_square_footage = square_footage
        print(f"\n\nIn {location}, an average {final_square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}")
        print(f"A 30-year fixed rate mortgage with a down payment of ${DOWN_PAYMENT:,.0f} at {APR:,.1f}% APR results")
        print(
            f"\tin an expected monthly payment of ${monthly_taxes:,.2f} (taxes) + ${monthly_payment:,.2f} (mortgage payment) = ${total:,.2f}")
        AMORTIZATION = input("\nWould you like to print the monthly payment schedule (Y or N)?")
        if AMORTIZATION == "Y":
            remaining_loan_amount = principal_amount
            print("\n{}|{}|{}|{}".format("Month".center(7), "Interest".center(12), "Payment".center(13),
                                         "Balance".center(14)))
            print("=" * 48)
            for month in range(1, N + 1):
                payment_to_interest = (remaining_loan_amount * APR) / 1200
                payment_to_loan = monthly_payment - payment_to_interest
                print(
                    f"{month:^7.0f}| $  {payment_to_interest:>,.2f} | $  {payment_to_loan:>,.2f} | $  {remaining_loan_amount:,.2f}")
                remaining_loan_amount = remaining_loan_amount - payment_to_loan

    elif square_footage == "NA" and MAX_MONTHLY_PAYMENT != "NA":
        DOWN_PAYMENT = float(DOWN_PAYMENT)
        MAX_MONTHLY_PAYMENT = float(MAX_MONTHLY_PAYMENT)
        square_footage = float(100)
        while True:
            home_cost = square_footage * price_per_sq_foot
            if APR == "NA":
                APR = float(APR_2023)
            else:
                APR = float(APR)
            property_tax = home_cost * property_tax_rate
            monthly_taxes = property_tax / 12
            principal_amount = home_cost - DOWN_PAYMENT
            Interest = APR_2023 / 1200
            a = (1 + Interest) ** N
            monthly_payment = (principal_amount * Interest * a) / (a - 1)
            if MAX_MONTHLY_PAYMENT < (monthly_taxes + monthly_payment):
                square_footage -= 1
                break
            else:
                square_footage += 1
        final_square_footage = square_footage
        home_cost = final_square_footage * price_per_sq_foot
        property_tax = home_cost * property_tax_rate
        monthly_taxes = property_tax / 12
        principal_amount = home_cost - DOWN_PAYMENT
        Interest = APR / 1200
        a = (1 + Interest) ** N
        monthly_payment = (principal_amount * Interest * a) / (a - 1)
        total = monthly_payment + monthly_taxes
        print(
            f"\nIn {location}, a maximum monthly payment of ${MAX_MONTHLY_PAYMENT:,.2f} allows the purchase of a house of {final_square_footage:,.0f} sq. feet for ${home_cost:,.0f} \t assuming a 30-year fixed rate mortgage with a ${DOWN_PAYMENT:,.0f} down payment at {APR:,.1f}% APR.")


    elif square_footage == "NA" and MAX_MONTHLY_PAYMENT == "NA":
        print("\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.")

    else:
        square_footage = float(square_footage)
        DOWN_PAYMENT = float(DOWN_PAYMENT)
        if APR == "NA":
            APR = float(APR_2023)
        else:
            APR = float(APR)
        home_cost = square_footage * price_per_sq_foot
        property_tax = home_cost * property_tax_rate
        monthly_taxes = property_tax / 12
        principal_amount = home_cost - DOWN_PAYMENT
        Interest = APR / 1200
        a = (1 + Interest) ** N
        monthly_payment = (principal_amount * Interest * a) / (a - 1)
        total = monthly_payment + monthly_taxes
        final_square_footage = square_footage
        if location != "Seattle" and location != "San Francisco" and location != "Austin" and location != "East Lansing":
            print(
                f"\n\nIn the average U.S. housing market, an average {final_square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(
                f"A 30-year fixed rate mortgage with a down payment of ${DOWN_PAYMENT:,.0f} at {APR:,.1f}% APR results")
            print(
                f"\tin an expected monthly payment of ${monthly_taxes:,.2f} (taxes) + ${monthly_payment:,.2f} (mortgage payment) = ${total:,.2f}")
        else:
            print(
                f"\n\nIn {location}, an average {final_square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(
                f"A 30-year fixed rate mortgage with a down payment of ${DOWN_PAYMENT:,.0f} at {APR:,.1f}% APR results")
            print(
                f"\tin an expected monthly payment of ${monthly_taxes:,.2f} (taxes) + ${monthly_payment:,.2f} (mortgage payment) = ${total:,.2f}")
        if MAX_MONTHLY_PAYMENT == "NA":
            pass
        else:
            MAX_MONTHLY_PAYMENT = float(MAX_MONTHLY_PAYMENT)
            if MAX_MONTHLY_PAYMENT < total:
                print(
                    f"Based on your maximum monthly payment of ${MAX_MONTHLY_PAYMENT:,.2f} you cannot afford this house.")
            else:
                print(
                    f"Based on your maximum monthly payment of ${MAX_MONTHLY_PAYMENT:,.2f} you can afford this house.")

        AMORTIZATION = input("\nWould you like to print the monthly payment schedule (Y or N)?")
        if AMORTIZATION == "Y":
            remaining_loan_amount = principal_amount
            print("\n{}|{}|{}|{}".format("Month".center(7), "Interest".center(12), "Payment".center(13),
                                         "Balance".center(14)))
            print("=" * 48)
            for month in range(1, N + 1):
                payment_to_interest = (remaining_loan_amount * APR) / 1200
                payment_to_loan = monthly_payment - payment_to_interest
                print("{a:^7.0f}|${b:>9,.2f}|${c:>10,.2f}|${d:>11,.2f}".format(a=month, b=payment_to_interest,
                                                                               c=payment_to_loan,
                                                                               d=remaining_loan_amount))
                remaining_loan_amount = remaining_loan_amount - payment_to_loan

    j=input("\nWould you like to make another attempt (Y or N)? ")
    if j.upper() == "N":
        break
