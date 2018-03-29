#!/usr/bin/env python3

import cv2


def main():
    img = cv2.imread('pics/3.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('readin', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass


if __name__ == '__main__':
    main()
