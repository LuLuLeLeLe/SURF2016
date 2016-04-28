from poloniex import Poloniex
#import numpy as np
import pandas as pd

#初始化变量
class CoinList(object):

    def __init__(self):
        self.polo = Poloniex()
        vol = self.polo.marketVolume()
        pairs = []
        coins = []
        volumes = []#代表数量
        
#vol的属性优k和v，v的属性有c和val
        for k, v in vol.iteritems():
            if k.startswith("BTC_") or k.endswith("_BTC"):#排除一些不是BTC的东西？不懂
        	pairs.append(k)
                for c, val in v.iteritems():#c和val都是v的一种属性，c是种类，val是数量多少
                    if c != 'BTC':
    		        coins.append(c) #coins只储存除了BTC以外的货币
	            else:
		        volumes.append(float(val))#只记载总共的volumes

        self._df = pd.DataFrame({'coin': coins, 'pair': pairs, 'volume': volumes})#这是一个数据结构他返回一个变量
	self._df = self._df.set_index('coin')

    def allActiveCoins(self):
        return self._df

    def allCoins(self):
	return self.polo.marketStatus().keys()	
#是一个简单的优化过程，每次都选取最优的
    def topNVolume(self, n = 5, order = False, minVolume = 0):
	if minVolume == 0:
	    r = self._df.sort_values(by='volume', ascending=False)[:n]
            if order:
		return r
            else:
		return r.sort_index()
	else:
	    return self._df[self._df.volume >= minVolume]

    #def volumeAtLeast(self, minvolume = 100):
	#return self._df[self._df.volume >= minvolume]
