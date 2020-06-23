import json
'''
All config file is Json type file,
the format shows below
{
    'task':'',
    'params':[...]
    
}

'''
class ConfigBase():
    def __init__(self,path):
        self._config_dict=None
        self._path = path
    def show(self):
        print(self._config_dict)
    
    def SetPath(self):
        pass
    def SetConfig(self,config):
        assert isinstance(config,dict) 
        self._config_dict = config

    def Read(self):
        with open(self._path,'r',encoding='utf-8') as f: 
            try:
                self._config_dict = json.load(f)
            except: pass

    def Write(self):
        assert self._config_dict is not None
        assert self._config_dict.get('task',None) is not None
        assert self._config_dict.get('params',None) is not None
        with open(self._path,'w',encoding='utf-8') as f: 
            try:
                json.dump(self._config_dict, f)
            except: pass

    def __repr__(self):
        return "Config base"