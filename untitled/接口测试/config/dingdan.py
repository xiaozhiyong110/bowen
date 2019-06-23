#所有的订单配置文件
import requests
from 接口测试.data import dingdan_duqu
class peijian(object):
    def cha_mingxi(self,num):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'
        header={
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderPartDetail",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "c909d3541a63a46b75f314a4e94828c0",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "a83cd467-1d78-48bb-b5ac-a93ddc4a28db,0baa422c-c6fe-422c-9d78-5251ce6669ac",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=8b9b4159924fe441e96e533a4ddf3f32; dapp.sgm.com:qa:=8b9b4159924fe441e96e533a4ddf3f32; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
            'accept-encoding': "gzip, deflate",
            'content-length': "30",
            'Connection': "keep-alive",
            'cache-control': "no-cache"}
        pyloa= "{\r\n \"partOrderItemId\": %s\r\n}"%(num)
        res=requests.post(url=url,headers=header,data=pyloa)
        return res.json()
if __name__=='__main__':
    for i in dingdan_duqu.shuju():
        peijian().cha_mingxi(i[0])