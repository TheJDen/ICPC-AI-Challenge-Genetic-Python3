# from multiprocessing import Process,Queue,Pipe
# import planetoids

# def send_cmd(cmd_queue, game):
#     #raw_json = data_stream.get()
#     cmd = "110001"
#     cmd_queue.put(cmd)

# def main():
#     data_stream = Queue()
#     # parent_cmd_stream,child_cmd_stream = Pipe()
#     data_p = Process(target=planetoids.send_data, args=(data_stream,))
#     #cmd_p = Process(target=send, args=(child_data_stream,))
#     data_p.start()
#     #cmd_p.start()
#     raw_json = data_stream.get()
#     #parent_cmd_stream.send(command)   # prints "Hello"
# import sys
# import os
# import json
# def main():
#     last_data_line_count = 0
#     while True:
#         raw_data = None
#         while not raw_data:
#             with open("DataStream.txt", "r") as data_stream:
#                 data_lines = data_stream.readlines()
#                 if len(data_lines) == last_data_line_count: continue
#                 if len(data_lines) > last_data_line_count:
#                     raw_data = data_lines[-1]
#                     last_data_line_count = len(data_lines)
#                 else: sys.exit(1)
#         data = json.loads(raw_data)
#         with open("CommandStream.txt", "w") as cmd_stream:
#             if "gameOver" in data and data["gameOver"]:
#                 cmd_stream.write("exit") # Exit if we hit Game Over.
#             cmd_stream.write("110001\n")



# def main():
#     data = None
#     os.system("sh ../LaunchSubmission_macOS.sh")
#     last_data_line_count = 0
#     while True:
#         raw_data = None
#         while not raw_data:
#             with open("DataStream.txt", "r") as data_stream:
#                 data_lines = data_stream.readlines()
#                 if len(data_lines) == last_data_line_count: continue
#                 if len(data_lines) > last_data_line_count:
#                     raw_data = data_lines[-1]
#                     last_data_line_count = len(data_lines)
#                 else: break
#         data = json.loads(raw_data)
#         with open("CommandStream.txt", "w") as cmd_stream:
#             # if "gameOver" in data and data["gameOver"]:
#             #     cmd_stream.write("exit") # Exit if we hit Game Over.
#             #     break
#             #cmd_stream.write(str(data)+"\n")
#             cmd_stream.write("110001\n")
#     with open("CommandStream.txt", "w") as cmd_stream:
#         cmd_stream.write(str(data))
# data_stream_path = "/tmp/datafifo"
# cmd_stream_path = "/tmp/cmdfifo"    
# def main():
#     if os.path.exists(data_stream_path):
#         os.unlink(data_stream_path)
#     data_fifo = os.mkfifo(data_stream_path, mode=0o666)
#     data_stream = open(data_stream_path, "w", 0)#, os.O_WRONLY | os.O_NONBLOCK)
#     cmd_stream = open(cmd_stream_path, "r", 0)
#     last_cmd_line_count = 0
#     while True:
#         raw_data = sys.stdin.readline().strip()
#         if not raw_data:
#             os.unlink(data_stream_path)
#             break # Exit if stdin is closed.
#         data_stream.write(raw_data)
#         cmd = None
#         while not cmd:
#             cmd = cmd_stream.read()
#         if "exit" in cmd:
#             os.unlink(data_stream_path)
#             sys.exit(0)
#         sys.stdout.write(cmd+'\n')
#         sys.stdout.flush() 
# tmpdir = "/tmp/"
# data_stream_name = "datafifo"
# cmd_stream_name = "cmdfifo"
# data_stream_path = tmpdir + data_stream_name
# cmd_stream_path = tmpdir + cmd_stream_name   
# def main():
#     # data = {'artfPos': [-2749.65234375, 1245.014404296875],
#     #     'astIds': [], 'astNum': 0, 'astPos': [], 'astSizes': [],
#     #     'bulIds': [], 'bulNum': 0, 'bulPos': [], 'bulSrc': [],
#     #     'currentRound': 1, 'currentScore': 5000.0, 'currentTime': 540.702392578125, 
#     #     'lives': 3, 'magic_num2': 3490578157,
#     #     'shipPos': [0.0, 0.0], 'shipR': 90.0,
#     #     'ufoIds': [1, 2, 3], 'ufoNum': 0, 'ufoPos': [], 'ufoSizes': []}
#     # bytes = pickle.dumps(data)
#     #print(len(bytes), "bytes")
#     try: os.unlink(cmd_stream_path)
#     except Exception: pass
#     try: os.unlink(data_stream_path)
#     except Exception: pass

