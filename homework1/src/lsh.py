"""
lsh.py

Implements the Locality-Sensitive Hashing (LSH) technique
to efficiently find candidate pairs of similar documents
based on their MinHash signatures.
"""

from collections import defaultdict

def lsh_candidate_pairs(signatures, bands, rows):
    """
    Group MinHash signatures into buckets using banding
    and return candidate document pairs.

    Args:
        signatures (list[list[int]]): MinHash signatures (one per document)
        bands (int): number of bands
        rows (int): number of rows per band

    Returns:
        set[tuple[int, int]]: pairs of document indices considered as candidates
    """
    buckets = defaultdict(list)
    candidates = set()

    for doc_id, sig in enumerate(signatures):
        for b in range(bands):
            start = b * rows
            end = start + rows
            band = tuple(sig[start:end])
            # Hash each band to group similar documents
            buckets[(b, hash(band))].append(doc_id)

    # All docs that fall into the same bucket are candidate pairs
    for bucket in buckets.values():
        if len(bucket) > 1:
            for i in range(len(bucket)):
                for j in range(i + 1, len(bucket)):
                    candidates.add((bucket[i], bucket[j]))

    return candidates
