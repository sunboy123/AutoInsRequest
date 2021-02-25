#coding:utf8
from sanic import Sanic
from sanic.response import json
from loguru import logger
from config import Python

import re
#暴力处理跨域
from sanic_cors import CORS
app = Sanic("hello_example")
CORS(app)

@app.route('/code',methods=['POST'])
async def test(request):
    print(dir(request))
    print(1111,type(request.json))
    message = {"msg":"","data":"","code":0}
    language = request.json["language"]
    url = request.json["url"] 
    method = request.json["method"]
    args = request.json["args"]
    try:
        headers = format_headers(request.json["request_header"])
        if language == "python":
            message["msg"] = Python.code_str.format(url,)
            message["code"] = 200
        else:
            message["msg"] = "咱不支持除python之外的语言代码转换"
            message["code"] = 100
        return json(message)
    except Exception as e:
        logger.error(e)
        return json({"msg":"输入请求参数格式有误"})
        

def format_headers(hesder):
     fd = {}
     header_list = re.split('\n',hesder)
     for h in header_list:
         try:
            h_index = h.index(':')
            key,value = h[:h_index],h[index+1:]
            fd[key]=value
        except Exception as e:
            logger.error(e)
    return fd


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=9000)