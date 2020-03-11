import random

############################
### CHANGEABLE CONSTANTS ###
############################

MAX_DISTANCE = 100

# Full speed distance
DIST_FULL = 15

# Slow speed distance
DIST_SLOW = 10

# Full speed random range
RNG_RANGE = 8

# Car starting distance
STARTING_DIST = 20

########################
### PRIVATE VARIBLES ###
########################

# Current distance traveled
dist_traveled = STARTING_DIST

# Enemy distance traveled
enemy_dist_traveled = 0

#################
### FUNCTIONS ###
#################

def displayStatus():
    print("\n~~~ STATUS ~~~")
    print("Current distance:", dist_traveled)
    print("Enemy distance:", enemy_dist_traveled)

#####################
### MAIN FUNCTION ###
#####################

print("~~~~~ INSTRUCTIONS ~~~~~")
print("You are in a race and things")
print("are getting down to the final")
print("stretch! You must make it " + str(MAX_DISTANCE))
print("to win. Good luck!")

while (dist_traveled < MAX_DISTANCE):
    displayStatus()

    print("\n~~~~~ ENTER NEXT MOVE ~~~~~")
    print("""a) Full speed
b) Slow speed
c) Pit stop
d) Drift
e) Check status
q) Quit""")
    usr_input = input("").lower()

    if usr_input == 'a':
        dist = random.randrange(DIST_FULL-RNG_RANGE-2, DIST_FULL)
        print("You moved " + str(dist) + "!")
        dist_traveled += dist

    if usr_input == 'b':
        print("You moved " + str(DIST_SLOW) + "!")
        dist_traveled += DIST_SLOW

    if usr_input == 'c':
        print("You took a pit stop!")

    if usr_input == 'd':
        print("You moved drifted and crashed!")
        print("Game over!")
        exit(1)

    if usr_input == 'q':
        print("Leaving game!")
        exit(1)

    dist = random.randrange(DIST_FULL-RNG_RANGE, DIST_FULL)
    print("The enemy moved " + str(dist) + "!")
    enemy_dist_traveled += dist

    if enemy_dist_traveled >= dist_traveled:
        print("You have been over taken!")
        print("Game over!")
        exit(1)

print("You reached the finish line! Congrats")