s = "Hey there! What should this string be?"

print(s)
print ("Length of s = %d " % len(s))
print ("The first occurrence of the letter 'a' = %d" % s.index("a"))
print ("'e' occur %d time." % s.count("e"))
print ("The first six characters are '%s'." % s[:6])
print ("The next five characters are '%s'." % s[5:10])
print ("The thirteenth character is '%s'." % s[12])
print ("The characters  with odd index  are '%s'." % s[1::2])
print ("The last five character are '%s'." % s[-5:])
print ("String in upperclass: %s" % s.upper())
print ("String in lowerclass: %s" % s.lower())

if s.startswith("Lol"):
    print ("String start with 'Hey'. Good!")

else:
    print ("String start with other. Bad!")

if s.endswith("be?"):
    print ("String with 'be?'. Good!")

else:
    print ("String start with other. Bad!")

print ("Split the words of String: %s" % s.split(" "))
