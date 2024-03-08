from Client0 import Client


IP = "127.0.0.1"
PORT = 8080
message = Client(IP, PORT)


try:
    message.talk("PING")
    message.talk("GET 0")
    message.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
    message.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA ")
    message.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
    message.talk("GENE U5")
except Exception:
    print('Something went wrong.')

