#!/usr/bin/env python

import os, sys, time

def test():  
    print ("AutoRes is starting")
    executable = sys.executable
    args = sys.argv[:]
    args.insert(0, sys.executable)

    time.sleep(30)
    print ("Respawning")
    num1 = 1.5
    num2 = 6.3
    sum = float(num1) + float(num2)
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
    os.execvp(executable, args)

if __name__ == "__main__":  
    test()