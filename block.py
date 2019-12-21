from datetime import datetime
class block:

    def __init__(self, index, data, previous):
        self.index = index
        self.data = data
        self.timeCreated = datetime.now()
        self.previous = previous
        self.nonce = 0
        self.hash = self.mine()

    def getHash(self):
        objectHash = str(self.index) + str(self.data) + str(self.timeCreated) + str(self.previous) + str(self.nonce)
        return hash(objectHash)

    def mine(self):

        #Proof of work
        objectHash = ''
        while( '33' not in objectHash[0:2]):
            print('Calculating hash... ' + str(self.nonce))
            objectHash = str( self.getHash() )
            print(objectHash)
            self.nonce = self.nonce + 1

        return objectHash
