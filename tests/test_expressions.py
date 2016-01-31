# -*- coding: utf-8 -*-
from rpn import RPN


class TestExpressions(object):

	def test_multiple(self):
		r = RPN()

		assert r.calc('2 3 + 4 *') == 20
