# -*- coding: utf-8 -*-
from unittest import TestCase
from common_utils import *
from sln_1_100.solution_91_100 import Solution_91_100


class Test_Solution_91_100(TestCase):
    def setUp(self) -> None:
        self.sln = Solution_91_100()

    def test_numDecodings(self):
        self.assertEqual(self.sln.numDecodings("0"), 0)
        self.assertEqual(self.sln.numDecodings("00"), 0)
        self.assertEqual(self.sln.numDecodings("1"), 1)
        self.assertEqual(self.sln.numDecodings("10"), 1)
        self.assertEqual(self.sln.numDecodings("12"), 2)
        self.assertEqual(self.sln.numDecodings("226"), 3)

    def test_reverseBetween(self):
        ret = self.sln.reverseBetween(build_linked_list([1, 2, 3, 4, 5]), 2, 4)
        assert print_linked_list(ret) == '1->4->3->2->5'

        ret = self.sln.reverseBetween(build_linked_list([1, 2, 3, 4, 5]), 1, 4)
        assert print_linked_list(ret) == '4->3->2->1->5'

        ret = self.sln.reverseBetween(build_linked_list([1, 2, 3, 4, 5]), 2, 5)
        print_linked_list(ret)

    def test_restoreIpAddresses(self):
        ret = self.sln.restoreIpAddresses("25525511135")
        self.assertEqual(ret, ['255.255.11.135', '255.255.111.35'])
        ret1 = self.sln.restoreIpAddresses("02525511135")
        # print(ret1)
        self.assertEqual(ret1, [])
        ret2 = self.sln.restoreIpAddresses("25025511135")
        self.assertEqual(ret2, ['250.255.11.135', '250.255.111.35'])
        self.assertEqual(self.sln.restoreIpAddresses("010010"), ["0.10.0.10", "0.100.1.0"])
        self.assertEqual(self.sln.restoreIpAddresses('0000'), ["0.0.0.0"])
        self.assertEqual(self.sln.restoreIpAddresses("101023"),
                         ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"])
        self.assertEqual(self.sln.restoreIpAddresses("9999999"),
                         ["9.99.99.99", "99.9.99.99", "99.99.9.99", "99.99.99.9"])
        s = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
        self.assertEqual(self.sln.restoreIpAddresses(s), [])
        # print(ret1)
        # self.assertEqual(ret, ['255.255.11.135', '255.255.111.35'])
