#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as ifp:
    lines = [int(x.strip()) for x in ifp.readlines()]

answer=0
last=sys.maxsize
for line in lines:
    if line > last:
        answer+=1
    last = line

print('Part 1 Answer: {}'.format(answer))

answer=0
last=sum(lines[0:3])
for offset in range(1,len(lines)-2):
    # print('Sample: {}'.format(lines[offset:offset+3]))
    next=sum(lines[offset:offset+3])
    if next > last:
        # print('Greater: {}'.format(lines[offset:offset+3]))
        answer+=1
    last=next

print('Part 2 Answer: {}'.format(answer))
