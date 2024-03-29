import pygame

# is mouse being pressed
_mouse_pressed      = False
_mouse_pressed_prev = False

# is mouse hoving over something
_hover      = False
_hover_prev = False

# is mouse in range
def inRange(_x, _y, _size):
    return (pygame.mouse.get_pos()[0] >= _x and pygame.mouse.get_pos()[0] <= _x + _size[0]) and (pygame.mouse.get_pos()[1] >= _y and pygame.mouse.get_pos()[1] <= _y + _size[1])

# is mouse hovering 
def isHover(_x, _y, _size):
    if inRange(_x, _y, _size):
        return True
    return False

# is mouse hover once
# **TODO** needs changing, will only work with one element
def isHover_once(_x, _y, _size):
    global _hover
    if inRange(_x, _y, _size) and not _hover and not _hover_prev:
        _hover = True
        return True
    elif not inRange(_x, _y, _size):
        _hover = False
    return False

# is mouse pressed once
def pressed_once():
    if _mouse_pressed and not _mouse_pressed_prev:
        return True
    return False

# update mouse
def update():
    global _mouse_pressed
    global _mouse_pressed_prev
    global _hover
    global _hover_prev

    _mouse_pressed_prev = _mouse_pressed
    _hover_prev = _hover

    _mouse_pressed = pygame.mouse.get_pressed()[0]

