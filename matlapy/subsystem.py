from pathlib import Path

from matlapy import Block

class Subsystem(Block):
    # def __init__(self, name, parent=None, eng=None, make_name_unique=False):
    #     if parent:
    #         path = parent + "/" + name
    #     else:
    #         path = name
    #     if eng:
    #         h = eng.add_block("simulink/Ports & Subsystems/Subsystem",
    #                       path,
    #                       "MakeNameUnique", "on" if make_name_unique else "off",
    #                       nargout=0)
    #         super().__init__(h, eng)
    #     else:
    #         super().__init__(name, eng)
    
    def subsystem(self, name):
        return Subsystem(self.path + "/" + name)

    def leave(self, step=1):
        path = str(self.path).rsplit("/", maxsplit=step)[0]
        return Subsystem(str(path), eng=self.eng)

    def enter(self):
        if "last_added_block" not in self.__dict__:
            return self
        else:
            return self.last_added_block
    
    def add_block(self, origpath, name, *args):
        self.last_added_block = Block(self.eng.add_block(origpath, self.path + "/" + name, *args))
        return self