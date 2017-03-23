'''
Use the power_data.csv file AND the zipcode database
to answer the questions below.  Make sure all answers
are printed in a readable format. (i.e. "The city with the highest electricity cost in Illinois is XXXXX."

The power_data dataset, compiled by NREL using data from ABB,
the Velocity Suite and the U.S. Energy Information
Administration dataset 861, provides average residential,
commercial and industrial electricity rates by zip code for
both investor owned utilities (IOU) and non-investor owned
utilities. Note: the file includes average rates for each
utility, but not the detailed rate structure data found in the
OpenEI U.S. Utility Rate Database.

This is a big dataset.
Below are some questions that you likely would not be able
to answer without some help from a programming language.
It's good geeky fun.  Enjoy

FOR ALL THE RATES, ONLY USE THE BUNDLED VALUES (NOT DELIVERY).  This rate includes transmission fees and grid fees that are part of the true rate.
'''
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

power_data = []
file = open("power_data.csv", 'r')

reader = csv.reader(file, delimiter=',')

for line in reader:
    power_data.append(line)

print(power_data)

zipcode_data = []
file = open("free-zipcode-database-Primary.csv", 'r')

reader = csv.reader(file, delimiter=',')

for line in reader:
    zipcode_data.append(line)

#print(zipcode_data)
print()
#1  What is the average residential rate for YOUR zipcode? You will need to read the power_data into your program to answer this.  (7pts)
def average_rate(zip):
    for i in range(len(power_data)):
        print(power_data[i])
        if power_data[i][0] == zip:
            return power_data[i][8]
        else:
            pass

print("My zipcode's average residential rate (Bundled) is", average_rate(str(60657)))
print()

#2 What is the MEDIAN rate for all BUNDLED RESIDENTIAL rates in Illinois? Use the data you extracted to check all "IL" zipcodes to answer this. (10pts)
my_list = []
def sort():
    for i in range(len(power_data) - 1):
        if power_data[i+1][3] == "IL" and power_data[i+1][4] == "Bundled":
            my_list.append(power_data[i][8])

    for pos in range(1, len(my_list)):
        key_pos = pos
        scan_pos = key_pos - 1
        key_val = my_list[key_pos]

        while my_list[scan_pos] > key_val and scan_pos >= 0:
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        my_list[scan_pos + 1] = key_val

    #print(my_list)

sort()
def bundled_res():
    pos = len(my_list)//2
    return my_list[pos]

print("The MEDIAN value is", bundled_res())
print()

#3 What city in Illinois has the lowest residential rate?  Which has the highest?  You will need to go through the database and compare each value for this one. Then you will need to reference the zipcode dataset to get the city.  (15pts)
biggest = .11
biggest_zip = 0
smallest = .05
smallest_zip = 0

for i in range(len(power_data)-1):
    if power_data[i+1][3] == "IL":
        res = float(power_data[i+1][8])
        if res > biggest:
            biggest = res
            biggest_zip = power_data[i+1][0]
        elif res < smallest:
            smallest = res
            smallest_zip = power_data[i+1][0]

biggest_city = ""
smallest_city = ""
for i in range(len(zipcode_data)-1):
    if zipcode_data[i+1][0] == biggest_zip:
        biggest_city = zipcode_data[i+1][2]
    elif zipcode_data[i+1][0] == smallest_zip:
        smallest_city = zipcode_data[i+1][2]

print("The biggest residential rate occurs in", biggest_city)
print("The smallest residential rate occurs in", smallest_city)
print()
#FOR #4  CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS. The first one is easier than the second.
#4  (Easier) USING ONLY THE ZIP CODE DATA... Make a scatterplot of all the zip codes in Illinois according to their Lat/Long.  Make the marker size vary depending on the population contained in that zip code.  Add an alpha value to the marker so that you can see overlapping markers.
import matplotlib.pyplot as plt
import random

xval = [] #6
yval = [] #5
size = []

for i in range(len(zipcode_data)):
    if zipcode_data[i][3] == "IL":
        if zipcode_data[i][10]:
            xval.append(float(zipcode_data[i][6]))
            yval.append(float(zipcode_data[i][5]))
            size.append(float(zipcode_data[i][10])/30)

plt.figure(1,tight_layout=True,figsize=(6,8))
plt.scatter(xval, yval, size, alpha=.42)


plt.show()


#4 (Harder) USING BOTH THE ZIP CODE DATA AND THE POWER DATA... Make a scatterplot of all zip codes in Illinois according to their Lat/Long.  Make the marker red for the top 25% in residential power rate.  Make the marker yellow for the middle 25 to 50 percentile. Make the marker green if customers pay a rate in the bottom 50% of residential power cost.  This one is very challenging.  You are using data from two different datasets and merging them into one.  There are many ways to solve. (20pts)