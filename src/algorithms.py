from collections import Counter
from itertools import combinations
from typing import Iterable

from src.bitmap import Bitmap


Basket = tuple[str, Iterable]


def pcy(
    baskets: Iterable[Basket],
    threshold: int,
    buckets: int,
) -> list[tuple]:
    item_counts = Counter()
    itemset_counts = [0] * buckets

    for basket in baskets:
        for item in basket[1]:
            item_counts[item] += 1
        for itemset in combinations(basket[1], 2):
            itemset_counts[hash(itemset) % buckets] += 1

    freq_items = [item for item, count in item_counts.items() if count > threshold]
    del item_counts

    bitmap = Bitmap(buckets)
    for i in range(buckets):
        if itemset_counts[i] > threshold:
            bitmap.set(i)
    del itemset_counts

    return [
        itemset
        for itemset in combinations(freq_items, 2)
        if bitmap.get(hash(itemset) % buckets)
    ]
