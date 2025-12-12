import json

with open("settings.json","r") as file:
    settings = json.load(file)

ops_x = [0, 1, 0, -1]
ops_y = [-1, 0, 1, 0]

class generate:
    def __init__(self, states, kara) -> None:
        self.states = states
        self.kara = kara
        self.java_commands = settings["Java_commands"]
        self.cmd_output = []

    def check(self, fac) -> int:
        self.fac = fac
        check_x = self.kara[0]+ops_x[fac]
        check_y = self.kara[1]+ops_y[fac]

        self.check_x = check_x
        self.check_y = check_y

        return self.states[check_x][check_y]

    def fac_cmd(self) -> list:
        cur_facing = int(self.kara[2])
        self.req_facing = self.fac
        
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

    def final(self) -> list:
        self.states[self.kara[0]][self.kara[1]] = 0
        self.kara = [self.check_x, self.check_y, self.req_facing]