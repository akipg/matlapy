from pathlib import Path

import matlapy.matlab_connection

class Block:
    def __init__(self, h=None, eng=None):
        if eng is None:
            self.eng = matlapy.matlab_connection.connection.eng
        else:
            self.eng = eng
        if self.eng and h:
            self.h = self.eng.get_param(h, "Handle")    

    @property
    def pos(self):
        return self.eng.get_param(self.h, "Position")[0]

    @pos.setter
    def pos(self, value):
        self.eng.set_param(self.h, "Position", value, nargout=0)

    @property
    def width(self):
        pos = self.pos
        return pos[2] - pos[0]

    @property
    def height(self):
        pos = self.pos
        return pos[3] - pos[1]

    @property
    def name(self):
        return self.eng.get_param(self.h, "Name")

    @property
    def parent(self):
        return self.eng.get_param(self.h, "Parent")

    @property
    def path(self):
        return self.parent + "/" + self.name

    @property
    def BlockType(self):
        return self.eng.get_param(self.h, "BlockType")

    def set_param(self, *args):
        self.eng.set_param(self.h, nargout=0, *args)
        return self

    def get_param(self, *args):
        return self.eng.get_param(self.h, *args)

    def moveTo(self, xy):
        pos = self.pos
        width = self.width
        height = self.height
        pos[0] = xy[0]
        pos[2] = xy[1]
        pos[1]= pos[0] + width
        pos[3]= pos[1] + height
        return self

    def moveX(self, dx):
        pos= self.pos
        pos[0] += dx
        pos[2] += dx
        self.pos= pos
        return self

    def moveY(self, dy):
        pos= self.pos
        pos[1] += dy
        pos[3] += dy
        self.pos= pos
        return self

    def alignTo(self, block, align=0, anchor=0, marginX=0, marginY=0):
        pos1= block.pos
        width1= block.width
        height1= block.height
        pos= pos1
        width= self.width
        height= self.height
        pos[0]= pos1[0] + width1/2.0 * (align % 3) - width/2.0 * (anchor % 3) + marginX
        pos[1]= pos1[1] + height1/2.0*int((align/3)) - height/2.0*int((anchor/3)) + marginY
        pos[2]= pos[0] + width
        pos[3]= pos[1] + height
        self.pos= pos
        return self

        """
        align, anchor:
        0 1 2
        3 4 5
        6 7 8
        """

    def connectTo(self, dstblock, dstport=1, srcport=1, auto_routing=True):
        if dstblock is None:
            raise Exception("dstblock is None.")
        parent= self.parent
        if parent != dstblock.parent:
            raise Exception(
                f"parent is missmatch, self: {parent}, dst:{dstblock.parent}")
        auto_routing= "on" if auto_routing else "Off"
        self.eng.add_line(parent, f"{self.name}/{int(srcport)}", f"{dstblock.name}/{int(dstport)}", "autoRouting", auto_routing)
        return self

    def delete(self):
        self.eng.delete_block(self.h, nargout=0)
        return self

    def copyTo(self, dstpath=None, make_name_unique=True):
        if dstpath is None:
            dstpath= self.path
            make_name_unique= "on" if make_name_unique else "off"
        return Block(self.eng.add_block(self.h, dstpath, "MakeNameunique", make_name_unique))

    def move(self):
        pass
        return self
    
if __name__ == "__main__":
    import matlab.engine
    eng_names = matlab.engine.find_matlab()
    print(eng_names)

    #self.eng = matlab.self.engine.connect_matlab(self.eng_names[0])
    