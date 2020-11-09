has_high_income = True
has_good_credit = False
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

elif has_high_income and has_criminal_record:
    print("He/she is Criminal")

elif has_good_credit and not has_criminal_record:
    print("Eligible for loan")

else:
    print("Not eligible for loan")