'''
Created on Oct 19, 2011

@author: mmasche
'''
from WMCore.Storage.TrivialFileCatalog import readTFC
from WMCore.Services.PhEDEx.PhEDEx import PhEDEx

class LFN2PFNConverter:
    '''
    The class handles the TFC cache of each site, and allow to perform the lfn2pfn
    conversion without connecting to phedex every time
    '''

    def __init__(self, dict=None):
        '''
        Constructor: create
        '''
        self.phedex = PhEDEx(responseType='xml', dict=dict)

    def lfn2pfn(self, siteName, lfn):
        #Default: cache expires in 0.5 hours in Service
        self.phedex.getNodeTFC(siteName)

        tfcCacheFile = self.phedex.cacheFileName('tfc', inputdata={'node': siteName})
        tfc = readTFC(tfcCacheFile)
        return tfc.matchLFN('srmv2', lfn)
