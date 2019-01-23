# irmet
[![PyPI](https://img.shields.io/pypi/v/irmet.svg)](https://pypi.org/project/irmet/)

Evaluation measures for Information Retrieval.
Please call this library *"I-R-met"*.

## Installation
Install via `pip`

```
$ pip install irmet
```

## Evaluation Measures
- NDCG (Normalized Discounted Cumulative Gain)
- AUC (Area Under the Curve)

## Usage as a package
### NDCG
```python
from irmet import NDCG

#                  <scores>
#               ↓  ↓  ↓  ↓  ↓
ranking_list = [2, 0, 1, 0, 1]
#      <rank> → 1  2  3  4  5

ndcg_score = ndcg(ranking_score, topk=3)
# >>> 0.8472668887613066
```

## Usage as a command line tool
WIP.
