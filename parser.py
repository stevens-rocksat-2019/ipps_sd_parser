from comm_pb2 import TxMicro, PowerRailInfo
import csv

num_rails = 6

with open("ANALOG11.TXT", "rb") as in_file, open("out.csv", "w") as out_file:
    results = []
    out_file_writer = csv.writer(out_file, delimiter=',',
                                 quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_file_writer.writerow([f"Voltage {i + 1}" for i in range(num_rails)] + [f"Current ${i + 1}" for i in range(num_rails)])

    while True:
        length = in_file.read(2)
        if not length:
            break
        try:
            decoded = TxMicro.FromString(in_file.read(int.from_bytes(length, byteorder='big')))
        except Exception:
            print("bad read")
            continue

        results.append(decoded)
        voltages = [0] * num_rails
        currents = [0] * num_rails
        rail: PowerRailInfo
        for rail in decoded.powerRailInfo:
            voltages[rail.powerRail-1] = rail.voltage
            currents[rail.powerRail-1] = rail.current

        out_file_writer.writerow(voltages + currents)