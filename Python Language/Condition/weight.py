weight = int(input("Weight: "))
unit = input ("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print("You are "+str(converted)+" kilos")

else:
    converted = weight / 0.45
    print("you are "+str(converted)+" pounds")
