import polars as pl
import math
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict

@dataclass
class RefinanceOption:
    new_loan_amount: float
    new_annual_interest_rate: float
    new_term_years: int
    associated_costs: float

    def calculate_new_payment(self) -> float:
        monthly_interest_rate = self.new_annual_interest_rate / 12 / 100
        number_of_payments = self.new_term_years * 12
        if monthly_interest_rate > 0:
            return (self.new_loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        else:
            return self.new_loan_amount / number_of_payments

@dataclass
class Mortgage:
    principal: float
    annual_interest_rate: float
    term_years: int
    start_date: str = None
    extra_principal_payment: float = 0

    def __post_init__(self):
        self.calculate_monthly_payment()

    def calculate_monthly_payment(self) -> float:
        monthly_interest_rate = self.annual_interest_rate / 12 / 100
        number_of_payments = self.term_years * 12
        if monthly_interest_rate > 0:
            self.monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        else:
            self.monthly_payment = self.principal / number_of_payments
        return self.monthly_payment

    def generate_amortization_schedule(self) -> pl.DataFrame:
        schedule = []
        principal_remaining = self.principal
        monthly_interest_rate = self.annual_interest_rate / 12 / 100
        payment = self.monthly_payment
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d')

        for i in range(1, self.term_years * 12 + 1):
            interest_payment = principal_remaining * monthly_interest_rate
            principal_payment = payment - interest_payment
            principal_remaining -= principal_payment
            payment_date = start_date + timedelta(days=30 * i)
            schedule.append({
                'payment_number': i,
                'payment_date': payment_date.strftime('%Y-%m-%d'),
                'payment': payment,
                'interest_payment': interest_payment,
                'principal_payment': principal_payment,
                'principal_remaining': max(principal_remaining, 0),
            })

        return pl.DataFrame(schedule)
    
    def calculate_principal_only_payment(self) -> Dict[str, float]:
        monthly_interest_rate = self.annual_interest_rate / 12 / 100
        number_of_payments = self.term_years * 12
        total_payment = self.monthly_payment + self.extra_principal_payment

        if monthly_interest_rate > 0:
            new_term_months = math.log((total_payment / (total_payment - self.principal * monthly_interest_rate))) / math.log(1 + monthly_interest_rate)
        else:
            new_term_months = self.principal / total_payment

        new_term_years = new_term_months / 12
        time_saved_years = self.term_years - new_term_years

        # Generate the amortization schedule
        schedule = []
        principal_remaining = self.principal
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d')

        for i in range(1, int(new_term_months) + 1):
            interest_payment = principal_remaining * monthly_interest_rate
            principal_payment = total_payment - interest_payment
            principal_remaining -= principal_payment
            payment_date = start_date + timedelta(days=30 * i)
            schedule.append({
                'payment_number': i,
                'payment_date': payment_date.strftime('%Y-%m-%d'),
                'payment': total_payment,
                'interest_payment': interest_payment,
                'principal_payment': principal_payment,
                'principal_remaining': max(principal_remaining, 0),
            })

        return new_term_months, time_saved_years,schedule


    def refinance_assessment(self, refinance_option: RefinanceOption, break_even_threshold=36) -> Dict[str, float]:
        new_payment = refinance_option.calculate_new_payment()
        monthly_savings = self.monthly_payment - new_payment
        break_even_point = refinance_option.associated_costs / monthly_savings if monthly_savings > 0 else float('inf')
        total_savings = (self.term_years * 12 * self.monthly_payment) - ((refinance_option.new_term_years * 12 * new_payment) + refinance_option.associated_costs)
        should_refinance = break_even_point < break_even_threshold and total_savings > 0
        
        return {
            "Old Monthly Payment": self.monthly_payment,
            "New Monthly Payment": new_payment,
            "Monthly Savings": monthly_savings,
            "Break-Even Point (months)": break_even_point,
            "Total Savings (over the loan term)": total_savings,
            "Should Refinance": should_refinance
        }
