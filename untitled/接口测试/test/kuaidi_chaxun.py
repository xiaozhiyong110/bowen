from 接口测试.config import kuaidi
from 接口测试.data.kuaidi_duqu import shuju
import unittest
class kuaidi_test(unittest.TestCase):
     ss=shuju()
     def test_1(self):
          aa=kuaidi.kuaidi().cha_xiangqing(self.ss[0][0])
          self.assertEqual(aa['errMsg'],'订单或配件信息为空！')
     def test_2(self):
          bb=kuaidi.kuaidi().cha_xiangqing(self.ss[3][0])
          self.assertEqual(bb['status'],1)
if __name__=='__main__':
     unittest.main()
