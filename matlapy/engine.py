"""matlab_connection
"""
from typing import Tuple

import matlab.engine as matlab_engine
import matlab.engine.matlabengine

class Engine(matlab_engine):
    def __init__(self) -> None:
        print("Init MatlabConnection")
        self.eng = None
        self.eng_name = ""

    @property
    def eng_names(self) -> Tuple[str, ...]:
        return matlab_engine.find_matlab()

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
