'''
Author: Ricardo Avila
KUID: 3175035
Date Made: 9/18/24
Last modified: 9/18/24
Purpose: Make dice
'''

num_dice = 2

import random

def roll_dice(num_dice):
    roll_result = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_result.append(roll)
    return roll_result

roll_result = roll_dice(num_dice)
dice_total = 0
for int in roll_result:
    dice_total += int

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def generate_dice_faces_diagram(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

dice_face_diagram = generate_dice_faces_diagram(roll_result)
def dice_print(dice_picture):
    dice_print = f"\n{dice_face_diagram}\nDice total = {dice_total}"
    return dice_print




