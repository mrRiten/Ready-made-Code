"""
    ================================================================
    This script create work-threads
    Work threads are created in a loop
    Every thread write information in the database (json)
    Time for work threads is randomly generated
    ================================================================
"""

import threading as th
from threading import Thread
import time
from random import randint
import json

logs = []   # for get inf about work threads
threads = []    # for get quantity of threads


# Create class for threading
class DataThread(th.Thread):
    # initializes the thread
    def __init__(self, order, time_work, work=0):
        th.Thread.__init__(self)
        self.time_work = time_work
        self.order = order
        self.work = work

    # active thread/ work thread
    def run(self):
        # imitation of work
        while self.time_work != 0:
            self.time_work -= 1
            self.work += 1
            print(f'thread №{self.order}: {self.work}')
            time.sleep(1)
        self.add_inf()
        self.json_work()

    # add inf  about thread`s work
    def add_inf(self):
        global logs
        logs.append([self.order, self.work])
        print(logs)

    # add inf in database
    def json_work(self):
        # open JSON file
        with open('data.json', 'r') as file_obj:
            data_from_json = json.load(file_obj)
        # check data
        if str(self.order) not in data_from_json:
            data_from_json[self.order] = {"name": f"thread{self.order}", "time": self.work}
        file_obj.close()
        # append inf in json
        with open('data.json', 'w') as file_obj:
            json.dump(data_from_json, file_obj, indent=4, ensure_ascii=False)
        file_obj.close()


# run one thread
def run_thread(count):
    threads.append(DataThread(count, randint(1, 15)).run())


# run all threads in loop
for n in range(10):
    thr = Thread(target=run_thread, args=(n, ))
    thr.start()
