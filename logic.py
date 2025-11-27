import random, time

commands = ["move()", "right()", "left()"]

def iwas():
    time1 = time.time()
    command = commands[random.randint(0,2)]
    time2 = time.time()
    difference = time2-time1
    return command, difference