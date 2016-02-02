# -*- coding: utf-8 -*-
from __future__ import division
import operator


class RPNOperator(object):

	def __init__(self, func, num_elements):
		self.func = func
		self.num_elems = num_elements

	def __call__(self, tokens, pos):
		args = tokens[pos - self.num_elems:pos]
		tokens[pos-self.num_elems:pos+1] = [self.func(*tuple(args))]
		return tokens


def operator_limit(value, low, high):
	if low <= value <= high:
		return value
	return None


OPERATORS = {
	# MATH
	'+': RPNOperator(operator.add, 2),
	'-': RPNOperator(operator.sub, 2),
	'*': RPNOperator(operator.mul, 2),
	'/': RPNOperator(lambda a, b: a / b, 2),
	'^': RPNOperator(operator.pow, 2),

	# BOOL
	'LT': RPNOperator(lambda a, b: int(operator.lt(a, b)), 2),
	'LE': RPNOperator(lambda a, b: int(operator.le(a, b)), 2),
	'GT': RPNOperator(lambda a, b: int(operator.gt(a, b)), 2),
	'GE': RPNOperator(lambda a, b: int(operator.ge(a, b)), 2),
	'EQ': RPNOperator(lambda a, b: int(operator.eq(a, b)), 2),
	'NE': RPNOperator(lambda a, b: int(operator.ne(a, b)), 2),

	#UN, ISINF
	'IF': RPNOperator(lambda a, b, c: b if isinstance(a, int) and a == 1 else c, 3),

	# COMPARE
	'MIN': RPNOperator(min, 2),
	'MAX': RPNOperator(max, 2),
	# MINNAN, MAXNAN
	'LIMIT': RPNOperator(operator_limit, 3),
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
					op = OPERATORS[token]

					assert i >= op.num_elems

					tokens = op(tokens, i)
					break

		return tokens[0]
