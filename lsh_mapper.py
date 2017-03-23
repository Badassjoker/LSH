import sys
from random import randrange

num_hashes = 20
num_per_band = 2

a_hash = [randrange(sys.maxint) for _ in range(0, num_hashes)]
b_hash = [randrange(sys.maxint) for _ in range(0, num_hashes)]


def min_hash_fn(a, b, sig):
    hashes = [((a * x) + b) % 11894 for x in sig]
    return min(hashes)


def get_min_hash_row(sig):
    hashes = [min_hash_fn(a, b, sig) for a, b in zip(a_hash, b_hash)]
    return hashes


def get_band(l, n):
    for i in xrange(0, len(l), n):
        yield frozenset(l[i:i+n])

fp = open('signature.txt', 'r')

for line in fp:
    try:
        user_id, rows = line.strip().split(' ', 1)
    except ValueError:
        continue
        
    rows = rows.strip().split(' ')

    for i in range(len(rows)):
        rows[i] = int(rows[i])

    signature = get_min_hash_row(rows)

    banded = get_band(signature, num_per_band)

    for band_id, band in enumerate(banded):
        print("%s\t%s\t%s" % (band_id, hash(band), user_id))

fp.close()