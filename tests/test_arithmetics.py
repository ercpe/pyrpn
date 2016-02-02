# -*- coding: utf-8 -*-
import math
from rpn import RPN


class TestArtithmetics(object):

	def test_sin(self):
		assert RPN().calc('1 SIN') == 0.8414709848078965

	def test_cos(self):
		assert RPN().calc('1 COS') == 0.5403023058681398

	def test_log(self):
		assert RPN().calc('10 LOG') == 2.302585092994046

	def test_exp(self):
		assert RPN().calc('1 EXP') == 2.718281828459045

	def test_sqrt(self):
		assert RPN().calc('2 SQRT') == 1.4142135623730951
		assert RPN().calc('4 SQRT') == 2.0

	def test_atan(self):
		assert RPN().calc('4 ATAN') == 1.3258176636680326

	def test_abs(self):
		assert RPN().calc('0 ABS') == 0
		assert RPN().calc('1 ABS') == 1
		assert RPN().calc('-1 ABS') == 1
		assert RPN().calc('-0.1234 ABS') == 0.1234

	def test_deg2rad(self):
		assert RPN().calc('180 DEG2RAD') == math.pi

	def test_rad2deg(self):
		x = RPN().calc('%s RAD2DEG' % math.pi)
		assert int(x) == 180.0


