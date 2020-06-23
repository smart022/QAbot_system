from . import LayerBase
from . import LayerType,BusinessType
import jieba
import jieba.posseg as pseg # 词性标注
class QU(LayerBase.LayerBase):
    def __init__(self,config_path):
        print('qu__init__')
        super().__init__(config_path,LayerType.QU)
        self.paddle_mode = False
        self.use_rule_match = True
        self.use_model_match = False
        
    def test(self):
        print(self.config)
        print(self.task_type)


    def _preprocess(self,text_input):
    #input: text (Mainly Chinese) : str
    #output: 0. original text: str
    #        1. cut text: list
    #        2. slot seq: list
        if self.paddle_mode :
            jieba.enable_paddle() #启动paddle模式。 0.40版之后开始支持，早期版本不支持
        words = pseg.cut(text_input,use_paddle=paddle_mode) #paddle模式
        
        ret2 = []
        ret3 = []
        for word, flag in words:
            ret2.append(word)
            ret3.append(flag)

        
        return text_input,ret2,ret3


    def _rule_match(self,orig_text_input,cut_text_input,slot_text):
        '''
        output: 1. 01 flag wether match rule: bool
                2. next BB type :
        '''
        if orig_text_input.startwith("__"): pass
        
        return True,BusinessType.Default

    def _model_match(self,orig_text_input,cut_text_input,slot_text):
        pass

    def deal(self,text_input):
        orig_text_input,cut_text,slot_infos=_preprocess(text_input)
        flag,Btype=_rule_match(orig_text_input,cut_text,slot_infos)

        if not flag and self.if_model_match: 
            flag,Btype =  _model_match(orig_text_input,cut_text,slot_infos)


        return orig_text_input,cut_text,Btype
    def __repr__(self):
        par_info=super().__repr__()
        return par_info+' QueryUnderstand'