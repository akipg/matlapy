from pathlib import Path

from matlapy import Block
import matlapy.blocks

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
    
    def subsystem(self, name, *args):
        sub = Subsystem(self.eng.add_block(matlapy.blocks.Subsystem,
                                           self.path + "/" + name,
                                           *args),
                        eng=self.eng)
        # sub.find("In1").delete()
        # sub.find("Out1").delete()
        return sub

    def leave(self, step=1): 
        path = str(self.path).rsplit("/", maxsplit=step)[0]
        return Subsystem(str(path), eng=self.eng)

    def enter(self):
        if "last_added_block" not in self.__dict__:
            return self
        else:
            return self.last_added_block
    
    def add_block(self, origpath, name=None, make_name_unique=True, *args):
        name = name or origpath.rsplit("/", maxsplit=1)[-1]
        self.last_added_block = Block(self.eng.add_block(origpath,
                                                         self.path + "/" + name, 
                                                         "MakeNameUnique", "on" if make_name_unique else "off", 
                                                         *args),
                                      eng=self.eng)
        return self
    
    def finds(self, *args):
        if len(args)%2 == 1:            
            finds = self.eng.find_system(self.path, "Name", *args)
        else:
            finds = self.eng.find_system(self.path, *args)
        blocks = []
        for h in finds:
            bt = self.eng.get_param(h, "BlockType") 
            if bt == "SubSystem":
                blocks.append(Subsystem(h, eng=self.eng))
            else:
                blocks.append(Block(h, eng=self.eng))
        return blocks
    
    def find(self, *args):
        if len(args)%2 == 1:            
            finds = self.eng.find_system(self.path, "Name", *args)
        else:
            finds = self.eng.find_system(self.path, *args)
        blocks = []
        for h in finds:
            bt = self.eng.get_param(h, "BlockType") 
            if bt == "SubSystem":
                blocks.append(Subsystem(h, eng=self.eng))
            else:
                blocks.append(Block(h, eng=self.eng))
            break
        try:
            return blocks[0]
        except:
            return None