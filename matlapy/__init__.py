import matlapy.matlab_connection
from .block import Block

from multiprocessing import Process


class MatlapyMultiProcessing:
    def __init__(self) -> None:
        self.procs = []

    def add(self, proc):
        print("add proc")
        self.procs.append(proc)

        with Process(target=proc.start, args=()) as p:
            p.start()

        
        

class Matlapy:
    def __init__(self) -> None:
        #self.connection = matopy.matlab_connection.connection
        self.connection = matlapy.matlab_connection.MatlabConnection()
        
        self.find_matlab = lambda : self.connection.find_matlab()
        self.connect_matlab = lambda eng_name : self.connection.connect_matlab(eng_name)
        self.start_matlab = lambda : self.connection.start_matlab()
        self.connect_first_matlab = lambda : self.connection.connect_first_matlab()

    @property
    def eng(self):
        return self.connection.eng

    def start(self):
        print("start")
        self.connect_first_matlab()

    def Block(self, h):
        return Block(h, eng=self.eng)

