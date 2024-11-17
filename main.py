import numpy_financial as npf
import numpy as np

def payments_remaining(int_rate,payment,princ):
	return np.ceil(npf.nper(int_rate/12,payment,princ))

def calc_total_interest(int_rate,payment_periods,princ):
	pay_per = np.arange(payment_periods)+1
	return sum(npf.ipmt(int_rate/12,pay_per,payment_periods,princ))

def calc_loan_info(princ,int_rate,payment):
	periods_remaining = payments_remaining(int_rate,payment,princ)
	interest_remaining = calc_total_interest(int_rate,periods_remaining,princ)
	return [periods_remaining, interest_remaining]

principal = 10182
current_interest_rate = 0.0375
print(calc_loan_info(principal, current_interest_rate, -400),current_interest_rate)

for interest in np.arange(0.018,0.025,0.003):
	print(calc_loan_info(principal, interest,-400),interest)
