from PIL import Image
import twophase.solver as sv
from pixel_maps import pixel_map

_success_phrase = str('{:<50}' + '\033[92m' + '[OK]' + '\033[0m').format(' ')
_fail_phrase = str('{:<50}' + '\033[91m' + '[FAIL]' + '\033[0m').format(' ')
_filename_prefix = "images/"
_filename_suffix = ".jpg"


# takes RGB values and converts it to white, orange, red, green , blue or yellow
def rgb_to_color(red_val: int, green_val: int, blue_val: int, is_verbose: bool) -> str:
    """
        accepts an RGB value and outputs one of six of the possible colours on the Rubik's Cube and the corresponding
        face, with green being front and white being up
        :param red_val: int
        :param green_val: int
        :param blue_val: int
        :return: str
        """
    if 130 < red_val < 210 and 130 < green_val < 210 and 130 < blue_val < 210:
        if is_verbose:
            print('white/up')
        return 'U'
    if red_val < 5 and green_val > 60 and blue_val < 30:
        if is_verbose:
            print('green/front')
        return 'F'
    if red_val > 100 and green_val > 120 and blue_val < 30:
        if is_verbose:
            print('yellow/down')
        return 'D'
    if red_val < 5 and green_val < 60 and blue_val > 70:
        if is_verbose:
            print('blue/back')
        return 'B'
    if red_val > 145 and 50 < green_val < 95 and blue_val < 35:
        if is_verbose:
            print('orange/left')
        return 'L'
    if 105 < red_val < 190 and green_val < 50 and blue_val < 40:
        if is_verbose:
            print('red/right')
        return 'R'
    else:
        print('Error: Color does not fit given ranges')
        return 'None'


def convert_raw_to_formatted(raw: str) -> str:
    """
    converts the raw instructions set created by sv.solve to a more friendly version by replacing any three clockwise
    rotations to one counterclockwise rotation, removing the move counter at the end of the string and adding positive
    and negative signs to signify clockwise and counterclockwise rotation
    :param raw: str
    :return: str
    """
    remove_last_chars = raw[:-5]
    remove_last_space = remove_last_chars.strip()
    added_plus_one = remove_last_space.replace('1', '+1')
    added_plus_two = added_plus_one.replace('2', '+2')
    formatted = added_plus_two.replace('3', '-1')
    return formatted


# face_side is L or R, face number is the number that tells you where in that face the location is.
# color is what is handed to the function i.e. U
def cubestring_index(face_side: str, face_number: int) -> int:
    """
    face_side is L, R, U, D, B or F face number is the number that tells you where in that face the location is (1-9).
    color is what is returned from the function i.e. U
    :param face_side: tuple
    :param face_number: int
    :return: int
    """
    # First thing to calculate the index of the color from the location
    # Then we return the index we calculated
    face_values = {
        'U': 0,
        'R': 9,
        'F': 18,
        'D': 27,
        'L': 36,
        'B': 45
    }
    return face_values[face_side] + face_number - 1


def cords_to_cube(filename: str, face_name: str, pixel_map: dict, cube_color_list: list, is_verbose: bool) -> list:
    """
    retrieves picture of cube, references the pixel map to find the corresponding pixel cords for each face in the
    picture, with the rgb_to_color function, it then determines the color of each pixel, which it uses to generate
    the cubestring
    :param filename: str
    :param face_name: tuple
    :param pixel_map: dict
    :param cube_color_list: list
    :return: list
    """
    img = Image.open(_filename_prefix + filename + _filename_suffix)
    counter = 1

    while counter <= 9:
        cords = (pixel_map[str(counter)]['x'],
                 pixel_map[str(counter)]['y'])
        red_value, green_value, blue_value = img.getpixel(cords)
        color = rgb_to_color(red_value, green_value, blue_value, is_verbose)
        if is_verbose or color == 'None':
            print('\n')
            print('Red: ' + str(red_value))
            print('Green: ' + str(green_value))
            print('Blue: ' + str(blue_value))
            # print location and cords given
            print(str(face_name) + str(counter) + " " + "@" + str(cords))
        index = cubestring_index(face_name, counter)
        cube_color_list[index] = color
        counter += 1
    return cube_color_list


def verbose_input() -> bool:
    i = input("\nType 'y' for verbose print and 'n' for a simpler run")
    i.lower()
    if i == 'y' or i == 'yes':
        return True
    elif i == 'n' or i == 'no':
        return False
    else:
        print("NOT A VALID INPUT")
        verbose_input()


