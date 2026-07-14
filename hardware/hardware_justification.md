Task B1 – Constraint Triangle Application
Hardware Selection Based on the Edge AI Constraint Triangle:
The LogiEdge system necessitates an edge computing platform that can execute real-time machine learning inference within FreightBridge's refrigerated trucks. The chosen hardware must fulfill three main constraints: performance, power usage, and cost, which are collectively referred to as the Edge AI Constraint Triangle. Additionally, the hardware must meet specific operational demands, including the ability to detect refrigeration issues within 90 seconds, operate within a maximum AI power consumption of 10 watts, and remain cost-effective for deployment across 85 pilot vehicles, with potential for future expansion to 265 trucks.
Option 1 – Raspberry Pi 5 (8 GB) with AI HAT (Hailo-8L, 13 TOPS)
The Raspberry Pi 5, when paired with the Hailo-8L AI accelerator, delivers a processing power of 13 TOPS, which is more than adequate for running lightweight classification models commonly used in cold-chain monitoring applications.
The overall power consumption of the system is approximately 7.5 watts, which well within the project's 10 watt power budget, allowing for continuous operation using the truck's 12-volt battery via a DC-DC converter.
The estimated cost of deployment for each truck is around ₹15,000, leading to the following total costs:
•	85 trucks (Pilot): ₹12.75 lakh
•	265 trucks (Full deployment): ₹39.75 lakh
This configuration provides a well-balanced solution in terms of computational power, energy efficiency, and cost.
The platform supports several essential technologies and tools, including Linux, Docker, MQTT brokers, TensorFlow Lite, ONNX Runtime, and Hailo acceleration, which simplifies the development and maintenance of future software.
Constraint Triangle Position: The solution is balanced in terms of performance, power consumption, and cost.
2.Option 2 – NVIDIA Jetson Orin Nano Super (67 TOPS)
The Jetson Orin Nano Super offers much greater computational power (67 TOPS) than needed for this application.
While it is capable of running complex deep learning models, the cold-chain monitoring system only performs sensor-based three-class classification.As a result, most of its processing power remains underutilized.
The platform uses around 15 W of power under moderate AI workloads, which is higher than the project's specified 10 W power limit.
Additionally, its cost of approximately ₹45,000 per truck makes large-scale deployment expensive:
•	85 trucks (Pilot): ₹38.25 lakh
•	265 trucks (Full deployment): ₹1.19 crore
Although it meets the latency requirements effectively, its higher power consumption and deployment costs make it less suitable for large-scale implementation.
Constraint Triangle Position: Strongly optimized for performance, but weak in terms of cost and power.
3.Option 3 – STM32H7 Custom MCU
The STM32H7 microcontroller provides outstanding energy efficiency, consuming only 0.4 watts of power and having a low hardware cost of approximately ₹3,500 per truck.
The deployment costs are as follows:
•	For 85 trucks (Pilot): ₹2.98 lakh
•	For 265 trucks (Full deployment): ₹9.28 lakh
However, the STM32H7 does not have dedicated AI acceleration and has limited memory and processing power.
While it is suitable for rule-based monitoring or TinyML tasks, it is not capable of running more complex machine learning models, supporting MLOps features, local MQTT services, secure storage, or enabling future software updates.This limits its scalability and adaptability, despite its strong performance in terms of power efficiency.
Constraint Triangle Position: Optimised for Cost and Power but constrained by Performance.
Recommended Hardware
The Raspberry Pi 5 (8 GB) paired with the Hailo-8L AI HAT is the most suitable hardware option for deploying the LogiEdge system.
This setup delivers adequate AI performance to meet real-time latency demands while staying within the 10 W power limit.Additionally, its reasonable cost allows for cost-effective large-scale implementation across both the 85-truck pilot program and the planned expansion to 265 vehicles.
In contrast, the Jetson Orin Nano Super offers much higher computational power than needed, but it surpasses the allowed power budget and leads to higher deployment expenses.
On the other hand, the STM32H7 microcontroller excels in energy efficiency and cost, but it lacks the necessary processing power and software support for reliable Edge AI inference, secure local processing, MQTT services, and future model updates.
Taking into account the combined needs for real-time inference, energy efficiency, cost-effectiveness, and future scalability, the Raspberry Pi 5 with the Hailo-8L AI accelerator is the best choice for the LogiEdge Edge AI system.
