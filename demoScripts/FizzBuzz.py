
# Put start and end points in variables so that they can be arbitrarily changed
start = 1
end = 100

for i in range(start, end):
    value = ""
    number = True

    if i % 3 == 0:
        value = "fizz"
        number = False

    if i % 5 == 0:
        value += "buzz"
    elif number:
        value = i

    print value