def main(is_verbose: bool) -> str:
    cube_color_list = ['None'] * 54

    filenames = ["1_white", "2_green", "3_yellow", "4_blue", "5_orange", "6_red"]
    face_order = ["U", "F", "D", "B", "L", "R"]

    # run the cords_to_cube function for each of the 6 images and their respective sides
    for i in range(len(filenames)):
        cords_to_cube(filenames[i], face_order[i], pixel_map, cube_color_list, is_verbose)

    print("\n" + "COMPLETE")
    cubestring = ''.join(cube_color_list)

    # Use test cubestring below
    cubestring = 'RDRFUFRDRFLFBRBFLFURUDFDURULULBDBLULBRBFLFBRBDLDUBUDLD'
    print("\nTHIS IS A TEST CUBESTRING IT IS NOT GENERATED, REMOVE WHEN TESTING FUNCTIONS BEFORE sv.solve")

    print(cubestring)

    instructions = sv.solve(cubestring, 19, 10)

    # raw instructions
    print('raw: ' + instructions)
    # with counter rotations / no move number
    formatted_inst = convert_raw_to_formatted(instructions)
    print('added counter rotations: ' + formatted_inst)
    return formatted_inst


# ----------------------------------------------------TESTING-----------------------------------------------------------

def test_cubestring_to_raw(cubestring_input: str, expected_result: str, counter: int) -> str:
    """
    This is a testing function, comparing test cubestrings to their expected instructions, cubestring input is the
    cubestring, the function runs sv.solve and compares the result to the corresponding expected result
    :param cubestring_input: str
    :param expected_result: str
    :param counter: int
    :return: str
    """
    test_instructions = sv.solve(cubestring_input, 19, 10)
    if test_instructions == expected_result:
        return '#' + str(counter + 1) + ' cubestring to raw inst.' + _success_phrase
    if test_instructions != expected_result:
        return '#' + str(counter + 1) + ' cubestring to raw inst.' + _fail_phrase


def test_raw_to_formatted(test_instructions: str, expected_result: str, counter: int) -> str:
    """
    This is a testing function, comparing test instructions to their expected formatted versions. The test instuctions
    are formatted inside the function to test it
    :param test_instructions: str
    :param expected_result: str
    :param counter: int
    :return: str
    """
    if test_instructions == expected_result:
        return '#' + str(counter + 1) + ' raw to formatted inst. ' + _success_phrase
    if test_instructions != expected_result:
        return '#' + str(counter + 1) + ' raw to formatted inst. ' + _fail_phrase


def cubestring_to_formatted_inst_testing():
    """
    This is a print function that tests different functions to convert test cubestrings to the raw instructions
    then to the formatted instructions
    :return:
    """
    print('\n' + 'TESTS BELOW'.center(80, '*') + '\n')

    test_cubestrings_array = [
        'BUDLUBLRFUULBRBRLLUURBFLFDDDRBRDURFURFFDLDFFLBFURBLBDD',
        'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL',
        'RDRFUFRDRFLFBRBFLFURUDFDURULULBDBLULBRBFLFBRBDLDUBUDLD'
    ]

    expected_raw_inst_array = [
        'D2 R1 B1 L2 U3 D1 R1 B1 U1 F1 (10f)',
        'L3 U1 B1 R2 F3 L1 F3 U2 L1 U3 B3 U2 B1 L2 F1 U2 R2 L2 B2 (19f)',
        'R1 L1 U1 D3 F2 U1 D3 B2 U1 D3 L2 (11f)'
    ]

    expected_formatted_inst_array = [
        'D+2 R+1 B+1 L+2 U-1 D+1 R+1 B+1 U+1 F+1',
        'L-1 U+1 B+1 R+2 F-1 L+1 F-1 U+2 L+1 U-1 B-1 U+2 B+1 L+2 F+1 U+2 R+2 L+2 B+2',
        'R+1 L+1 U+1 D-1 F+2 U+1 D-1 B+2 U+1 D-1 L+2'
    ]

    # test cubestring to raw instructions
    for i in range(0, len(test_cubestrings_array)):
        cubestring_to_raw_result = test_cubestring_to_raw(test_cubestrings_array[i], expected_raw_inst_array[i], i)
        print(cubestring_to_raw_result)

    # test cubestring to formatted inst
    for i in range(0, len(expected_raw_inst_array)):
        test_formatted = convert_raw_to_formatted(expected_raw_inst_array[i])
        raw_to_formatted_result = test_raw_to_formatted(test_formatted, expected_formatted_inst_array[i], i)
        print(raw_to_formatted_result)
