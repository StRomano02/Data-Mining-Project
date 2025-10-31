"""
shingling.py

Contains functions to create k-shingles (substrings of length k)
from a text document and convert them into a set of integer hashes.
"""

def create_shingles(text: str, k: int):
    """
    Create a set of k-shingles from the given text.

    Args:
        text (str): document text (e.g., a lasagna recipe)
        k (int): length of each shingle (e.g., 10 characters)

    Returns:
        set[str]: a set of unique k-length strings
    """
    # Normalize text: lowercase and remove newlines
    text = text.lower().replace("\n", " ")

    shingles = set()
    # Slide a window of length k over the text
    for i in range(len(text) - k + 1):
        shingle = text[i:i+k]
        shingles.add(shingle)

    return shingles


def hash_shingles(shingles):
    """
    Convert each shingle into an integer using Python's built-in hash function.

    Args:
        shingles (set[str]): set of k-shingles

    Returns:
        set[int]: hashed integer representation of each shingle
    """
    return set(hash(s) for s in shingles)
