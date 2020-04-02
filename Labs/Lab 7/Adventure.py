#********************************************************************************
#** Nick Coombe 2020/03/14 ***
#** Lab 7 Introduction to Lists ***
#** ***
#** Very simple text adventure ***
#** ***
#********************************************************************************

# Room class, just to help organize
class Room():
    def __init__(self, _text, _id, _n_id = None, _e_id = None, _s_id = None, _w_id = None):

        # Display Text
        self.text = _text

        # Room ID
        self.id = _id

        # Adjacent Room IDs
        self.n_id = _n_id
        self.e_id = _e_id
        self.s_id = _s_id
        self.w_id = _w_id



# Setup rooms -----------------------------------------------------#

r1_second_hall = Room("You enter a kitchen full of knifes.\nYou feel like you are being watch.\nYou can only go back (e)ast", 2, None, 1, None, None)
win = Room("win", -1)

second_hall = Room("You can hear the rain hit the window.\nThere is a room too your (e)ast and (w)est. You can also head back (s)outh", 1, None, 3, 0, 2)

main_hall = Room("The air is dry.\nThere is a room to your (e)ast and (w)est and the hallway continues (n)orth.", 0, 1, 5, None, 4)

r1_main_hall = Room("There is a lit fire but there is nothing burning.\n What could that smell be?\nYou can only go (e)ast", 4, None, 0, None, None)
r2_main_hall = Room("You enter what looks like a living room.\nThe books look like they haven't been touched in ages.\nYou can only go back (w)est", 5, None, None, None, 0)

# array of rooms
rooms = [main_hall, second_hall, r1_second_hall, win, r1_main_hall, r2_main_hall]
# current room
room = 0

# While not done
done = False

while not done:
    # Print room text
    print(rooms[room].text)

    # Ask for direction
    i = input("Enter Direction: ").lower()

    if i == 'n':
        if not (rooms[room].n_id == None):
            room = rooms[room].n_id
    
    elif i == 'e':
        if not (rooms[room].e_id == None):
            room = rooms[room].e_id

    elif i == 's':
        if not (rooms[room].s_id == None):
            room = rooms[room].s_id

    elif i == 'w':
        if not (rooms[room].w_id == None):
            room = rooms[room].w_id

    print(room, i)

    if room == 3:
        print("Congrats!\nYou found the way out!!!")
        exit(0)

    print("\n\n")