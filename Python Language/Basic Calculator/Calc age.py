birth_year = int(input("Enter your birth year: "))
weight_in_kilo = int(input("Enter your weight in Kilogram: "))
age = int(2020 - birth_year)
weight_in_pound = float(weight_in_kilo / 0.4535924)

print(str(age)+" years old")
print(str(weight_in_pound)+" pound")
