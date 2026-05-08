🔐 CipherScope — Encrypted Communication Behavior Analysis

📌 Overview

CipherScope is a cyber forensics prototype designed to analyze encrypted communication behavior without accessing or decrypting message content. The project focuses on extracting meaningful forensic insights from network traffic metadata such as packet timing, frequency, and burst intensity.
Instead of breaking encryption, CipherScope analyzes behavioral patterns in encrypted traffic to identify anomalous or coordinated communication activity in a privacy-preserving manner.

🚀 Features

>📡 Captures encrypted network traffic using Wireshark
>🔍 Extracts packet metadata from PCAP/PCAPNG files
>📊 Performs packet frequency and burst analysis
>⚠️ Detects coordinated or high-intensity communication patterns
>📈 Generates time-based traffic visualizations
>🔒 Privacy-safe analysis without message decryption

🧠 Core Idea
Modern communication platforms use strong encryption, making direct content inspection difficult for investigators and security teams. CipherScope addresses this challenge by focusing on behavioral analysis instead of content analysis.
The system studies:
Packet timing
Packet frequency
Burst communication intensity
Time-based traffic behavior
to derive forensic insights while respecting privacy and encryption boundaries.

⚙️ Tech Stack
Python
Wireshark
PyShark
Matplotlib

🏗️ Project Workflow
>Capture encrypted traffic using Wireshark
>Store traffic as .pcapng files
>Extract packet metadata using PyShark
>Analyze packet frequency and timing behavior
>>Classify traffic using rule-based logic
>Visualize packet-rate patterns over time

📊 Detection Logic
CipherScope uses a rule-based behavioral analysis algorithm.
Detection Parameters
Total packet count
Packets per second
Burst communication spikes
Relative traffic intensity
If burst traffic significantly exceeds normal traffic thresholds, the communication is flagged as coordinated or anomalous.

📈 Visualization
The project generates packet-rate visualizations comparing:
Normal communication behavior
Burst / coordinated communication behavior
These visualizations help investigators interpret encrypted traffic patterns more effectively.

🔒 Ethical Considerations
CipherScope does not:
decrypt messages
inspect message content
infer intent or guilt
The system is designed as an assistive forensic tool that flags anomalous patterns for human investigation.

💡 Use Cases
Cyber forensics investigations
Security Operations Center (SOC) traffic analysis
Encrypted traffic behavioral monitoring
Educational cybersecurity demonstrations
Research on privacy-preserving forensic systems

▶️ How to Run
1️⃣ Install dependencies
pip3 install pyshark matplotlib
2️⃣ Place capture files
Store your capture files inside:
captures/
Example:
captures/normal_chat.pcapng
captures/burst_chat.pcapng
3️⃣ Run the analysis
cd code
python3 analyze.py

📷 Output
Packet count analysis
Behavior classification
Risk level detection
Time-based traffic visualization graph

📌 Future Improvements
Real-time traffic monitoring
Advanced anomaly scoring
Machine learning-assisted classification
Interactive dashboard visualization
Multi-session traffic correlation

👥 Team
Developed as part of NOOB HACKFEST, a 24-hour national multidisciplinary hackathon hosted at SRM Institute of Science and Technology, Tiruchirappalli.

🔖 License
This project is intended for educational and research purposes only.
