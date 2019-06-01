from comm_pb2 import TxMicro,PowerRailInfo
import random

with open("test.txt", "wb") as f:
    for j in range(1000):

        tx = TxMicro()

        for i in range(7):
            rail = tx.powerRailInfo.add()
            rail.current = random.random() + i
            rail.voltage = random.random() + i
            rail.powerRail = i

        serialized = tx.SerializeToString()
        serialized_w_length = (len(serialized)).to_bytes(2, byteorder="big", signed=False) + serialized
        f.write(serialized_w_length)
