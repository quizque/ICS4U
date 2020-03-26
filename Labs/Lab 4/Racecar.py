#********************************************************************************
#** Nick Coombe - March 06, 2020 ***
#** Lab 4 Camel ***
#** ***
#** Replaced camel game with car game. Goal is to make ***
#** it to the end without being overtaken ***
#** ***
#********************************************************************************

import random

############################
### CHANGEABLE CONSTANTS ###
############################

# How long does the game last?
MAX_DISTANCE = 100

# Full speed distance
DIST_FULL = 15

# Slow speed distance
DIST_SLOW = 10

# Full speed random range
RNG_RANGE = 8

# Car starting distance
STARTING_DIST = 20

# Starting fuel
STARTING_FUEL = 10

########################
### GLOBAL VARIABLES ###
########################

# Current distance traveled
dist_traveled = STARTING_DIST

# Enemy distance traveled
enemy_dist_traveled = 0

# Starting fuel
fuel = STARTING_FUEL

#################
### FUNCTIONS ###
#################

# Display the current status
def displayStatus():
    print("\n~~~ STATUS ~~~")
    print("Current distance:", dist_traveled)
    print("Enemy distance:", enemy_dist_traveled)
    print("Fuel left:", fuel)

#####################
### MAIN FUNCTION ###
#####################

print("~~~~~ INSTRUCTIONS ~~~~~")
print("You are in a race and things")
print("are getting down to the final")
print("stretch! You must make it " + str(MAX_DISTANCE))
print("to win. Good luck!")

# While the user hasn't surpassed the distance required
while (dist_traveled <= MAX_DISTANCE):
    
    # If enemy over takes, lose
    if enemy_dist_traveled >= dist_traveled:
        print("You have been over taken!")
        print("Game over!")
        exit(1)
    
    # Out of fuel?
    if fuel <= 0:
        print("You're out of fuel!")
        print("Game over!")
        exit(1)

    # Display status
    displayStatus()

    # Ask next move
    print("\n~~~~~ ENTER NEXT MOVE ~~~~~")
    print("""a) Full speed
b) Normal speed
c) Pit stop (refuel)
d) Drift
other) Stop car
q) Quit""")
    usr_input = input("").lower()

    # If full speed...
    if usr_input == 'a':
        # Determind if the full speed was buff or not
        dist = random.randrange(DIST_FULL-RNG_RANGE-2, DIST_FULL)
        print("You moved " + str(dist) + "!")
        dist_traveled += dist

    # If slow speed
    if usr_input == 'b':
        # Move at a constant speed
        print("You moved " + str(DIST_SLOW) + "!")
        dist_traveled += DIST_SLOW

    # If pit stop, do nothing
    if usr_input == 'c':
        fuel = 10
        print("You took a pit stop and refueled!")

    # If drift, lose. You can't drift.
    if usr_input == 'd':
        print("You moved drifted and crashed!")
        print("Game over!")
        exit(1)

    # If q, quit game
    if usr_input == 'q':
        print("Leaving game!")
        exit(1)

    # Enemy will always move random dist
    dist = random.randrange(DIST_FULL-RNG_RANGE, DIST_FULL)
    print("The enemy moved " + str(dist) + "!")
    enemy_dist_traveled += dist

    # Remove one fuel point
    fuel -= 1

print("You reached the finish line! Congrats")