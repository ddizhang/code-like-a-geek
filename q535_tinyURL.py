class Codec:
    
    def __init__(self):
        self.code = {}
        self.code_len = 6
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) 
                         for _ in range(self.code_len))
        
        # if random_string is already used: generate a new one!
        while random_string in self.code:
                    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) 
                                            for _ in range(self.code_len))
        
        shortened_url = 'http://tinyurl.com/'+random_string
        self.code[random_string] = longUrl
        #print(random_string)
        #print(self.code[random_string])
        return shortened_url
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        shortened_url_code = shortUrl[-(self.code_len) : ]
        #print(shortened_url_code)
        return self.code[shortened_url_code]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))