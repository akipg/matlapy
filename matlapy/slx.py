from pathlib import Path

class Slx:
    def __init__(self, desiredName, eng, saveTo=None) -> None:
        self.__desiredName = desiredName
        self.eng = eng
        
        # if saveTo is None:
        #     saveTo = Path()
        
        self.h = None

    
    @property
    def name(self):
        if self.h is not None:
            return self.eng.get_param(self.h, "Name")
        else:
            return self.__desiredName
    @name.setter
    def name(self, new_name):
        self.__desiredName = new_name
        self.h = None
    
    @property
    def MDLInfo(self):
        return self.eng.Simulink.MDLInfo(self.name)
    
    @property
    def info(self):
        return self.MDLInfo
    
    @property
    def inports(self):
        return self.eng.matlapy.getMdlInports(self.name)
    
    @property
    def outports(self):
        return self.eng.matlapy.getMdlOutports(self.name)
    
    def force_close(self):
        self.eng.close_system(self.h, 0, "CloseReferencedModels", "on", nargout=0)
        return self
    
    def close(self, ForceClose=True, CloseReferencedModels=True, SaveBeforeSave=False):
        if SaveBeforeSave:
            self.save()
        self.eng.close_system(self.h,
                              0 if ForceClose else 1,
                              "CloseReferencedModels", "on" if CloseReferencedModels else "off",
                              nargout=0)
        return self
        
    def new(self, name=None):
        self.h = self.eng.new_system(name or self.__desiredName, nargout=1)
        self.save()
        return self
    
    def renew(self):
        self.force_close()
        self.new()
        return self
    
    def save(self):
        self.eng.save_system(self.h, nargout=0)
        return self
        
    def load(self, name=None):
        self.h = self.eng.load_system(name or self.__desiredName)
        return self

    def open(self):
        self.eng.open_system(self.h)
        return self