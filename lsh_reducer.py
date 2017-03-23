import sys

prev_band_id, prev_band_hash = None, None
cluster = []
cid = 0

fp = open('result.txt', 'w')

for line in sys.stdin:
    band_id, band_hash, user_id = line.strip().split("\t", 3)

    if prev_band_id is None and prev_band_hash is None:
        prev_band_id, prev_band_hash = band_id, band_hash

    if prev_band_id is band_id:
        if prev_band_hash == band_hash:
            cluster.append(user_id)
        else:
            fp.write('%s, %s\n' % (cid, cluster))
            cluster = [user_id]
    else:
        fp.write('%s, %s\n' % (cid, cluster))
        cluster = [user_id]
        cid += 1
    prev_band_id, prev_band_hash = band_id, band_hash

fp.close()