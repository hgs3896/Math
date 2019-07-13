import random
from math import pi

loop_count = 74743825
sum = 0.0
cnt = 0

for n in range(loop_count):
    x = random.random()
    y = random.random()
    if x**2+y**2 < 1:
        cnt = cnt + 1
        
    if n%2==0:
        sum = sum + 4.0 / ( 2 * n + 1 )
    else:
        sum = sum - 4.0 / ( 2 * n + 1 )

# 1. Use the Taylor expansion to calculate the PI.
print("Estimated PI Value #1 : " + str(sum))
# 2. Use the monte carlo simulation (based on geometric probability) to calculate the PI.
print("Estimated PI Value #2 : " + str(4.0*float(cnt)/(loop_count)))
# 3. Use the predefined value of PI.
print("Stored PI Value       : " + str(pi))

## Estimated PI Value #1 : 3.1415926669687746
## Estimated PI Value #2 : 3.141642804606267
## Stored PI Value       : 3.141592653589793
