# -*- coding: utf-8 -*-
from __future__ import division
import operator

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': lambda a, b: a / b,
	'^': operator.pow,
}


class RPN(object):

	def calc(self, expression, vars=None):
		vars = vars or {}
		tokens = []

		for x in expression if isinstance(expression, (list, tuple)) else expression.strip().split():
			if x in vars:
				tokens.append(vars[x])
			elif x in OPERATORS or isinstance(x, (int, float)):
				tokens.append(x)
			else:
				tokens.append(float(x) if '.' in x or 'e' in x.lower() else int(x))

		while len(tokens) > 1:
			for i, token in enumerate(tokens):
				if token in OPERATORS:
					assert i >= 2

					tokens[i-2:i+1] = [OPERATORS[token](tokens[i-2], tokens[i-1])]
					break

		return tokens[0]
