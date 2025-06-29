 HEAD
from address import Address


764018d5ea3a7bf55226cb438fe317a0dae1dbe9
class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track