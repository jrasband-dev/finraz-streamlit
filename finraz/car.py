def new_or_used(
    new_car_price, 
    new_car_interest_rate,
    new_car_loan_term_years,
    used_car_price, 
    used_car_interest_rate, 
    used_car_loan_term_years,
    used_car_mileage, 
    used_car_msrp,
    annual_mileage=12000, 
    total_lifespan_miles=180000,
    new_car_downpayment=0, 
    used_car_downpayment=0
):
    """
    Compare the cost of a new car vs. a used car, factoring in loan terms, interest rates,
    annual mileage, and optional downpayments.

    Parameters:
    - new_car_price (float): Price of the new car.
    - new_car_interest_rate (float): Annual interest rate for the new car loan (e.g., 0.025 for 2.5%).
    - new_car_loan_term_years (int): Loan term in years for the new car.
    - used_car_price (float): Price of the used car.
    - used_car_interest_rate (float): Annual interest rate for the used car loan (e.g., 0.06 for 6%).
    - used_car_loan_term_years (int): Loan term in years for the used car.
    - used_car_mileage (int): Mileage of the used car.
    - annual_mileage (float): Annual miles driven.
    - total_lifespan_miles (float): Total expected lifespan of a car in miles.
    - new_car_downpayment (float, optional): Downpayment for the new car. Default is 0.
    - used_car_downpayment (float, optional): Downpayment for the used car. Default is 0.

    Returns:
    A dictionary with the monthly payments, total cost, total interest paid, and effective cost per year for both cars.
    """
    # Helper function to calculate monthly loan payments
    def calculate_monthly_payment(principal, annual_rate, years):
        # Convert annual rate to monthly rate in decimal form
        monthly_rate = (annual_rate / 100) / 12
        num_payments = years * 12
        # Calculate monthly payment using the loan formula
        return principal * (monthly_rate / (1 - (1 + monthly_rate) ** -num_payments))

    # Adjust principal amounts for downpayments
    new_car_loan_amount = new_car_price - new_car_downpayment
    used_car_loan_amount = used_car_price - used_car_downpayment

    # Calculate monthly payments for each car
    new_car_monthly_payment = calculate_monthly_payment(new_car_loan_amount, new_car_interest_rate, new_car_loan_term_years)
    used_car_monthly_payment = calculate_monthly_payment(used_car_loan_amount, used_car_interest_rate, used_car_loan_term_years)

    # Calculate remaining lifespan of the used car
    remaining_miles_used_car = total_lifespan_miles - used_car_mileage
    remaining_years_used_car = remaining_miles_used_car / annual_mileage

    # Calculate remaining lifespan of new car
    remaining_miles_new_car = total_lifespan_miles
    remaining_years_new_car = remaining_miles_new_car / annual_mileage

    # calculate estimated cost per mile for new car
    estimated_cost_per_mile_new_car = new_car_price / total_lifespan_miles

    # Calculate expected MSRP discount for used car
    estimated_cost_per_mile = used_car_msrp / total_lifespan_miles
    mileage_based_price = estimated_cost_per_mile * remaining_miles_used_car
    premium_or_discount = used_car_price - mileage_based_price

    # Calculate total cost over loan term
    new_car_total_cost = new_car_monthly_payment * new_car_loan_term_years * 12
    used_car_total_cost = used_car_monthly_payment * used_car_loan_term_years * 12

    # Calculate total interest paid
    new_car_total_interest = new_car_total_cost - new_car_loan_amount
    used_car_total_interest = used_car_total_cost - used_car_loan_amount

    # Calculate effective cost per year of ownership
    new_car_cost_per_year = new_car_total_cost / (total_lifespan_miles / annual_mileage)
    used_car_cost_per_year = used_car_total_cost / remaining_years_used_car

    # Return results
    return {
        "new_car": {
            "cost_per_year": round(new_car_cost_per_year, 2),
            "remaining_miles": remaining_miles_new_car,
            "remaining_years": round(remaining_years_new_car, 2),
            "new_car_price": new_car_price,
            "total_cost": round(new_car_total_cost, 2),
            "monthly_payment": round(new_car_monthly_payment, 2),
            "principal": new_car_loan_amount,
            "interest": round(new_car_total_interest, 2),
            "cost_per_mile": round(estimated_cost_per_mile_new_car, 2),
        },
        "used_car": {
            "cost_per_year": round(used_car_cost_per_year, 2),
            "remaining_miles": remaining_miles_used_car,
            "remaining_years": round(remaining_years_used_car, 2),
            "used_car_price": used_car_price,
            "mileage_based_price": round(mileage_based_price, 2),
            "premium_or_discount": round(premium_or_discount, 2),
            "total_cost": round(used_car_total_cost, 2), 
            "monthly_payment": round(used_car_monthly_payment, 2),
            "principal": round(used_car_loan_amount,2),
            "interest": round(used_car_total_interest, 2),
            "cost_per_mile": round(estimated_cost_per_mile, 2),  
        }
    }
