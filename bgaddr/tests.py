# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase
from django.utils import six
from six import print_

from bgaddr import parse_address

class ParseAddressTest(TestCase):

    def _expected(self, s='', n='', ab='', e='', f='', ap=''):
        return {
            'street': s,
            'num': n,
            'ab': ab,
            'en': e,
            'fl': f,
            'ap': ap,
        }

    def test_1(self):
        inp = 'ул. бл 100Б бл. 2, ет. 3, ап. 123'
        expected = self._expected('бл', '100Б', '2', '', '3', '123')
        actual = parse_address(inp)
        self.assertEqual(expected, actual)

    def test_2(self):
        inp = '''
        № 1 А
        бл 2 Б
        вх 3 В
        ет 374916
        ап 417
        '''
        expected = self._expected('', '1 А', '2 Б', '3 В', '374916', '417')
        actual = parse_address(inp)
        self.assertEqual(expected, actual)

    def test_3(self):
        inp = '''
        ул. "Пиротска" №4
        '''
        expected = self._expected('Пиротска', '4')
        actual = parse_address(inp)
        self.assertEqual(expected, actual)

    def test_4(self):
        inp = 'ап.1 бл. 2 ул. 3 ет. 4 вх 5'
        expected = self._expected('', '3', '2', '5', '4', '1')
        actual = parse_address(inp)
        self.assertEqual(expected, actual)

    def test_5(self):
        inp = 'ап.1 ул. 3 ет. 4'
        expected = self._expected('', '3', '', '', '4', '1')
        actual = parse_address(inp)
        self.assertEqual(expected, actual)

    def test_6(self):
        inp = 'ул. "30-та" номер 89'
        expected = self._expected('30-та', '89')
        actual = parse_address(inp)
        self.assertEqual(expected, actual)
