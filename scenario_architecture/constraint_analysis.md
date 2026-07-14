Task A1 – Constraint Analysis
Constraint Analysis for the FreightBridge Cold-Chain Edge AI Deployment
The LogiEdge system is designed to monitor refrigerated trucks that transport medicines in real time, utilizing Edge Artificial Intelligence. Rather than depending solely on the cloud, this AI operates directly on the truck, ensuring continuous monitoring even when internet connectivity is unreliable. To evaluate the effectiveness of this approach, four key aspects of Edge AI must be considered: its response speed, data usage, connectivity reliability, and the security of the information it handles.
1. Latency Constraint
FreightBridge's refrigerated trucks are used to transport temperature-sensitive medicines and vaccines, and any failure in the refrigeration system can quickly lead to a loss in product quality.
According to the project's specifications, a refrigeration unit failure can cause the cargo temperature to rise by about 1°C per minute, and the system must identify and generate an alert within 90 seconds of the first sign of a fault in the sensor data.
A cloud-based system requires sensor data to be sent from the truck to a remote cloud server for processing before the results are sent back to the truck or the operations centre.
In rural areas of Maharashtra and Andhra Pradesh, cellular networks often face issues like high latency, network congestion, and intermittent connectivity.While a stable 4G network usually has a round-trip latency of between 100 and 300 milliseconds, in rural areas these delays can increase to several seconds or even lead to complete communication failure.Therefore, a purely cloud-based solution cannot ensure the required 90-second detection window, especially during network interruptions.
In contrast, Edge AI performs the inference directly on the onboard computing device, reducing the inference latency to just a few milliseconds.
This allows for the immediate detection of refrigeration system problems and ensures that timely alerts can be sent to both the driver and the operations centre whenever a connection is available.
2. Bandwidth Constraint
Each refrigerated truck continuously generates sensor data from three sources:
Temperature sensor: 1 reading/second
Vibration sensor: 500 readings/second (3-axis)
Door sensor: Event-driven (open/close)
Assuming each sensor value occupies 4 bytes, the daily data generation can be estimated as follows:
Temperature data:
86,400 readings/day × 4 bytes = 345,600 bytes ≈ 0.33 MB/day
Vibration data:
500 × 3 = 1,500 values/second
1,500 × 86,400 = 129,600,000 values/day
129,600,000 × 4 bytes = 518,400,000 bytes ≈ 494 MB/day
Door event data is negligible compared to vibration data.
Therefore, the total raw data generated per truck is approximately:
494 MB + 0.33 MB ≈ 494.33 MB/day
At a transmission cost of ₹0.10 per MB, the communication cost becomes:
494.33 × ₹0.10 ≈ ₹49.43 per truck per day
For 85 refrigerated trucks, the daily transmission cost would be approximately:
85 × ₹49.43 ≈ ₹4,202 per day
An Edge AI solution avoids continuous transmission of raw sensor streams. Instead, only anomaly alerts, periodic summaries, and system health reports are transmitted, typically amounting to only a few kilobytes per day. This significantly reduces bandwidth consumption and communication costs while improving scalability.
3. Connectivity Constraint
FreightBridge has identified seven points along the Nashik–Aurangabad route where cellular connectivity is unavailable for between 35 to 90 minutes.
During these periods of network outage, a cloud-only system would not be able to receive sensor data, carry out analysis, or produce timely alerts. Any refrigeration failures that occur during these times would go unnoticed until the network connection is restored, thereby increasing the risk of damaged cargo and failure to meet regulatory standards.
The proposed Edge AI architecture addresses this issue by conducting all analysis locally on the truck.
Sensor data is continuously processed in real time, even when there is no network connection. Drivers receive immediate alerts, and operational events are safely stored in the device's local memory. When connectivity is restored, the stored data and alerts are automatically synced with the central operations platform. This store-and-forward approach ensures continuous monitoring throughout the entire transportation process.
4. Privacy Constraint
FreightBridge's pharmaceutical clients need to be assured that temperature records and cargo condition data are kept secure and not accessible to unauthorized individuals.
In a cloud-only setup, the constant sending of raw operational data through public cellular networks raises the risk of interception, unauthorized access, and possible data breaches.
By conducting inference locally, the Edge AI system reduces the amount of sensitive information being sent outside the vehicle.
Only necessary outputs, such as classification results, alerts, and encrypted summary reports, are shared with the cloud. This greatly lowers the potential for security threats while maintaining the confidentiality of operational data. As a result, on-device inference supports compliance with security agreements and boosts customer confidence in the reliability of the pharmaceutical cold chain.
Conclusion
Given the strict latency demands, large volume of sensor data, inconsistent connectivity in rural areas, and strong privacy regulations, a cloud-only setup is not suitable for FreightBridge's cold-chain monitoring system.
An Edge AI-based approach enables real-time decision-making, lowers communication expenses, ensures continuous operations during network disruptions, and improves data security. As a result, Edge AI is the most suitable architecture for the LogiEdge pilot and offers a scalable foundation for future implementation across the entire company fleet.
