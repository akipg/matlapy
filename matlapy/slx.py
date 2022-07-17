from pathlib import Path

class Slx:
    def __init__(self, desiredName, eng, desiredSuffix="slx", saveTo=None) -> None:
        self.__desiredName = desiredName
        self.__desiredSuffix = desiredSuffix
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
    def filepath(self):
        return str(self.eng.matlapy.getMdlFilename(self.name))
    
    @property
    def parentpath(self):
        return str(Path(self.filepath).parent)
    
    @property
    def suffix(self):
        try:
            return Path(self.filepath).suffix
        except:
            return self.__desiredSuffix
    
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
        mdlname = name or self.name
        self.h = self.eng.new_system(f"{mdlname}", nargout=1)
        self.save(f"{mdlname}.{self.suffix}")
        return self
    
    def renew(self):
        self.force_close()
        self.new()
        return self
    
    def save(self, filepath=None):
        if filepath:
            self.eng.save_system(filepath, nargout=0)
        else:
            self.eng.save_system(self.h, nargout=0)
            
        return self
        
    def load(self, name=None):
        self.h = self.eng.load_system(name or self.__desiredName)
        return self

    def open(self):
        self.eng.open_system(self.h)
        return self
    
    def duplicate(self):
        success = False
        num = 1
        duplicatedName = f"Copy_of_{self.name}"
        while True:
            if num > 5000:
                raise Exception("Duplicate filename cannot be set.")
            if Path(duplicatedName + "." + self.suffix).exists():
                num += 1
                duplicatedName = f"Copy_{num}_of_{self.name}"
            else:
                break
        return Slx(duplicatedName, eng=self.eng, desiredSuffix=self.suffix).new()
            

        