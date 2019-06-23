import requests
from 接口测试.data.kuaidi_duqu import shuju
class kuaidi(object):
    def cha_xiangqing(self,num):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/deliveryInfo"

        payload = "{\n\t\"pagrSize\":\"%s\",\n\t\"pageNo\":\"1\",\n\t\"queryTerms\":\n\t{\n\t\t\"orderNo\":\"\",\n\t\t\"partNo\":\"\"\n\t}\n}"%(num)
        headers = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrderSearch_deliveryInfo",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "d6a5abdb98fd2ee203a4ddcd7ae47d07",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "b70a1939-9c6f-4209-b6cd-6ebc11d60c3a,6328cdb5-d0d7-41f6-b8e4-2c18c978850e",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=b572c26829166c1a19a3cf21bbdd12a6; dapp.sgm.com:qa:=b572c26829166c1a19a3cf21bbdd12a6; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
            'accept-encoding': "gzip, deflate",
            'content-length': "87",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        response = requests.post(url=url, data=payload, headers=headers)
        return response.json()
if __name__=='__main__':
    for i in shuju():
        print(kuaidi().cha_xiangqing(i[0]))