try:
    import simplejson as json
except:
    import json
import requests

class FuckOff():
    """instantiate with senders name"""
    def __init__(self,sender):
        self.sender = sender
        self.headers = {'Accept':'application/json'}
        self.host_url = 'http://foaas.herokuapp.com/'

    def fo_from(self,uri,sender):
        url = self.host_url + uri + '%s' % sender
        fuckoff = requests.get(url,headers=self.headers)
        return fuckoff

    def fo_to_from(self,uri,receiver,sender):
        url = self.host_url + uri + '%s/%s' % (receiver,sender)
        fuckoff = requests.get(url,headers=self.headers)
        return fuckoff

    def off(self,recip):
        uri = 'off/'
        fuckoff = self.fo_to_from(uri,recip,self.sender)
        return fuckoff.text

    def you(self,recip):
        uri = 'off/'
        fuckoff = self.fo_to_from(uri,recip,self.sender)
        return fuckoff.text

    def donut(self,recip):
        uri = 'donut/'
        fuckoff = self.fo_to_from(uri,recip,self.sender)
        return fuckoff.text

    def shakespeare(self,recip):
        uri = 'shakespeare/'
        fuckoff = self.fo_to_from(uri,recip,self.sender)
        return fuckoff.text

    def linus(self,recip):
        uri = 'linux/'
        fuckoff = self.fo_to_from(uri,recip,self.sender)
        return fuckoff.text

    def king(self,recip):
        uri = 'king/'
        fuckoff = self.fo_to_from(uri,recip,self.sender)
        return fuckoff.text

    def chainsaw(self,recip):
        uri = 'chainsaw/'
        fuckoff = self.fo_to_from(uri,recip,self.sender)
        return fuckoff.text

    def fthis(self):
        uri = 'this/'
        fuckoff = self.fo_from(uri,self.sender)
        return fuckoff.text

    def fthat(self):
        uri = 'that/'
        fuckoff = self.fo_from(uri,self.sender)
        return fuckoff.text

    def everything(self):
        uri = 'everything/'
        fuckoff = self.fo_from(uri,self.sender)
        return fuckoff.text

    def everyone(self):
        uri = 'everyone/'
        fuckoff = self.fo_from(uri,self.sender)
        return fuckoff.text

    def pink(self):
        uri = 'pink/'
        fuckoff = self.fo_from(uri,self.sender)
        return fuckoff.text

    def life(self):
        uri = 'life/'
        fuckoff = self.fo_from(uri,self.sender)
        return fuckoff.text

    def thanks(self):
        uri = 'thanks/'
        fuckoff = self.fo_from(uri,self.sender)
        return fuckoff.text

    def flying(self):
        uri = 'that/'
        fuckoff = self.fo_from(uri,self.sender)
        return fuckoff.text

    def fascinating(self):
        uri = 'fascinating/'
        fuckoff = self.fo_from(uri,self.sender)
        return fuckoff.text

    def thing(self,thing):
        uri = '%s/' % thing
        url = self.host_url + uri + '%s' % self.sender
        fuckoff = requests.get(url,headers=self.headers)
        return fuckoff.text
