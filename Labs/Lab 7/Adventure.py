
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

done = False

r1_second_hall = Room("You enter a kitchen full of knifes.\nYou feel like you are being watch.\nYou can only go back (e)ast", 2, None, 1, None, None)
r2_second_hall = Room("You enter what looks like a living room,", 3, None, None, None, 1)

second_hall = Room("You can hear the rain hit the window.\nThere is a room too your (e)ast and (w)est. You can also head back (s)outh", 1, None, None, 0, 2)

main_hall = Room("The air is dry.\nThere is a room to your (e)ast and (w)est and the hallway continues (n)orth.", 0, 1, None, None, None)

rooms = [main_hall, second_hall, r1_second_hall, r2_second_hall]
room = 0

while not done:
    print(rooms[room].text)
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

    print("\n\n")