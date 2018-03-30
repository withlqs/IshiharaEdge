#!/usr/bin/env python3

import cv2
import numpy as np

from kmeans import *


def contrast(img, a):
    base = np.mean(img)
    b = base * (1 - a)
    return np.uint8(np.clip((a * img + b), 0, 255))


def show(img):
    height, width = img.shape[:2]
    cv2.namedWindow('readin', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('readin', max(min(600, height), 100), max(min(600, width), 100))
    cv2.imshow('readin', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize(img, factor):
    height, width = img.shape[:2]
    return cv2.resize(img, (int(height * factor), int(width * factor)))


def main():
    img = cv2.imread('pics/2a.png')
    # img = cv2.GaussianBlur(img, (41, 41), 10)
    #
    # img = resize(img, 0.1)
    show(img)
    # img = resize(img, 10)
    # img = cv2.GaussianBlur(img, (21, 21), 10)
    #
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # img[:, :, 1] = np.clip(img[:, :, 1]*1.75, 0, 255)
    # img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    # img = contrast(img, 1.75)
    #
    # img[0][0][0] = img[0][0][1] = img[0][0][2] = 0

    sets = [set(), set(), set()]
    inputs = set()
    max_sum = 0
    min_sum = 255 * 3
    for x in img:
        for y in x:
            max_sum = max(max_sum, y[0] + y[1] + y[2])
            min_sum = min(min_sum, y[0] + y[1] + y[2])

    for x in img:
        for y in x:
            # inputs.add(tuple(y))
            sum_v = sum(y)
            if max_sum == sum_v:
                sets[2].add(tuple(y))
            elif min_sum == sum_v:
                sets[0].add(tuple(y))
            else:
                sets[1].add(tuple(y))

    sets = kmeans_sets(sets, inputs)

    for x in img:
        for y in x:
            if tuple(y) in sets[0]:
                y[0] = 0
                y[1] = 0
                y[2] = 0
            elif tuple(y) in sets[1]:
                y[0] = int(255 / 2)
                y[1] = int(255 / 2)
                y[2] = int(255 / 2)
            else:
                y[0] = int(255)
                y[1] = int(255)
                y[2] = int(255)

    show(img)

    # pyplot.axis('off')
    # pyplot.imshow(img)
    # pyplot.show()
    pass


if __name__ == '__main__':
    main()
