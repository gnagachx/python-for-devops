#!/usr/bin/env python

import fire
import os

def walk_path(parent_path):
    print(f"Checking: {parent_path}")
    childs = os.listdir(parent_path) 1

    for child in childs:
        child_path = os.path.join(parent_path, child) 2
        if os.path.isfile(child_path): 3
            last_access = os.path.getatime(child_path) 4
            size = os.path.getsize(child_path) 5
            print(f"File: {child_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")
        elif os.path.isdir(child_path): 6
            walk_path(child_path) 7

if __name__ == '__main__':
    fire.Fire()