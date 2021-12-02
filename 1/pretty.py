#!/usr/bin/env python3
import sys

def part1(input):
    answer=sum(1 for _ in filter(lambda x: x[1] > x[0], zip(input, input[1:])))

    print('Part 1 Answer: {}'.format(answer))

def part2(input):
    #with trick
    answer=sum(1 for _ in filter(lambda x: x[1] > x[0], zip(input, input[3:])))

    print('Part 2 Answer: {}'.format(answer))

def part2hard(input):
    #without trick
    triples=list(zip(input, input[1:], input[2:]))
    answer=sum(1 for _ in filter(lambda x: sum(x[1]) > sum(x[0]), zip(triples, triples[1:])))

    print('Part 2 Answer: {}'.format(answer))

def main():
    with open(sys.argv[1], 'r') as ifp:
        vals = [int(x.strip()) for x in ifp.readlines()]
    part1(vals)
    part2(vals)

if __name__ == "__main__":
    main()
