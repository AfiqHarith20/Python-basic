x = object()
y = object()

x_list = [x] * 5
y_list = [y] * 2
big_list = x_list + y_list

print ("x_list contains %d objects" % len(x_list))
print ("y_list contains %d objects" % len(y_list))
print ("big_list contains %d objects" % len(big_list))

if x_list.count(x) <= 8 and y_list.count(y) <= 6:
    print ("Almost there.....")

if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
