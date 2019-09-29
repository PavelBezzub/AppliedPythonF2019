#!/usr/bin/env python
# coding: utf-8

import sys
from type_is import json_or_csv
from parse import read_data, print_data
from file import open_file
from encode import find_encode


if __name__ == '__main__':
    filename = sys.argv[1]
    try:
        open_file(filename)
        type_f = find_encode(filename)
        encoding = json_or_csv(filename, type_f)
        print_data(read_data(filename, type_f, encoding))
    except FileNotFoundError:
        print("Файл не валиден")
    except UnicodeDecodeError:
        print("Формат не валиден")
    except:
        print("Формат не валиден")
