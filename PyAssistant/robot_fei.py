import requests, json


# 机器人发送消息 False True
def setFeidata(fei_url_,fei_data_,isAtAll_):
    all = "<at user_id='all'>所有人</at>" if isAtAll_ else ''

    fei_data = {"msg_type": "text",
                "content": {"text": all + f"{fei_data_}"}}

    r = requests.request('POST', fei_url_, headers={'Content-Type': 'application/json'}, data=json.dumps(fei_data))
    print(r)