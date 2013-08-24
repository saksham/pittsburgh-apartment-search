
import os

class BrowsedItems(object):
    __dir, __src = os.path.split(os.path.abspath(__file__))
    __emailed_filepath = __dir+"/Emailed.txt"
    __useless_filepath = __dir+"/Useless.txt"
    def __init__(self):
        emailed_file = open(BrowsedItems.__emailed_filepath, "r")
        self.emailed = {}
        for line in emailed_file:
            if len(line.strip()) == 0:
                continue
            tokens = line.split(",")
            self.emailed[tokens[0].strip()] = tokens[1:]
        useless_file = open(BrowsedItems.__useless_filepath, "r")
        self.useless = {}
        for line in useless_file:
            if len(line.strip()) == 0:
                continue
            tokens = line.split(",")
            self.useless[tokens[0].strip()] = tokens[1:]
        self.visited = {}
        for emailed in self.emailed:
            if emailed not in self.visited:
                self.visited[emailed] = True
        for useless in self.useless:
            if useless not in self.visited:
                self.visited[useless] = True
       
    def add_useless(self, id, line):
        f = open(BrowsedItems.__useless_filepath, "a")
        f.write(id + "," + line + "\n")
        
    def add_emailed(self, id, email):
        f = open(BrowsedItems.__emailed_filepath, "a")
        f.write(id + "," + email + "\n")
        