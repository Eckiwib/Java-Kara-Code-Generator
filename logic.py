Java_commands = {"move":"Kara.move();","Turn left":"Kara.turnLeft();","Turn right":"Kara.turnRight();"}

ops_x = [0, 1, 0, -1]
ops_y = [-1, 0, 1, 0]

def generate(states, ladybug):

    cmd_output = []

    while True:

        for i in range(4):

            check_x = ladybug[0]+ops_x[i]
            check_y = ladybug[1]+ops_y[i]
            check = states[check_x][check_y]
            
            if check > 0:

                req_facing = i
                cur_facing = int(ladybug[2])
                
                dif_r = (req_facing-cur_facing)%4
                dif_l = (cur_facing-req_facing)%4

                if dif_r < dif_l:
                    cmd_output.append(Java_commands["Turn right"])
                elif dif_r > dif_l:
                    cmd_output.append(Java_commands["Turn left"])
                elif dif_l == 2:
                    cmd_output.append(Java_commands["Turn left"])
                    cmd_output.append(Java_commands["Turn left"])

                cmd_output.append(Java_commands["move"])
                
                states[ladybug[0]][ladybug[1]] = 0
                print(states)
                ladybug = [check_x, check_y, req_facing]
                print(ladybug)

                break


    
    return cmd_output