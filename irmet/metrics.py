# -*- coding: utf-8 -*-
import numpy as np
from functools import reduce
from operator import add

def AUC(scores):
    """Area Under the Curve

    params
    ------
    scores : ndarray, shape (n_combination, 3)
             Each 3d row consists of (idx, jdx, indicator).
             If rank(idx|c) < rank(jdx|c), the indicator is 1;
             0 otherwise.
             You have to reshape scores in advance.

             e.g.
             [[0, 1, 1], [0, 2, 1], [0, 4, 0], ...]

    returns
    -------
    AUC    : float
             The higher the AUC score, the better.
    """
    pos_indices = np.unique(scores[:,0])
    neg_indices = np.unique(scores[:,1])
    indicators = scores[:,2]
    assert scores.shape[1] == 3, "# of dimenstion in rows must be 3"
    assert len(set(pos_indices) & set(neg_indices)) == 0, "pos_indices AND neg_indices must be empty set"
    assert set(np.unique(indicators)) | {0, 1} == {0, 1}, "indicators must be subset of {0, 1}"
    n_pos = len(pos_indices)
    n_neg = len(neg_indices)
    return reduce(add, indicators) / (n_pos * n_neg)

if __name__ == "__main__":
    auc_test_data = np.array([
            [0, 1, 1],
            [0, 3, 1],
            [0, 4, 0], # <- irregular
            [2, 1, 1],
            [2, 3, 1],
            [2, 4, 1],
        ])
    # [START test functions]
    assert AUC(auc_test_data) == (5 / 6), "Test failed"
    print("Clear all tests. yey!")
