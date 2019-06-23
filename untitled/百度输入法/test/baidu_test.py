from 百度输入法.config import baidu_web
from 百度输入法.data import baidu_duqu
import unittest
class baidu_test(unittest.TestCase):
    ss=baidu_duqu.baidu_duqu()
    def test_1(self):
        aaa=baidu_web.baidu_web(self.ss[0])
        self.assertEqual('最新',aaa)
    def test_2(self):
        bbb=baidu_web.baidu_web(self.ss[1])
        self.assertIn('搜索',bbb)

    def test_3(self):
        ccc=baidu_web.baidu_web(self.ss[2])
        self.assertIn('搜索',ccc)
if __name__=='__main__':
    unittest.main()