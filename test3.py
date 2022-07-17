from pathlib import Path

from matlapy import Matlapy

mat = Matlapy()
mat.connect_first_matlab()

mat.eng.cd(str(Path().absolute()))

#mat.eng.load_system("")
