# -*- coding: utf-8 -*-
import numpy as np
from functools import reduce
from operator import add


def DCG(rels):
    """DCGを計算する関数.

    arguments
    ---------
    rels : array-like, shape (n, )
           i番目の要素はi番目のアイテムの適合度を表す.

    returns
    -------
    dcg  : float
    """
    numer = lambda x: (2 ** x - 1)
    denom = lambda i: np.log2(1 + (i + 1))
    elems = [numer(rel) / denom(idx) for idx, rel in enumerate(rels)]
    return reduce(add, elems)

def nDCG(rels, topk=None):
    """nDCGを計算する関数.

    arguments
    ---------
    rels : array-like, shape (n, )
           i番目の要素はi番目のアイテムの適合度を表す.

    returns
    -------
    ndcg : float
    """
    # [START listの場合の型変換]
    if type(rels) == list:
        rels = np.array(rels)
    # [END]
    opt_rels = np.sort(rels)[::-1]
    last_idx = -1 if topk is None else topk
    dcg_obs = DCG(rels[:last_idx])
    dcg_opt = DCG(opt_rels[:last_idx])
    return dcg_obs / dcg_opt

if __name__ == "__main__":
    arr = [2, 0, 1, 0, 1]
    dcg = DCG(arr)
    ndcg = nDCG(arr, topk=3)
    assert dcg == 3.5 + (1 / np.log2(6))
    assert ndcg == 3.5 / (3.5 + (1 / np.log2(3)))
    print("arr = {}".format(arr))
    print("DCG: {}".format(dcg))
    print("nDCG: {}".format(ndcg))
