

class BaseClass:
    ...


# noinspection PyPropertyDefinition
class Heir(BaseClass):
    def __init__(self, name):
        BaseClass.__init__(self)
        self._name = name

    @property
    def geter_name(self):
        return self._name

    @geter_name.setter
    def geter_name(self, new):
        self._name = new
        return self._name


class Fields(Heir):

    def __init__(self,new_instance,name):
        Heir.__init__(self,name)
        self.new_instance=new_instance


    def  return_fields(self):
        ...



class New_fields(Fields):

    def __init__(self,new_istacees1,new_istacees2,new_istacees,name):
        Fields.__init__(self,name,new_istacees)
        self.new_instance1=new_istacees1
        self.new_instance2=new_istacees2


    def return_fields(self):
        return self.__dict__

