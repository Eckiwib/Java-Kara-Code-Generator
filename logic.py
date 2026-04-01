import json
import copy

copy = copy.deepcopy

with open("settings.json","r") as file:
    settings = json.load(file)

# These are the relative coordinates for every square that has to be checked in order to determine the next walk direction
ops_x = [0, 1, 0, -1]
ops_y = [-1, 0, 1, 0]

class generate:
    def __init__(self, states, kara) -> None:
        self.states = copy(states)
        self.kara = kara

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

        # Assign placeholder value if kara doesn't need to turn
        out = "_"

        if dif_r < dif_l:
            out = "r"
        elif dif_r > dif_l:
            out = "l"
        elif dif_l == 2:
            out = "ll"

        return out

    def update(self) -> list:
        self.states[self.kara[0]][self.kara[1]] = 0
        self.kara = [self.check_x, self.check_y, self.req_facing]