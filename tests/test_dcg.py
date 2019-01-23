# -*- coding: utf-8 -*-
import unittest
import numpy as np
from irmet import DCG, NDCG


class TestDcg(unittest.TestCase):

    def setUp(self):
        self.arr = np.array([2, 0, 1, 0, 1])

    def test_dcg(self):
        # [START Test of DCG]
        dcg = DCG(self.arr)
        self.assertEqual(dcg, 3.5 + (1 / np.log2(6)))
        print("arr = {}".format(self.arr))
        print("DCG: {}".format(dcg))
        # [END Test of DCG]

    def test_ndcg(self):
        # [START Test of DCG]
        ndcg = NDCG(self.arr, topk=3)
        self.assertEqual(ndcg, 3.5 / (3.5 + (1 / np.log2(3))))
        print("arr = {}".format(self.arr))
        print("nDCG: {}".format(ndcg))
        # [END Test of DCG]
