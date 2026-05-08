import pyshark
import matplotlib.pyplot as plt
from datetime import datetime

def count_packets(file_path):
    cap = pyshark.FileCapture(file_path)
    count = 0
    for packet in cap:
        count += 1
    cap.close()
    return count


def get_packet_times(file_path):
    cap = pyshark.FileCapture(file_path)
    times = []

    for packet in cap:
        if hasattr(packet, 'sniff_time'):
            times.append(packet.sniff_time)

    cap.close()
    return times


def packets_per_second(times):
    counts = {}

    for t in times:
        second = t.replace(microsecond=0)
        counts[second] = counts.get(second, 0) + 1

    return counts


normal_file = '../captures/normal_chat.pcapng'
burst_file = '../captures/burst_chat.pcapng'



normal_count = count_packets(normal_file)
burst_count = count_packets(burst_file)

print("Normal traffic packet count:", normal_count)
print("Burst traffic packet count:", burst_count)


if burst_count > normal_count * 1.5:
    behavior = "Coordinated / Burst Communication"
    risk = "Medium"
else:
    behavior = "Normal Communication"
    risk = "Low"

print("\nBehavior Detected:", behavior)
print("Risk Level:", risk)


normal_times = get_packet_times(normal_file)
burst_times = get_packet_times(burst_file)

normal_pps = packets_per_second(normal_times)
burst_pps = packets_per_second(burst_times)

plt.figure(figsize=(10, 4))
plt.plot(normal_pps.keys(), normal_pps.values(), label='Normal Traffic')
plt.plot(burst_pps.keys(), burst_pps.values(), label='Burst Traffic')

plt.xlabel('Time')
plt.ylabel('Packets per Second')
plt.title('Encrypted Traffic Behavior Analysis')
plt.legend()
plt.tight_layout()

plt.savefig('../screenshots/traffic_analysis.png')
print("Graph saved as screenshots/traffic_analysis.png")
