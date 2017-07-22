import time
def blast(x):
    if x==0:
        print "Blast Off!!!!!!!"
    else:
        time.sleep(1)
        print x
        blast(x-1)
blast(8)
