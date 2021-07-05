#!/usr/bin/env python3
# ^^^ Important - tells kattis this is python3 vs python2
import os
import sys
import json
import logging
import pickle
from multiprocessing.connection import Listener, Client
# from collections import namedtuple



# #logging.basicConfig(filename="planetoids.log", encoding='utf-8', level=logging.DEBUG)

# Vector2D = namedtuple("Vector2D", ['x', 'y'])

# class Player:

#     def __init__(self, coords, bearing):
#         self._pos = Vector2D(*coords)
#         self.bearing = bearing
#         self.vel = Vector2D(0,0)

#     @property
#     def pos(self):
#         return self._pos

#     @pos.setter
#     def pos(self, coords):
#         new_pos = Vector2D(*coords)
#         self.vel = Vector2D(new_pos.x - self._pos.x, new_pos.y - self._pos.y)
#         self._pos = new_pos


# class GameState:
#     def __init__(self, data):
#         self.artifact_pos = Vector2D(*data["artfPos"])
#         self.player = Player(data["shipPos"], data["shipR"])

# def main():

#     last_cmd_line_count = 0
#     while True:
    
#         raw_data = sys.stdin.readline().strip()
#         with open("DataStream.txt", "w") as data_stream:
#             if not raw_data:
#                 data_stream.truncate()
#                 break # Exit if stdin is closed.
#             data_stream.write(raw_data)            
#         cmd = None
#         while not cmd:
#             with open("CommandStream.txt", "r") as cmd_stream:
#                 cmd_lines = cmd_stream.readlines()
#                 if len(cmd_lines) == last_cmd_line_count: continue
#                 if len(cmd_lines) > last_cmd_line_count:
#                     cmd = cmd_lines[-1]
#                     last_cmd_line_count = len(cmd_lines)
#                 else: cmd = "exit"
#         # if "exit" in cmd:
#         #     with open("DataStream.txt", "w") as data_stream:
#         #         data_stream.truncate()
#         #     break
#         sys.stdout.write(cmd+'\n')
#         sys.stdout.flush() 
# def main():
#     last_cmd_line_count = 0
#     while True:
    
#         raw_data = sys.stdin.readline().strip()
#         with open("DataStream.txt", "w") as data_stream:
#             if not raw_data:
#                 data_stream.truncate()
#                 break # Exit if stdin is closed.
#             data_stream.write(raw_data)            
#         cmd = None
#         while not cmd:
#             with open("CommandStream.txt", "r") as cmd_stream:
#                 cmd_lines = cmd_stream.readlines()
#                 if len(cmd_lines) == last_cmd_line_count: continue
#                 if len(cmd_lines) > last_cmd_line_count:
#                     cmd = cmd_lines[-1]
#                     last_cmd_line_count = len(cmd_lines)
#                 else: cmd = "exit"
#         if "exit" in cmd:
#             with open("DataStream.txt", "w") as data_stream:
#                 data_stream.truncate()
#             sys.exit(0)
#         sys.stdout.write(cmd+'\n')
#         sys.stdout.flush() 
# tmpdir = "/tmp/"
# data_stream_name = "datafifo"
# cmd_stream_name = "cmdfifo"
# data_stream_path = tmpdir + data_stream_name
# cmd_stream_path = tmpdir + cmd_stream_name  
# logging.basicConfig(filename="DataStream.txt", encoding="utf-8", level=logging.DEBUG) 
# def main():
#     data_stream = os.open(data_stream_path, os.O_WRONLY | os.O_NONBLOCK)
#     logging.debug("opened data fifo")
#     cmd_stream =  os.open(cmd_stream_path, os.O_RDONLY | os.O_NONBLOCK)# | os.O_NONBLOCK)
#     logging.debug("opened cmd fifo")
#     os.write(data_stream, bytes(0)) #ready flag
#     os.fsync(data_stream)
#     logging.debug("said was ready")
    
    
#     # rdir_fd = os.open(tmpdir, os.O_RDONLY)# | os.O_NONBLOCK)
#     # wdir_fd = os.open(tmpdir, os.O_RDONLY)# | os.O_NONBLOCK)
#     # def ropener(path, flags):
#     #      return os.open(path, flags, dir_fd=rdir_fd)
#     # def wopener(path, flags):
#     #      return os.open(path, flags, dir_fd=wdir_fd)
#     # logging.debug("bruh")
#     # with open(data_stream_name, 'w', 0, opener=wopener) as data_stream:
    

#     # data_stream = os.open(data_stream_path, os.O_WRONLY)# | os.O_NONBLOCK)
#     # data_stream = open(data_stream_path, 'w', 0)
#     #os.set_blocking(data_stream.fileno(), False)

