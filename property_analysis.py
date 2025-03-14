import numpy as np

# Define Property Criteria
def analyze_property(property):
    # Core Criteria
    location_factors = property.get('location_factors')
    property_type = property.get('property_type')
    financials = property.get('financials')
    
    # Analysis Variables
    arvs = property.get('arvs')  # After Repair Values (ARVs)
    repair_costs = property.get('repair_costs')
    rent_income = property.get('rent_income')
    expenses = property.get('expenses')
    
    # Core Criteria Analysis
    if location_factors['rental_demand'] < 3:  # Example condition
        return "Location does not meet high rental demand."
    if location_factors['crime_rate'] > 3:  # Example condition
        return "Location has high crime rate."
    if property_type not in ['single-family', 'multi-family', 'foreclosed']:
        return "Property type is not suitable."

    # Financial Criteria Calculations
    cap_rate = calculate_cap_rate(rent_income, expenses, property['price'])
    cash_on_cash_return = calculate_cash_on_cash_return(rent_income, expenses, property['cash_invested'])
    max_offer_price = calculate_max_offer_price(arvs, repair_costs)
    
    # Decision Making
    if cap_rate < 8:
        return "Cap rate is too low."
    if cash_on_cash_return < 10:
        return "Cash-on-cash return is too low."
    if property['price'] > max_offer_price:
        return "Price exceeds max offer price based on ARV and repairs."
    
    return "Property meets investment criteria."

# Financial Calculations
def calculate_cap_rate(rent_income, expenses, property_value):
    noi = rent_income - expenses
    cap_rate = (noi / property_value) * 100
    return cap_rate

def calculate_cash_on_cash_return(rent_income, expenses, cash_invested):
    annual_cash_flow = rent_income - expenses
    return (annual_cash_flow / cash_invested) * 100

def calculate_max_offer_price(arvs, repair_costs):
    arvs_avg = np.mean(arvs)
    max_price = (arvs_avg * 0.70) - repair_costs
    return max_price

# Example Property Data
property_data = {
    'location_factors': {'rental_demand': 5, 'crime_rate': 2},
    'property_type': 'single-family',
    'price': 200000,
    'arvs': [250000, 240000, 260000],
    'repair_costs': 30000,
    'rent_income': 2000,
    'expenses': 500,
    'cash_invested': 50000,
    'financials': {'cap_rate': 8, 'cash_on_cash_return': 10}
}

# Analyze Property
result = analyze_property(property_data)
print(result)