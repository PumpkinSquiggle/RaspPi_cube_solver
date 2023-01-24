
# take first picture
# flip cube twice then rotate cube once
# take second picture

# run color_extraction.py
# separate each move from the instructions into a dict
# separate the three components of each instruction into a nested dict (face, number of turns)
# instructions = 'D+2 R+1 B+1 L+2 U-1 D+1 R+1 B+1 U+1 F+1'


def print_movements(inst: str) -> None:
    """
    Simply prints the given instructions in a more readable format
    To be used for debugging.
    :param inst: str
    :return:
    """
    movements_arr = inst.split()
    for i in range(len(movements_arr)):
        face = str(movements_arr[i])[0]
        direction = str(movements_arr[i])[1]
        count = str(movements_arr[i])[2]
        print('\n')
        print('Movement # ' + str(i + 1))
        print('Face: ' + face)
        print('Rotations: ' + count)
        if direction == '+':
            print('Direction: Counter-clockwise')
        if direction == '-':
            print('Direction: Clockwise')


def computer_instructions(inst: str) -> list:
    """
    Turns the instruction string into a 2D array allowing for easier calling
    :param inst: str
    :return: list
    """
    computer_inst_arr = []
    movements_arr = inst.split()
    for i in range(len(movements_arr)):
        face = str(movements_arr[i])[0]
        direction = str(movements_arr[i])[1]
        count = str(movements_arr[i])[2]
        temp_list = [face, direction, count]
        computer_inst_arr.append(temp_list)
    return computer_inst_arr


def main_movements(formatted_inst: str):
    # print_movements(formatted_inst) Uncomment for more human legible movements (not in array)
    print('\n')
    print('Final Instructions:')
    print(computer_instructions(formatted_inst))
