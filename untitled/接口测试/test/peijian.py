from 接口测试.config import dingdan
from 接口测试.data.dingdan_duqu import shuju
import unittest
class pei(unittest.TestCase):
    ss=shuju()
    def test_1(self):
        b=dingdan.peijian().cha_mingxi(self.ss[0][0])
        self.assertEqual(b['errMsg'],'处理成功')
    def test_2(self):
        aa=dingdan.peijian().cha_mingxi(self.ss[3][0])
        self.assertNotIn('处理成功',aa)
if __name__=='__main__':
    unittest.main()
