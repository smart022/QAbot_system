from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from datetime import timedelta
from elasticsearch import Elasticsearch
#from dialog_current_cot import Dialog_cot
from Utils.Dialog.dialog_current_cot import Dialog_cot
## es
es = Elasticsearch(['http://120.78.222.31:9200/'],port=9200)
index_name = 'my_index'
class Recall:
    def __init__(self,es,index_name):
        self.es = es
        self.index_name = index_name
        self.q_data={
        "query":{
            "match":{ # 指定查询类型为 match
                # 查询 name 中有 New 或者 York 的文档
                "left": {
                "query": None,
                "analyzer": "ik_max_word"
                }
                }
            }
        }
    def set_sent(self,sent):
        self.q_data['query']['match']['left']['query'] = sent

    def get_response(self,input):
        res = self.query(str(input))
        return self.gen_react(res)

    def query(self,sent):
        self.set_sent(sent)
        res=es.search(index=self.index_name,body=self.q_data)
        return res
    def gen_react(self, res):
        assert res is not None and res['_shards']['successful']==1
        hits_len=res['hits']['total']['value']
        
        if hits_len ==0:
            return "我不知道"
        hits=res['hits']['hits']
        res_cot=[]
        for i in range(len(hits)):
            res_tmp = hits[i]['_source']['right']
            res_cot.append(res_tmp)
        return self.match("",res_cot)

    def match(self,ctx,res_list):
        return res_list[0]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
socketio = SocketIO(app)
recall=Recall(es,index_name)


d_cot=Dialog_cot()

@socketio.on('connect')
def connect():
    uid = request.sid
    print("connect: ",uid)
    emit('chat-message',"你好朋友！",room=uid)
    
    #dialog_save_cot[uid]=[]
    d_cot.init(uid)


@socketio.on('disconnect')
def disconnect():
    print("close: ",request.sid)
    d_cot.delelt(uid)
    #del dialog_save_cot[request.sid]


@socketio.on('chat-message')
def msg_handle(msg):
    uid = request.sid
    d_cot.set(uid,msg)
    #dialog_save_cot[uid].append(msg)
    ## server logging

    print('recv {} from {}'.format(msg,uid))
    print('cur: ',d_cot.get(uid))
    try:
        ret = recall.get_response(msg)
        # request.sid = session id == every user per session only unchanged
        # 
        #uid=request.sid
        emit('chat-message',ret,room=request.sid)
    except:
        emit('system-message',"err",room=request.sid)
    


@app.route('/chatbot')
def index():
    return render_template('app_index.html')

if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1', debug=1)