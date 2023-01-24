import movement_map as movement_map

movement_map.movement_map = dict(movement_map.movement_map)


def inst_to_servo(inst: list):
    command_list = []
    _one_turn_degrees = 90
    for i in range(len(inst)):
        if inst[i][1] == '-':
            rotation_direction = '-'
        else:
            rotation_direction = '+'
        move_to = movement_map.movement_map[str(inst[i][0])][0]
        move_back = movement_map.movement_map[str(inst[i][0])][1]

        # remove to run latter func. used rn for debugging
        command_list.append("\nprint('" + "Movement # " + str(i) + "')")

        command_list.append(move_to)
        command_list.append(move_back)
        command_list.append("locking_bar(true)")
        command_list.append("holder_servo.write(" + rotation_direction + str(int(inst[i][2]) * _one_turn_degrees) + ")")
        command_list.append("locking_bar(false)")
    return command_list


# test input bc don't want to print every time
inst_to_servo([['R', '+', '1'], ['L', '+', '1'], ['U', '+', '1'], ['D', '-', '1'], ['F', '+', '2'], ['U', '+', '1'],
               ['D', '-', '1'], ['B', '+', '2'], ['U', '+', '1'], ['D', '-', '1'], ['L', '+', '2']])
