# -*- coding: utf-8 -*-
from rpn import RPN


class TestComplex(object):

	def test_complex(self):
		r = RPN()
		assert r.calc('3 4 2 * 1 5 - 2 3 ^ ^ / +') == 3.0001220703125
