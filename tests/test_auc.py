# -*- coding: utf-8 -*-
import unittest
import numpy as np
from irmet.auc import AUC


class TestAuc(unittest.TestCase):

    def test_auc(self):
        # [START Test of AUC]
        auc_test_data = np.array([
                [0, 1, 1],
                [0, 3, 1],
                [0, 4, 0],  # <- irregular
                [2, 1, 1],
                [2, 3, 1],
                [2, 4, 1],
            ])
        self.assertEqual(AUC(auc_test_data), 5 / 6)
        # [END Test of AUC]
