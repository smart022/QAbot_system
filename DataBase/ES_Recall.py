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