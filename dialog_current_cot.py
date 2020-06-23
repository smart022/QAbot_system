class Dialog_cot():
    def __init__(self):
        self.cot={}

    def init(self,uid):
        self.cot[uid]=[]

    def get(self,uid):
        return self.cot.get(uid,None)

    def set(self,uid,msg):
        if self.get(uid) is None: return
        self.cot[uid].append(msg)

    def delelt(self,uid):
        if self.get(uid) is None: return
        del self.cot[uid]


