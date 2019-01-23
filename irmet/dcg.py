# -*- coding: utf-8 -*-
"""A variants of Discounted Cumulative Gain.
"""
from typing import Optional, Sequence
import numpy as np
from .types import Scalar


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


def NDCG(rels: Sequence[Scalar], topk: Optional[int] = None) -> Scalar:
    """Compute NDCG based on given relevances of entities.

    Parameters:
        rels: array-like, shape (n, )
              i-th element represents the relevance score of i-th item.
        topk: int, k for NDCG@`k`. defaults to None.
              all of the relevance scores will be considerd if k is None.

    Retuls:
        ndcg: NDCG score
    """
    obs_rels: Sequence[Scalar]
    opt_rels: Sequence[Scalar]
    if topk is None:
        obs_rels = rels
        opt_rels = np.sort(rels)[::-1]
    else:
        obs_rels = rels[:topk]
        opt_rels = np.sort(rels)[::-1][:topk]
    dcg_obs = DCG(obs_rels)
    dcg_opt = DCG(opt_rels)
    return dcg_obs / dcg_opt
