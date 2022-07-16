import matlapy.matlab_connection
from .block import Block

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

    def Block(self, h):
        return Block(h, eng=self.eng)
