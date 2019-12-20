from datetime import datetime
class block:

    def __init__(self, index, data, previous):
        self.index = index
        self.data = data
        self.timeCreated = datetime.now()
        self.previous = previous
        self.hash = self.getHash()
        self.nonce = 0

    def getHash(self):
        #Proof of work
        objectHash = ''
        while(objectHash[0:1] is not '0000'):
            print('Calculating hash...')
            print(objectHash)
            objectHash = str(self.index) + str(self.data) + str(self.timeCreated)+ str(self.previous)
            hash(objectHash)
            self.nonce = self.nonce + 1
        return objectHash