#     cmd_fifo = os.mkfifo(cmd_stream_path, mode=0o666)#, mode=0o666)
#     print("made cmd fifo")
#     data_fifo = os.mkfifo(data_stream_path, mode=0o666)#, mode=0o666)
#     print("made data fifo")
#     data_stream =  os.open(data_stream_path, os.O_RDONLY | os.O_NONBLOCK)
#     print("opened data fifo")
#     # rdir_fd = os.open(tmpdir, os.O_RDONLY | os.O_NONBLOCK)
#     # wdir_fd = os.open(tmpdir, os.O_RDONLY | os.O_NONBLOCK)
#     # def ropener(path, flags):
#     #      return os.open(path, flags, dir_fd=rdir_fd)
#     # def wopener(path, flags):
#     #      return os.open(path, flags, dir_fd=wdir_fd)
    
#     os.system("sh ../LaunchSubmission_macOS.sh")
#     print("launched game")
#     raw_data = None
#     while not raw_data:
#         raw_data = os.read(data_stream, 1000)
#     cmd_stream =  os.open(cmd_stream_path, os.O_WRONLY | os.O_NONBLOCK)
#     print("opened cmd_stream")
    
#     # while True:
#     #     if os.path.exists(data_stream_path): break
#     #     print("acquired cmd fifo")
#     # with  as data_stream:#, os.O_WRONLY | os.O_NONBLOCK)
#     #     os.set_blocking(data_stream.fileno(), False)
#     last_data_line_count = 0
#     while True:
#         raw_data = None
#         while not raw_data:
#             raw_data = os.read(data_stream, 1000)
#         data = json.loads(pickle.loads(raw_data))
#         if "gameOver" in data and data["gameOver"]:
#                 os.write(cmd_stream, pickle.dumps("exit")) # Exit if we hit Game Over.
#                 os.fsync(cmd_stream)
#                 break
#         else: 
#             os.write(cmd_stream,pickle.dumps("110001\n")) # pickle
#             os.fsync(cmd_stream)
    
#     try: os.unlink(data_stream_path)
#     except Exception: pass
#     try: os.unlink(cmd_stream_path)
#     except Exception: pass
#     # os.close(rdir_fd)
#     # os.close(wdir_fd)
import json
from multiprocessing.connection import Listener, Client
import subprocess
data_stream_address = ("127.0.0.1", 6000)     # family is deduced to be 'AF_INET
cmd_stream_address = ("127.0.0.1", 6001)

def play_round(data_listener):
    game = subprocess.Popen(["sh", "../LaunchSubmission_macOS.sh"]) #("sh ../LaunchSubmission_macOS.sh") NONBLOCKING
    print("submission")
    data_stream = data_listener.accept()
    print("connection accepted from", data_listener.last_accepted)    
    print(data_stream.recv()) # out of sync execution possible , chance low enough to be accceptable for now
    cmd_stream = Client(cmd_stream_address, authkey=b'secret password') # in that case this would not connect because listener not accepted
    #gen = (cmd for cmd in ("110001", "exit"))
    score = 0
    while True:
        raw_data = data_stream.recv()
        if not raw_data:
            print("closing datastream")
            data_stream.close()
            break
        data = json.loads(raw_data)
        #print(data)
        # do something with msg
        # if "gameOver" in data and data["gameOver"]:
        score = data["currentScore"]   
        cmd_stream.send("110001")
    cmd_stream.close()
    return score

def main():
    data_listener = Listener(data_stream_address, authkey=b'secret password')
    print("made listener")
    for _ in range(2):
        print(play_round(data_listener))
    data_listener.close()
    
    
if __name__ == '__main__':
    print("entered")
    main()