#     last_cmd_line_count = 0
#     while True:
#         raw_data = sys.stdin.readline().strip()
#         if not raw_data:
#             try: os.unlink(cmd_stream_path)
#             except Exception: pass
#             try: os.unlink(data_stream_path)
#             except Exception: pass
#             break # Exit if stdin is closed.
#         #os.write(data_stream, raw_data)
#         os.write(data_stream, pickle.dumps(raw_data))
#         os.fsync(data_stream)
#             #os.fl
#         cmd = None
#         while not cmd:
#             cmd = os.read(cmd_stream, 1000)
#         cmd = pickle.loads(cmd)
#         if "exit" in cmd:
#             try: os.unlink(data_stream_path)
#             except Exception: pass
#             sys.exit(0)
#         sys.stdout.write(cmd+'\n')
#         sys.stdout.flush() 
#     try: os.unlink(data_stream_path)
#     except Exception: pass
#     try: os.unlink(cmd_stream_path)
#     except Exception: pass
#     # os.close(rdir_fd)
#     # os.close(wdir_fd)

data_stream_address = ("127.0.0.1", 6000)     # family is deduced to be 'AF_INET
cmd_stream_address = ("127.0.0.1", 6001)
logging.basicConfig(filename="DataStream.txt", encoding="utf-8", level=logging.DEBUG) 


def main():
    #time.sleep(2)
    #logging.debug("finished sleep")
    data_stream = Client(data_stream_address, authkey=b'secret password')
    #ogging.debug("data stream")
    cmd_listener = Listener(cmd_stream_address, authkey=b'secret password')
    #logging.debug("cmd listener")
    data_stream.send("cmd ready") 
    cmd_stream = cmd_listener.accept()
    
    # logging.debug("connection accepted from", cmd_listener.last_accepted)
    #gen = (data for data in ("yeet", "gameOver"))
    while True:
        raw_data = sys.stdin.readline().strip()
        data_stream.send(raw_data)
        if not raw_data:
            data_stream.close()
            break # Exit if stdin is closed.
        cmd = cmd_stream.recv()
        #print(cmd)
        #do something with msg
        if "exit" in cmd:
            #print("closing cmdstream")
            cmd_stream.close()
            break
        sys.stdout.write(cmd+'\n')
        #sys.stdout.write('110001\n')
        sys.stdout.flush() 
    cmd_stream.close()
    cmd_listener.close()


if __name__ == "__main__":
    #logging.debug("entered")
    main()




    # # 2. Write simulation frame to disk (DataStream.txt)
    # # 3. Repeatedly open and close CommandStream.txt until new data is available
    # # 4. Print the last command in CommandStream.txt through STDOUT
    #     data = json.loads(raw_data)
    #     logging.debug(data)
    #     # Exit if we hit Game Over.
    #     if "gameOver" in data and data["gameOver"]:
    #         break

    #     # @TODO: Process input frame

    #     # Emit command.
  






# while True:
    
#         raw_data = sys.stdin.readline()
#         # Exit if stdin is closed.
#         if not raw_data:
#             break
#         with open("DataStream.txt", "r+") as data_stream:
#             data_stream.write(raw_data)

#         command = None
#         while not command:
#             with open("CommandStream.txt", "r") as cmd_stream:
#                 cmd_stream.write(raw_data)
#     # 2. Write simulation frame to disk (DataStream.txt)
#     # 3. Repeatedly open and close CommandStream.txt until new data is available
#     # 4. Print the last command in CommandStream.txt through STDOUT
#         data = json.loads(raw_data)
#         logging.debug(data)
#         # Exit if we hit Game Over.
#         if "gameOver" in data and data["gameOver"]:
#             break

#         # @TODO: Process input frame

#         # Emit command.
#         sys.stdout.write("110001\n")
#         sys.stdout.flush()
# cmd_stream = Queue()
# cmd_p = Process(target=send_cmd, args=(cmd_stream,))
# received_command = True

# def send_data(data_stream):
#     global received_command
#     if not received_command:
#         while cmd_stream.empty(): continue

#     raw_data = sys.stdin.readline()
#     if not raw_data: sys.exit(0)
#     data_stream.put(raw_data)
#     received_command = False

# def main():
#     global received_command
#     cmd_p.start()
#     while True:
#         cmd = cmd_stream.get()
#         received_command = True
#         if cmd == "exit": sys.exit(0)
#         # Emit command.
#         cmd = cmd_stream.get()
#         sys.stdout.write(cmd + "\n")
#         sys.stdout.flush()