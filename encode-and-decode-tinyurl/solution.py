class Codec:
    def __init__(self):
        self.encod={}
        self.decod={}
        self.base="pop.com/"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.encod:
            short=self.base+str(len(self.encod)+1)
            self.encod[longUrl]=short
            self.decod[short]=longUrl
        return self.encod[longUrl]
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.decod[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))