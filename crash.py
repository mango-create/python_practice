# Crash is an online gambling game where a rocket takes up and racks up a multiplier.
# it can crash before launching or at anytime thereafter.
# if you cash out before it explodes, you win the multiplier.
# if not, you lose the bet.
# this code simulates running the game 100x

import random

a = 0 # how many immediate crashes
b = 0 # maximum multiplier
c = 0 # average multiplier
n = 100 # number of trials
my_list = [] # a list of every multiplier value. (immediate crashes are 0)
my_hist_list = [0, 0, 0, 0, 0] # counts how many are in each slot.
# each slot represents 0, 1-6, 6-11, 11-16, 16+

for m in range(0, n):
    if round(random.random()*33) % 33 == 0:
        a+=1
        my_list.append(0)
    else:
        y = 0.99 / (1 - random.random()) # the multiplier value
        if y > b:
            b = y # finds the max multiplier in this trial
        my_list.append(y)

c = sum(my_list)/len(my_list)

# this iterates through my_list and adds 1 for each bucket
for m in range(len(my_list)):
    if my_list[m] == 0:
        my_hist_list[0] = my_hist_list[0] + 1

    if 0 < my_list[m] <= 6:
        my_hist_list[1] = my_hist_list[1] + 1

    if 6 < my_list[m] <=11:
        my_hist_list[2] = my_hist_list[2] + 1

    if 11 < my_list[m] <= 16:
        my_hist_list[3] = my_hist_list[3] + 1

    if my_list[m] > 16:
        my_hist_list[4] = my_hist_list[4] + 1

print("Total # of immediate crashes: " + str(a))
print("Highest multiplier: " + str(round(b, 2)))
print("Average multiplier: " + str(round(c, 2)), "\n")

# prints a histogram of values
print("Histogram!")
for m in range(len(my_hist_list)):
    for n in range(my_hist_list[m]):
        print("*", end = "")
    print()
