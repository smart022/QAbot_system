from . import LayerBase
from . import LayerType,BusinessType

class BB(LayerBase.LayerBase):
    def __init__(self,config_path):
        print('bb__init__')
        super().__init__(config_path,LayerType.BB)
        
        self._BType = BusinessType.Default # config fix later
        self._model_type = None
        self._model_path = None
        
    def test(self):
        print(self.config)
        print(self.task_type)
        

    def _model_func(self,model_type,model_path):
        pass
        #return ModelBase()

    def _main_func(self,orig_text_input):

        #=_main_func()
        pass
    
    def get_btype(self):
        return self._BType

    def deal(self):
        ret=_main_func(orig_text_input)

        ret_json=dict({
                answer:ret[0],
                info:None,
                other_info:None,
            })

        return ret_json
    def __repr__(self):
        par_info=super().__repr__()
        return par_info+' BusinessBase'