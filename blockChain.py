
import hashlib

class Sak36CoinBlock:

    def __init__(self, previousBlockHash, transectionList):
        self.previousBlockHash = previousBlockHash
        self.transectionList = transectionList

        self.blockData = "-".join(transectionList) + "-" + previousBlockHash        
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()


transection1 = "someone sends me 10000 SC"
transection2 = "sometwo sends me 5000 SC"
transection3 = "somethree sends me 500 SC"
transection4 = "somefour sends me 50 SC"
transection5 = "somefive sends me 5 SC"

initialBlock = Sak36CoinBlock("Initial String", [transection1, transection2])

print(initialBlock.blockData)
print(initialBlock.blockHash)