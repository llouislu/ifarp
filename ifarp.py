#!/usr/bin/env python3

import csv, math, re, struct, sys
from ipdb import set_trace

def rng(bgn, end, loc):
    while bgn < end:
        suff = int(math.log2(end-bgn))
        loc = re.sub('\t$', '', loc).replace('\t', ' ').strip()
        newrow = [bgn, end, loc]
        rows.append(newrow)
        bgn += 1 << suff

rows = []
with open(sys.argv[1], 'rb') as f:
    a = f.read()
    data = struct.unpack('>I', a[:4])[0]
    i = 4+256*4
    bgn = 0
    while 1:
        end = struct.unpack('>I', a[i:i+4])[0]+1
        offset = struct.unpack('I', a[i+4:i+7]+b'\0')[0]
        if offset > 0:
            length = a[i+7]
            t = data-1024+offset
            rng(bgn, end, a[t:t+length].decode())
        if end == 0x100000000:
            break
        i += 8
        bgn = end
with open(sys.argv[2], 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    spamwriter.writerows(rows)