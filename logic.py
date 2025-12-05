ops_x = [0, 1, 0, -1]
ops_y = [-1, 0, 1, 0]

class generate():

    def __init__(self, states, ladybug, java_commands, cmd_output) -> None:
        s = self
        s.states = states
        s.ladybug = ladybug
        s.java_commands = java_commands
        s.cmd_output = cmd_output

    def check(self, i) -> int:
        check_x = self.ladybug[0]+ops_x[i]
        check_y = self.ladybug[1]+ops_y[i]

        self.check_x = check_x
        self.check_y = check_y

        return self.states[check_x][check_y]

    def fac_cmd(self) -> list:

        cur_facing = int(self.ladybug[2])
        
        dif_r = (self.req_facing-cur_facing)%4
        dif_l = (cur_facing-self.req_facing)%4

        if dif_r < dif_l:
            self.cmd_output.append(self.java_commands["Turn right"])
        elif dif_r > dif_l:
            self.cmd_output.append(self.java_commands["Turn left"])
        elif dif_l == 2:
            self.cmd_output.append(self.java_commands["Turn left"])
            self.cmd_output.append(self.java_commands["Turn left"])

        self.cmd_output.append(self.java_commands["move"])

        return self.cmd_output

    def final(self):
        self.states[self.ladybug[0]][self.ladybug[1]] = 0
        ladybug = [self.check_x, self.check_y, self.req_facing]

        return ladybug, self.states