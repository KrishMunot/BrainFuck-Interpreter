#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# simulate the tape with a list
tape = [0]*(3*10**4)

# the data pointer
ptr   = 0

# the simple brainfuck commands

def lt():
    """ performs a < """
    global ptr
    if ptr <= 0:
        raise ValueError, "Segmentation fault!"
    ptr -= 1

def rt():
    """" performs a > """
    global ptr
    if ptr >= 3*10**4 - 1:
        raise ValueError, "Segmentation fault!"
    ptr += 1

def plus():
    """ performs a + """
    global ptr
    tape[ptr] = (tape[ptr] + 1) % 256

def minus():
    """ perfoms a - """
    global ptr
    tape[ptr] = (tape[ptr] - 1) % 256

def dot():
    """ performs a . """
    global ptr
    sys.stdout.write(chr(tape[ptr]))

def comma():
    """ performs a , """
    global ptr
    c = ord(sys.stdin.read(1))
    if c != -1:
        tape[ptr] = c
        
