from blockChain import blockChain
from block import block

class main:

    chain = blockChain()
    chain.addBlock('second block')
    chain.addBlock('Third block')

    chain.printChain()

