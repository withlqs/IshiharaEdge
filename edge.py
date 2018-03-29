#!/usr/bin/env python3

import cv2


def main():
    img = cv2.imread('pics/3.jpg', cv2.IMREAD_COLOR)
    # resize
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(img)
    cv2.namedWindow('readin', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('readin', 600, 600)
    cv2.imshow('readin', hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass


if __name__ == '__main__':
    main()
