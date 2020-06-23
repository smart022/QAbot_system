from . import LayerBase
from . import LayerType

class RG(LayerBase.LayerBase):
    def __init__(self,config_path):
        print('RG__init__')
        super().__init__(config_path,LayerType.RG)
        

    def _struct_info_gen(self):
        # {}
        #
        #
        pass

    def _manufact(self,last_input):
    #   output info definiton:
    #   1. direct answer: str
    #   2. systerm info: str
    #   3. struct info: option jsonfy
    #
        ret = {}
        return ret

    def test(self):
        print(self.config)
        print(self.task_type)

    def deal(self,last_input):
        ret=_manufact(last_input)

        return ret
    def __repr__(self):
        par_info=super().__repr__()
        return par_info+' ResponseGenerator'