from MainController import MainController

from BusinessLogic.QU import QU
from BusinessLogic.BB import BB
from BusinessLogic.RG import RG
from BusinessLogic import LayerType
from Utils.ConfigBase import ConfigBase

if __name__ == '__main__':
    ctl=MainController('sid')
    
    qu=QU('ww')
    bb=BB('aa')
    rg=RG('daw')

    ctl.registerLayer(LayerType.QU,qu)
    ctl.registerLayer(LayerType.BB,bb)
    ctl.registerLayer(LayerType.RG,rg)
    
    tmpConfig=ConfigBase('tmpfig.json')

    #config_dict=dict({'task':'hah','params':'ddd'})
    #tmpConfig.SetConfig(config_dict)
    tmpConfig.Read()
    tmpConfig.show()

