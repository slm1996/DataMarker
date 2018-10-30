count = "0123456789"
for i in range(11):
    print(count[0:i].rjust(10, ' '))
for i in range(9, 0, -1):
    print(count[0:i].rjust(10, ' '))
