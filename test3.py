from pathlib import Path

from matlapy import Matlapy

mat = Matlapy()
mat.connect_first_matlab()

mat.eng.cd(str(Path().absolute()))

# mat.eng.close_system("testsys", 0, "CloseReferencedModels", "on",  nargout=0)

# mat.eng.new_system("testsys", nargout=0)

# mat.eng.open_system("testsys", nargout=0)

model = mat.Slx("test1")



#mat.eng.load_system("")
