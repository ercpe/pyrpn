# -*- coding: utf-8 -*-
from rpn import RPN


class TestBooleanOperators(object):
	def test_less_than(self):
		r = RPN()
		self._assert_result(r.calc('1 2 LT'))
		self._assert_result(r.calc('2 2 LT'), False)
		self._assert_result(r.calc('3 2 LT'), False)

	def test_less_than_or_equal(self):
		r = RPN()
		self._assert_result(r.calc('1 2 LE'))
		self._assert_result(r.calc('2 2 LE'))
		self._assert_result(r.calc('3 2 LE'), False)

	def test_greater_than(self):
		r = RPN()
		self._assert_result(r.calc('2 1 GT'))
		self._assert_result(r.calc('2 2 GT'), False)
		self._assert_result(r.calc('2 3 GT'), False)

	def test_greater_than_or_equal(self):
		r = RPN()
		self._assert_result(r.calc('2 1 GE'))
		self._assert_result(r.calc('2 2 GE'))
		self._assert_result(r.calc('2 3 GE'), False)

	def test_equal(self):
		r = RPN()
		self._assert_result(r.calc('2 2 EQ'))
		self._assert_result(r.calc('2 1 EQ'), False)

	def test_not_equal(self):
		r = RPN()
		self._assert_result(r.calc('2 1 NE'))
		self._assert_result(r.calc('2 2 NE'), False)

	def test_if(self):
		r = RPN()

		assert r.calc('1 2 3 IF') == 2
		assert r.calc('0 2 3 IF') == 3

	def _assert_result(self, result, b=True):
		assert isinstance(result, int) and not isinstance(result, bool), "Boolean operators must return 0 or 1 instead of True and False"
		assert result == int(b)

