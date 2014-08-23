import re, os, sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def read_ui_performance_fps():
    fname = "uispeed.log"

    x = []
    results = []
    f = open(fname, 'r')
    for line in f:
        #[Tue Feb 28 17:35:24.500 2012] I/UITEST  ( 1147): 60.728745 fps 
        m = re.match(r'.*: *([0-9.]+) fps', line)
        if m:
            fps = float(m.group(1))
            results.append(fps)
    f.close() 
            
    if len(results)>5:
        fps = 0
        for r in results:
            fps += r
        fps /= len(results)
        print 'average:', fps
    else:
        print "found", len(results),"results, waiting for 5"


    plt.subplot(211)
    plt.title(r'$\mathrm{FPS(run)\  and\  Histogram\ of\ FPS}$')
    x = np.arange(0, len(results), 1);
    plt.plot(x, results, 'b*')
    plt.xlim(0,len(results))
    plt.xlabel('run #')
    plt.ylabel('uiSpeed2 FPS')
    plt.grid(True)

    plt.subplot(212)
    n, bins, patches = plt.hist(results, 10, normed=0,facecolor='green', alpha=0.75)
    plt.xlabel('FPS')
    plt.ylabel('#')
    plt.grid(True)

    plt.savefig("test.png", dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None,  transparent=False, bbox_inches=None, pad_inches=0.1)

    #plt.show()
    return fps       

read_ui_performance_fps()
