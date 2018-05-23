#!/usr/bin/env python

import os, sys, time

def test(): 
    status="on" 
    print ("Auto restart mode")
    executable = sys.executable
    args = sys.argv[:]
    args.insert(0, sys.executable)

    time.sleep(30)
    print ("check")
    if status =="on":
        print ("yes")
    else:
       print("no")
    os.execvp(executable, args)

if __name__ == "__main__":  
    test()