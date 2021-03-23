interval = 100
for val in range(0, interval + 1):
    if val > 1:
       for n in range(2, val):
           if (val % n) == 0:
               break
       else:
           print(val, end=" ")