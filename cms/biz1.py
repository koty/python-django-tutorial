# -*- coding: utf-8 -*-

class Biz1:
    class_val1 = 0

    def __init__(self):
        self.instance_val1 = 0

    def plus(self, num1, num2):
        result = num1 + num2
        self.instance_val1 = result
        Biz1.class_val1 = result
        return result
        