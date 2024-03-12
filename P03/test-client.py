from Client0 import Client


IP = "127.0.0.1"
PORT = 8080
message = Client(IP, PORT)


try:
    message.talk("PING")
    message.talk("GET 0")
    message.talk("GET 1")
    message.talk("GET 2")
    message.talk("GET 3")
    message.talk("GET 4")
    message.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
    message.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA ")
    message.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
    message.talk("GENE U5")
    message.talk("GENE FRAT1")
    message.talk("GENE ADA")
    message.talk("GENE FXN")
    message.talk("GENE RNU6_269P")
except Exception as e:
    print(f'Something went wrong: {e}')

