from datetime import datetime
from block import block

class blockChain:

    def __init__(self):
        self.rootBlock = block( 0, 'root block', 0)
        self.chain = [self.rootBlock]

    def addBlock(self, data):
        index = len( self.chain ) - 1
        timeCreated = datetime.now()
        newBlock = block( index, data, self.getLastHash() )
        self.chain.append(newBlock)

    def getLastHash(self):
        return self.chain[-1].hash

    def printChain(self):
        for block in self.chain:
            print('Data = ' + str(block.data) )
            print('Hash = ' + str(block.hash) )
            print('Previous hash = ' + str(block.previous) )
            print('')
