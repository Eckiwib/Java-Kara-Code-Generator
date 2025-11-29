Java_commands = {"move":"Kara.move()","Turn left":"Kara.turnLeft()","Turn right":"Kara.turnRight()"}

def generate(states, ladybug):

    ops_x = [1, -1, 0, 0]
    ops_y = [0, 0, 1, -1]

    for op in range(4):
        check = states[ladybug[0]+ops_x[op]][ladybug[1]+ops_y[op]]
        print(check)