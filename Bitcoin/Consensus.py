import random
from Configuration import GeneralConfiguration

class Consensus:
    nonce = random.randrange(0, GeneralConfiguration.thirty_two_bit_upper_range)
    pass