from pathlib import Path

from matlapy import Matlapy
from matlapy.blocks import Constant, Inport, Outport

mat = Matlapy()
mat.connect_first_matlab()

mat.eng.cd(str(Path().absolute()))

# mat.eng.close_system("testsys", 0, "CloseReferencedModels", "on",  nargout=0)

# mat.eng.new_system("testsys", nargout=0)

# mat.eng.open_system("testsys", nargout=0)

mdl = mat.Slx("untitled1")

print(mat.eng.matlapy.getMdlInports("untitled1"))

print(mdl.inports)


#model.duplicate()

mdl.load()
sub1 = mdl.subsystem("sub1", make_name_unique=True)

print(sub1.name)

print(sub1.add_block(Constant, "cons1"))

search = mdl.find("sub1")
print(search)


sub1.moveTo(0, 0)

constant = sub1.add_block(Constant, "hgoe")
print(constant.name)
print(constant.parent)
subsub = sub1.subsystem(f"subsub_ue")
subsub.alignTo(constant, 2, 0, marginX=30)
constant.connectTo(subsub)
for i in range(10):
    subsub = sub1.subsystem(f"subsub{i}").alignTo(subsub, align=6, anchor=0, marginY=20).connectFrom(subsub)
terminator = sub1.add_block("simulink/Sinks/Terminator").connectFrom(subsub).alignTo(subsub, 3, 0, marginX=30)

    
