"""matlab_connection
"""
from typing import Tuple
from pathlib import Path

import matlab.engine as matlab_engine
import matlab.engine.matlabengine

class MatlabConnection:
    def __init__(self) -> None:
        self.__eng = None
        self.eng_name = ""

    @property
    def eng_names(self) -> Tuple[str, ...]:
        return matlab_engine.find_matlab()

    @property
    def eng(self):
        return self.__eng
    @eng.setter
    def eng(self, new_eng):
        self.__eng = new_eng
        self.add_mfiles_path()
    
    def add_mfiles_path(self):
        mfiles_path = str(Path(__file__).absolute().parent/"matlab").replace("/", "\\")
        self.eng.addpath(mfiles_path, nargout=0)

    def find_matlab(self) -> Tuple[str, ...]:
        return matlab_engine.find_matlab()

    def connect_matlab(self, eng_name:str) -> matlab.engine.matlabengine.MatlabEngine:
        if self.eng:
            print("Warning: connect_matlab is ignored because the MatlabConnection is already established.\n \
                Please renew instance and try again.")
            #TODO: Judge if self.eng's name is equal to eng_name or not.
        else:
            self.eng_name = eng_name
            self.eng = matlab_engine.connect_matlab(eng_name)
        return self.eng

    def start_matlab(self) -> matlab.engine.matlabengine.MatlabEngine:
        self.eng = matlab_engine.start_matlab()
        return self.eng

    def connect_first_matlab(self) -> matlab.engine.matlabengine.MatlabEngine:
        return self.connect_matlab(self.eng_names[0])


connection = MatlabConnection()
