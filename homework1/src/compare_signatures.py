"""
compare_signatures.py

Compares two MinHash signatures to estimate document similarity.
"""

def signature_similarity(sig1, sig2):
    """
    Compute the fraction of components that agree between two MinHash signatures.

    Args:
        sig1 (list[int]): first signature
        sig2 (list[int]): second signature

    Returns:
        float: similarity value in [0, 1]
    """
    assert len(sig1) == len(sig2), "Signatures must have the same length"
    agree = sum(1 for i in range(len(sig1)) if sig1[i] == sig2[i])
    return agree / len(sig1)
