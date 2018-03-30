#!/usr/bin/env python3
import random


def kmeans_sets(sets, input):
    for e in list(input):
        final_distance = 256 ** 2 * 3
        final_set = sets[0]
        for now_s in sets:
            distance = 0
            for element in now_s:
                distance += (e[0] - element[0]) ** 2 + (e[1] - element[1]) ** 2 + (e[2] - element[2]) ** 2
            distance /= len(now_s)
            if distance < final_distance:
                final_distance = distance
                final_set = now_s
        input.discard(e)
        final_set.add(e)

    changed = True
    loop = 10
    i = 0
    while changed and i < loop:
        i += 1
        print('---')
        for s in sets:
            for e in list(s):
                final_distance = 256 ** 2 * 3
                final_set = sets[0]
                for now_s in sets:
                    distance = 0
                    for element in now_s:
                        distance += (e[0] - element[0]) ** 2 + (e[1] - element[1]) ** 2 + (e[2] - element[2]) ** 2
                    distance /= len(now_s)
                    if distance < final_distance:
                        final_distance = distance
                        final_set = now_s
                if final_set != s:
                    changed = True
                    s.discard(e)
                    final_set.add(e)

    return sets


def kmeans(input, sets_number):
    sets = []
    for i in range(sets_number):
        sets.append(set())
        element = random.choice(list(input))
        input.discard(element)
        sets[i].add(element)

    for e in list(input):
        final_distance = 256 ** 2 * 3
        final_set = sets[0]
        for now_s in sets:
            distance = 0
            for element in now_s:
                distance += (e[0] - element[0]) ** 2 + (e[1] - element[1]) ** 2 + (e[2] - element[2]) ** 2
            distance /= len(now_s)
            if distance < final_distance:
                final_distance = distance
                final_set = now_s
        input.discard(e)
        final_set.add(e)

    changed = True
    loop = 10
    i = 0
    while changed and i < loop:
        i += 1
        print('---')
        for s in sets:
            for e in list(s):
                final_distance = 256 ** 2 * 3
                final_set = sets[0]
                for now_s in sets:
                    distance = 0
                    for element in now_s:
                        distance += (e[0] - element[0]) ** 2 + (e[1] - element[1]) ** 2 + (e[2] - element[2]) ** 2
                    distance /= len(now_s)
                    if distance < final_distance:
                        final_distance = distance
                        final_set = now_s
                if final_set != s:
                    changed = True
                    s.discard(e)
                    final_set.add(e)

    return sets


def main():
    input = {
        (0, 1, 1),
        (0, 2, 1),
        (0, 1, 2),
        (0, 4, 5),
        (0, 4, 4),
        (0, 5, 4)
    }
    sets = kmeans(input, 2)
    for s in sets:
        for e in s:
            print(e)
        print('======')

    pass


if __name__ == '__main__':
    main()
