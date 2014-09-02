#!/usr/bin/env python

import sys

try:
	import matplotlib.pyplot as plt
	import numpy as np

except ImportError:
	print ("Error importing matplotlib")
	sys.exit(1)

def mplot_heatmap( x, y, z, title=None, xlabel=None, ylabel=None, colorbar=True, figsize=(10,4), cmap=plt.cm.Oranges, \
                  xlabel_fontsize='small', ylabel_fontsize='small', title_fontsize='large'):
    """function mplot_heatmap( args ):
    
    x = list of items to be placed on x-axis
    y = list of items to be placed on y-axis
    z = 2x2 Grid of values to plot
    
    title_fontsize, xlabel_fontsize, ylabel_fontsize:
            'xx-small', 'x-small', 'small', 'large', 'x-large', 'xx-large'
    
    cmap =  ColorMap
            plt.cm.Oranges (default)
            plt.cm.Blues
            plt.cm.Accent
            plt.cm.BrBG
            plt.cm.BuGn
            plt.cm.BuPu
            plt.cm.CMRmap
            plt.cm.Dark2
            plt.cm.GnBu
            plt.cm.Greens
            plt.cm.Greys
            plt.cm.OrRd
            plt.cm.Paired
            plt.cm.PRGn
            plt.cm.Pastel1 | Pastel2
            plt.cm.RdBu
            plt.cm.RdGy
            plt.cm.RdPu
            plt.cm.RdYlBu
            plt.cm.RdYlGn
            plt.cm.Reds
            plt.cm.ScalarMappable
            plt.cm.Set1 | Set2 | Set3
            plt.cm.Spectral
            plt.cm.Wistia
            plt.cm.YlGn
            plt.cm.YlGnBu
            plt.cm.YlOrBr
            plt.cm.YlOrRd
    
    """
    
    heatmap = plt.pcolor( z, cmap=cmap )
    
    
    fig = plt.gcf()
    fig.set_size_inches(figsize[0], figsize[1])
    
    
    plt.ylim([0, len(y)])
    plt.xlim([0, len(x)])
    
    if (title):
        plt.title(title, fontsize=title_fontsize)
    
    if (xlabel):
        plt.xlabel(xlabel, fontsize=xlabel_fontsize)
        
    if (ylabel):
        plt.ylabel(ylabel, fontsize=ylabel_fontsize)
    
    
    ax = plt.gca()
    ax.set_xticks(np.arange(z.shape[1])+0.5, minor=False)
    ax.set_yticks(np.arange(z.shape[0])+0.5, minor=False)
    ax.set_xticklabels(x, minor=False, color='blue', fontsize='small')
    ax.set_yticklabels(y, minor=False, color='blue', multialignment='left', fontsize='small')
    
    
    if (colorbar):
        plt.colorbar(heatmap)
    
    plt.show()




