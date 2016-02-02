# -*- coding: utf-8 -*-
from rpn import RPN


class TestSimpleMath(object):

	def test_add(self):
		assert RPN().calc('1 2 +') == 3

	def test_sub(self):
		assert RPN().calc('1 2 -') == -1
		assert RPN().calc('2 2 -') == 0

	def test_mul(self):
		assert RPN().calc('1 2 *') == 2

	def test_div(self):
		assert RPN().calc('1 2 /') == 0.5
		assert RPN().calc('10 5 /') == 2

	def test_floor(self):
		assert RPN().calc('10.5 FLOOR') == 10
		assert RPN().calc('0.1 FLOOR') == 0
		assert RPN().calc('0 FLOOR') == 0

	def test_ceil(self):
		assert RPN().calc('10.5 CEIL') == 11
		assert RPN().calc('0.1 CEIL') == 1
		assert RPN().calc('0 CEIL') == 0
