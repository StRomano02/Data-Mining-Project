"""
compare_sets.py

Implements the Jaccard similarity function between two sets.
"""

def jaccard_similarity(set1, set2):
    """
    Compute Jaccard similarity between two sets.

    Args:
        set1 (set): first set (e.g., hashed shingles)
        set2 (set): second set

    Returns:
        float: Jaccard similarity in range [0, 1]
    """
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0.0
