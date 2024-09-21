import unittest

def myfunc():
   print(f'test 모듈 실행합니다')

class CustomTests(unittest.TestCase):
   def test_runs(self):
       myfunc()

if __name__ == '__main__':
   unittest.main()