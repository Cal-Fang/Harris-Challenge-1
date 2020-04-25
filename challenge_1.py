# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020
# to analyze supply and demand for bikes in the system.

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json

# do not delete; this is the data you'll be working with
ivvy_stations = json.loads(open('divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and
# available bikes (num_bikes_available) at all stations in the system
total_docks_available = 0
total_bikes_available = 0

for i in range(len(ivvy_stations)):
    total_docks_available = total_docks_available + ivvy_stations[i]["num_docks_available"]  # iteratively add available docks number of each list together
    total_bikes_available = total_bikes_available + ivvy_stations[i]["num_bikes_available"]  # same logic

average_docks_available = total_docks_available / len(ivvy_stations)   # average number of empty docks (num_docks_available)
average_bikes_available = total_bikes_available / len(ivvy_stations)   # average number of available bikes (num_bikes_available)

print(average_bikes_available)
print(average_docks_available)


# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)
total_bikes_rented = 0
total_bikes = 0

for i in range(len(ivvy_stations)):
    total_bikes_rented = total_bikes_rented + ivvy_stations[i]["num_docks_available"]  # Assuming an empty dock means a rented bike
    total_bikes = total_bikes + + ivvy_stations[i]["num_docks_available"] + ivvy_stations[i]["num_bikes_available"]  # same logic, rented bikes plus available bikes

ratio_rented_to_total = total_bikes_rented / total_bikes
print(ratio_rented_to_total)


# PROBLEM 3
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows
# the percentage of bikes available at each individual station (again ignore ebikes).
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%
<<<<<<< HEAD
for i in range(len(ivvy_stations)):
    percentage = 100 * ivvy_stations[i]["num_bikes_available"] / (ivvy_stations[i]["num_bikes_available"] + ivvy_stations[i]["num_docks_available"]) # rented bikes plus available bikes equals total bikes number in each station
    percentage_rounded = round(percentage, 2)
    ivvy_stations[i]["percent_bikes_remaining"] = "{}%".format(percentage_rounded)

# Just to check how does it go:
from pprint import pprint
pprint(ivvy_stations[2])
=======
>>>>>>> parent of 957436f... Update challenge_1.py
