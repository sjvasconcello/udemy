# librarys
# %%
import matplotlib.pyplot as plt


# %%
class ZeroCouponBonds:

	def __init__(self, principal, maturity, interest_rate):      
		# Principal amount
		self.principal = principal 
		# Date of maturity
		self.maturity = maturity
		# Market interest rate (discounting rate)
		self.interest_rate = interest_rate

	def __repr__(self):
		return f"ZeroCouponBonds({self.principal}, {self.maturity}, {self.interest_rate})"

	def present_value(self, x, n):
		return x / (1 + self.interest_rate)**n
	
	def calculate_price(self):
		return round(self.present_value(self.principal, self.maturity), 4)
	
	def __str__(self) -> str:
		return f'Price in present value: {self.calculate_price()}'

# %%
class CouponBond:

	def __init__(self, principal, rate, maturity, interest_rate):      
		# Principal amount
		self.principal = principal 
		# Date of maturity
		self.maturity = maturity
		# Rate of the bond
		self.rate = rate
		# Market interest rate (discounting rate)
		self.interest_rate = interest_rate

		self.payments = []

	def present_value(self, x, n):
		return x / (1 + self.interest_rate)**n
	
	def calculate_price(self):
		# Discount the coupon payments

		for t in range(1, self.maturity+1):
			payment = self.present_value(self.principal * self.rate, t)
			self.payments.append(payment)

		# Discount principle amount
		price = self.present_value(self.principal, self.maturity)
		self.payments.append(price)

		return sum(self.payments)

	def __str__(self) -> str:
		return f'Price in present value: {self.calculate_price()}'


# %%
bond = CouponBond(1000, 0.1, 7, 0.04)
#bond
# %%
print(bond)
print(bond.payments)

# %%
# Create a list of years (from 1 to maturity)
years = list(range(1, bond.maturity + 1))


# %%  
# Plot the bond payments 
plt.bar(years, bond.payments, label='Bond Payments')
plt.xlabel('Year')
plt.ylabel('Payment Value')
plt.title('Bond Payments Over Time')
plt.legend()
plt.plot()
for a,b in zip(years, bond.payments): 
    plt.text(a, b, str(b))
plt.show()
# %%
