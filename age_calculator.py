from datetime import datetime

# Age Calculator Project - My First Python Program
print("=== AGE CALCULATOR ===")
print("Enter your date of birth")

# Get user input
birth_year = int(input("Enter your birth year (e.g., 2003): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

# Get today's date
today = datetime.now()

# Calculate age
age_years = today.year - birth_year
age_months = today.month - birth_month
age_days = today.day - birth_day

# Adjust for negative months/days
if age_days < 0:
    age_months -= 1
    age_days += 30  # Approximate

if age_months < 0:
    age_years -= 1
    age_months += 12

# Display results
print(f"\n🎉 You are {age_years} years, {age_months} months, and {age_days} days old!")
print(f"Total days alive: {(today - datetime(birth_year, birth_month, birth_day)).days}")
print("Perfect time to start, neither late nor early!")