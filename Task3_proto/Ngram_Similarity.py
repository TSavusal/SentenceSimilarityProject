def ngrams(sequence, n, pad_left=False, pad_right=False, pad_symbol=None):
    """
    A utility that produces a sequence of ngrams from a sequence of items.
    """

    if pad_left:
        sequence = chain((pad_symbol,) * (n-1), sequence)
    if pad_right:
        sequence = chain(sequence, (pad_symbol,) * (n-1))
    sequence = list(sequence)

    count = max(0, len(sequence) - n + 1)
    return [tuple(sequence[i:i+n]) for i in range(count)] 