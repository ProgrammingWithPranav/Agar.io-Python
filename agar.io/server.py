import socket
import time
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 5050
BALL_RADIUS = 5
START_RADIUS = 7

ROUND_TIME = 60 * 5

MASS_LOST_TIME = 7

WIDTH, HEIGHT = 1000, 700

SERVER_IP = "172.16.8.21"

try:
    s.bind(SERVER_IP, PORT)

except socket.error as  e:
    print(str(e))
    print("[SERVER] SERVER COULD NOT START")
    quit()

print("[SERVER] SERVER STARTED SUCCESFULLY")

#functions
def release_mass(players):
    for player in players:
        p = players[player]
        if p["score"] > 8:
            p["score"] = math.floor(p["score"]*0.95)

def check_collision(players, ball):
    pass

def player_collision(players):
    pass

def create_balls(balls, n):
    for i in range(n):
        while True:
            stop = True
            x = random.randrange(0,WIDTH)
			y = random.randrange(0,HEIGHT)
			for player in players:
				p = players[player]
				dis = math.sqrt((x - p["x"])**2 + (y-p["y"])**2)
				if dis <= START_RADIUS + p["score"]:
					stop = False
            if stop:
                break

def get_start_location(players):
    pass

def threaded_client(conn, _id):
    pass

