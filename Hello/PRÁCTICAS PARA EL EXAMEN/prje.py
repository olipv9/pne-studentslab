from Servertry import MyServer


IP = "127.0.0.1"
PORT = 8080
message = MyServer(IP, PORT)


try:
    message.take_the_chose_methods("PING")
    message.take_the_chose_methods("GET 0")
    message.take_the_chose_methods("GET 1")
    message.take_the_chose_methods("GET 2")
    message.take_the_chose_methods("GET 3")
    message.take_the_chose_methods("GET 4")
    message.take_the_chose_methods("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
    message.take_the_chose_methods("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA ")
    message.take_the_chose_methods("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
    message.take_the_chose_methods("GENE U5")
    message.take_the_chose_methods("GENE FRAT1")
    message.take_the_chose_methods("GENE ADA")
    message.take_the_chose_methods("GENE FXN")
    message.take_the_chose_methods("GENE RNU6_269P")
except Exception:
    print('Something went wrong.')