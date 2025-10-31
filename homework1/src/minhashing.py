"""
minhashing.py

Implements functions to create MinHash signatures
using a collection of random hash functions.
"""

import random

def generate_hash_functions(num_hashes, max_shingle_id):
    """
    Generate 'num_hashes' independent hash functions.

    Each hash function is defined as: h(x) = (a*x + b) % max_shingle_id

    Args:
        num_hashes (int): number of hash functions
        max_shingle_id (int): maximum modulus value

    Returns:
        list[tuple[int, int]]: list of (a, b) parameters
    """
    return [(random.randint(1, max_shingle_id), random.randint(0, max_shingle_id))
            for _ in range(num_hashes)]


def compute_minhash_signature(shingle_set, hash_functions, max_shingle_id):
    """
    Compute a MinHash signature for a set of hashed shingles.

    Args:
        shingle_set (set[int]): set of hashed shingles
        hash_functions (list[tuple[int, int]]): hash function parameters
        max_shingle_id (int): modulus for hash functions

    Returns:
        list[int]: MinHash signature vector
    """
    signature = []
    for (a, b) in hash_functions:
        # For each hash function, compute the minimum hash value across shingles
        min_hash = min(((a * x + b) % max_shingle_id) for x in shingle_set)
        signature.append(min_hash)
    return signature
