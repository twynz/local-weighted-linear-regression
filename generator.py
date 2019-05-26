#! /usr/bin/python2.7

import random


def genrate():
    file_name = '/Users/tangw/Desktop/homework/mlp/testtrain.txt'
    f = open(file_name, 'a+')  # open file in append mode
    for i in range(30):
        newLine = trainset()
        f.write(newLine)
    f.close()


def trainset():
    f1 = round(random.uniform(8, 14), 1)
    f2 = round(random.uniform(18, 40), 0)
    f3 = round(random.uniform(0, 1), 0)
    f4 = round(random.uniform(0, 12), 0)
    f5 = round(random.uniform(0, 36), 0)
    f6 = round(random.uniform(0, 10), 0)
    f7 = round(random.uniform(6, 11), 0)
    f8 = round(random.uniform(0.5, 2.5), 0)
    f9= round(random.uniform(0, 10), 0)
    newLine = (str(1.0) + '\t' + str(f1) + '\t' + str(f2) + '\t' + str(f3) + '\t' + str(f4) + '\t' + str(
        f5) + '\t' + str(f6) + '\t' + str(f7) + '\t' + str(f8) + '\t' + str(f9) +'\n')
    return newLine


def main():
    genrate()


if __name__ == '__main__':
    main()
