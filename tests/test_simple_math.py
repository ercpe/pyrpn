# -*- coding: utf-8 -*-
from rpn import RPN


class TestSimpleMath(object):

	def test_basic_operators(self):
		for exp, result in [
			('1 2 +', 3),
			('1 2 -', -1),
			('1 2 *', 2),
			('1 2 /', 0.5)
		]:
			assert RPN().calc(exp) == result
