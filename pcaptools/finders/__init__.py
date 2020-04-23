from . import qos_info

class FinderList:   
    _finders = {'qos_info': qos_info}
    
    @classmethod
    def get(cls, name):
        return cls._finders.get(name, None)
    