# -*- coding: utf-8 -*-
from rpn import RPN


class TestCompare(object):

	def test_min(self):
		r = RPN()

		assert r.calc('1 2 MIN') == 1
		assert r.calc('3 2 MIN') == 2

	def test_max(self):
		r = RPN()

		assert r.calc('1 2 MAX') == 2
		assert r.calc('3 2 MAX') == 3

	def test_limit(self):
		r = RPN()

		assert r.calc('1 1 10 LIMIT') == 1
		assert r.calc('10 1 10 LIMIT') == 10
		assert r.calc('0 1 10 LIMIT') is None
		assert r.calc('-1 1 10 LIMIT') is None
		assert r.calc('100 1 10 LIMIT') is None
