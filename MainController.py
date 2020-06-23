import BusinessLogic as BL

class MainController():
    def __init__(self,session_id):
        self._QU_layer = None
        self._Business_layers = { i:None for i in BL.BusinessType}
        self._ResponseGen_layer = None
        self._cur_btype = None
        self._sid = session_id

    def _switch(flag):
        return self._Business_layers_entity[flag]

    def registerLayer(self,layerType,layerEntity):
        if layerType == BL.LayerType.QU:
            self._QU_layer = layerEntity
        elif layerType == BL.LayerType.BB:

            # each single btype holds only one entity
            self._Business_layers[layerEntity.get_btype()] = layerEntity
        elif layerType == BL.LayerType.RG:
            self._ResponseGen_layer = layerEntity

        print(layerEntity,' register!')
    def test(self):
        print(self._Business_layers )

    def toggle(self,end_busi):
        if end_busi: self._cur_btype = None

    def _check_ok(self):# check all need is ready for a single reply
        return True

    def run(self,text_input):
        assert self._check_ok()==True
        
        if self._cur_btype is None: # first enter dialog
            orig_text,_,btype=self._QU_layer.deal(text_input)
            #b_entity_pos=_switch(btype)
            self._cur_btype = btype
            ret=_switch(self._cur_btype).deal(ret)
            ret=self._ResponseGen_layer.deal(ret)
        else: # no end business
            ret=self._switch(self._cur_btype).deal(text_input)
            ret=self._ResponseGen_layer.deal(ret)
            
        return ret