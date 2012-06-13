#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2011
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a reader
    a is an array on int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# -----------
# collatz_cycle_length
# -----------

# -----------
# collatz_cycle_length
# -----------

def collatz_cycle_length(i) :
    cycleLen = 1
    x = i
    while x > 1:
        if x%2 == 0:
            x = x/2
            cycleLen = cycleLen + 1
        else:
            x = x*3
            x = x + 1
            cycleLen = cycleLen +1
    return cycleLen


# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    # <start my code>
    temp = -1
    maxCycleLen = -1
    y = i
    if j > i:
        while (y <=j) :
            temp = collatz_cycle_length(y)
            if temp > maxCycleLen :
                maxCycleLen = temp
            y = y + 1
    else:
        while y <= i :
            temp = collatz_cycle_length(y)
            if temp > maxCycleLen :
                maxCycleLen = temp
            y = y + 1
    # <end my code>
    v = maxCycleLen
    assert v > 0
    return v

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)


