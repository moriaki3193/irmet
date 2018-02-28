# -*- coding: utf-8 -*-
import numpy as np


def _calc_numer(rels):
    """Calculate numerator of DCG

    params
    ------
    rels :
        np.ndarray, shape = (n_entities, )

    return
    ------
    numer :
        np.ndarray, The numerator of DCG
    """
    return np.array([2.0 ** rel - 1 for rel in rels])


def _calc_denom(n_entities):
    """Calculate denominator of DCG

    params
    ------
    n_entities :
        int, # of entities.

    return
    ------
    denom :
        np.ndarray, The denominator of DCG
    """
    return np.log2(np.arange(2, n_entities + 2))



def DCG(rels):
    """Calculate DCG based on given relevances of entities.

    params
    ------
    rels :
        array-like, shape = (n_entities, )
        i-th element represents the relevance score of i-th item.

    return
    ------
    dcg :
        float, The value of DCG.
    """
    numer = _calc_numer(rels)
    denom = _calc_denom(len(rels))
    return (numer / denom).sum()


def nDCG(rels, topk=None):
    """Calcurate nDCG based on given relevances of entities.

    params
    ------
    rels :
        array-like, shape (n, )
        i-th element represents the relevance score of i-th item.
    topk :
        int, k of nDCG@`k`
        default to None,
        which means all of the relevance will be considerd.

    return
    ------
    ndcg :
        float, The value of nDCG.
    """
    opt_rels = np.sort(rels)[::-1]
    last_idx = -1 if topk is None else topk
    dcg_obs = DCG(rels[:last_idx])
    dcg_opt = DCG(opt_rels[:last_idx])
    return dcg_obs / dcg_opt
