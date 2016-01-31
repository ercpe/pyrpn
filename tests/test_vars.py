# -*- coding: utf-8 -*-
from rpn import RPN


class TestVars(object):

	def test_basic_vars(self):
		r = RPN()

		assert r.calc('foo bar +', {
			'foo': 2,
			'bar': 3
		}) == 5

