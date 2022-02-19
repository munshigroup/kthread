import sys
import time
import unittest

from kthread import KThread

def infinite_loop_func():
    while True:
        sys.stdout.write("KThread test\n")
        sys.stdout.flush()
        time.sleep(0.5)
        
class DefaultKThreadTestCase(unittest.TestCase):
    def setUp(self):
        self.kthread = KThread(name = "DefaultKThreadTestThread", target = infinite_loop_func)
        
    def runTest(self):
        self.kthread.start()
        self.assertTrue(self.kthread.is_alive(), "KThread failed to start")
        # let it run for some time
        time.sleep(5)
        self.kthread.terminate()
        # give it time to process exception
        time.sleep(1)
        self.assertFalse(self.kthread.is_alive(), "KThread failed to stop")
        
    def tearDown(self):
        self.kthread.join()
        self.kthread = None

if __name__ == '__main__':
    unittest.main()
