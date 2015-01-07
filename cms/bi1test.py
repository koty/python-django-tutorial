# -*- coding: utf-8 -*-

import unittest
from cms.biz1 import Biz1


class TestSequenceFunctions(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    
    def setUp(self):
        print("setUp")

    def test_foo(self):
        sut = Biz1()
        result = sut.plus(1, 2)
        self.assertEqual(result, 3, "1+2 != 3")
        self.assertEqual(sut.instance_val1, 3)
#        self.assertEqual(Biz1.instance_val1, 3)
        self.assertEqual(Biz1.class_val1, 3)