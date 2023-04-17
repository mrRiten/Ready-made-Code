"""
    This script create and work with simple Database
    First active: add to database 10 elements
    Second active: delete from database 5 random elements

"""

import json
from random import randint


# Create main class
class TestDatabase:
    # initialization elements
    def __init__(self, order, name, player1, player2):
        self.order = order
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.reg()

    # register and add users with server to database
    def reg(self):
        # open JSON file
        with open('data.json', 'r') as file_obj:
            data_from_json = json.load(file_obj)
        # check user.id
        if str(self.order) not in data_from_json:
            data_from_json[self.order] = {"name": self.name, "player1": self.player1, "player2": self.player2}
        # append user in json
        with open('data.json', 'w') as file_obj:
            json.dump(data_from_json, file_obj, indent=4, ensure_ascii=False)


# delete data-element from JSON file and delete element from server_list
def delete(order_delete):
    global server
    server.pop(order_delete)
    with open('data.json', 'r') as file_obj:
        data_from_json = json.load(file_obj)
    if str(order_delete) in data_from_json:
        del data_from_json[str(order_delete)]
    with open('data.json', 'w') as file_obj:
        json.dump(data_from_json, file_obj, indent=4, ensure_ascii=False)


# create 10 classes in server_list
server = []
for i in range(10):
    # random int number for user
    pl1 = randint(0, 100)
    pl2 = randint(0, 100)
    server.append(TestDatabase(i, f'server{i}', pl1, pl2))

# print server_list
print(server)
# wait for user activity
activ = str(input('Continue?\t'))

# delete 5 random classes and elements from database
for i in range(6):
    ind = randint(0, len(server))
    delete(ind)

# print server_list
print(server)
