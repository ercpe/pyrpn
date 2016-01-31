# -*- coding: utf-8 -*-
from rpn import RPN


class TestConstructor(object):

	def test_string(self):
		assert RPN().calc('2 3 +') == 5

	def test_iterable(self):
		assert RPN().calc((2, 3, '+')) == 5
