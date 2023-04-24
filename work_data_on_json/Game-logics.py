"""
    ================================================================
    This script create work-threads
    Work threads are created in a loop
    All arguments are generated randomly
    This snippet will be used for game-bot

    Simple test program-logics for creating work-threads(game-threads)
    ================================================================
"""
import json
from threading import Thread
import threading as th
import time
from random import randint

server = []
users = []


# Register user in bot
class User:
    # initialize user statistics
    def __init__(self, id_user, username, game, win, loose):
        self.id_user = id_user
        self.username = username
        self.game = game
        self.win = win
        self.loose = loose

    # register user in json-database
    def reg_user(self):
        with open('data.json', 'r') as file_obj:
            data_from_json = json.load(file_obj)
        # check data
        if str(self.id_user) not in data_from_json:
            data_from_json[self.id_user] = {"name": f"{self.username}", "game": self.game, "win": self.win,
                                            "loss": self.loose}
        file_obj.close()
        # append user in json
        with open('data.json', 'w') as file_obj:
            json.dump(data_from_json, file_obj, indent=4, ensure_ascii=False)
        file_obj.close()
        print('reg')


# Game active class
class Game(th.Thread):
    # initialize game
    def __init__(self, session, player1, player2, active, time_work):
        th.Thread.__init__(self)
        self.session = session
        self.player1 = player1
        self.player2 = player2
        self.active = active
        self.time_work = time_work

    # run game and activate
    def run(self):
        while self.time_work != 0:
            print(f'\nSession: {self.session}: pl1: {self.player1} - {self.active}')
            print(f'\nSession: {self.session}: pl2: {self.player2} - {self.active}')
            self.time_work -= 1
            time.sleep(1)

    # delete game session and end of game
    def __del__(self):
        print(f'End game - Session {self.session} deleted!')


# func for registering users in database (imitation)
def register(user_id):
    users.append(User(user_id, str(randint(0, 100)), randint(20, 80), randint(0, 20), randint(0, 20)).reg_user())


# func for creating a new game session (imitation)
def active_th(session):
    server.append(Game(session, randint(10, 100), randint(10, 100), randint(0, 10), randint(3, 5)).run())


# run all threads in loop
for n in range(5):
    thr = Thread(target=active_th, args=(n,))
    thr.start()

for t in range(5):
    register(t)
