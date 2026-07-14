# Hardware Justification

## Overview

This document presents the hardware evaluation for the LogiEdge Edge AI deployment at FreightBridge Logistics Pvt. Ltd. The analysis includes the application of the Edge AI Constraint Triangle for hardware selection and the Roofline Model for performance analysis of the chosen platform.

---

# Task B1 – Constraint Triangle Application

## Hardware Selection Based on the Edge AI Constraint Triangle

The LogiEdge system requires an edge computing platform capable of executing real-time machine learning inference inside FreightBridge's refrigerated trucks. The selected hardware must satisfy three major constraints:

- **Performance** – Detect refrigeration failures within **90 seconds**.
- **Power Consumption** – Operate within a maximum AI power budget of **10 W**.
- **Cost** – Remain economically feasible for deployment across **85 pilot trucks**, with future expansion to **265 vehicles**.

These three requirements form the **Edge AI Constraint Triangle**, where performance, power efficiency, and cost must be balanced.

---

## Option 1 – Raspberry Pi 5 (8 GB) + AI HAT+ (Hailo-8L, 13 TOPS)

The Raspberry Pi 5 combined with the Hailo-8L AI accelerator provides **13 TOPS** of AI processing capability, which is more than sufficient for executing the lightweight machine learning models used for cold-chain monitoring.

The complete system consumes approximately **7.5 W**, comfortably satisfying the project's **10 W power budget**. It can therefore operate continuously using the truck's 12 V battery through a DC–DC converter.

### Deployment Cost

- **85 trucks (Pilot):** ₹12.75 lakh
- **265 trucks (Full Deployment):** ₹39.75 lakh

Apart from adequate computing performance, the Raspberry Pi ecosystem supports:

- Linux
- Docker
- Mosquitto MQTT
- TensorFlow Lite
- ONNX Runtime
- Hailo AI acceleration

These features simplify future software deployment, maintenance, and scalability.

**Constraint Triangle Position:** Balanced across Performance, Power, and Cost.

---

## Option 2 – NVIDIA Jetson Orin Nano Super (67 TOPS)

The NVIDIA Jetson Orin Nano Super delivers **67 TOPS**, significantly exceeding the computational requirements of this application.

Since LogiEdge only performs sensor-based three-class classification, much of this processing capability remains unused.

The platform consumes approximately **15 W**, exceeding the project's maximum allowable AI power budget of **10 W**.

### Deployment Cost

- **85 trucks (Pilot):** ₹38.25 lakh
- **265 trucks (Full Deployment):** ₹1.19 crore

Although the Jetson platform easily satisfies the latency requirement, its higher power consumption and significantly greater deployment cost reduce its suitability for fleet-wide deployment.

**Constraint Triangle Position:** Optimised for Performance but weak in Cost and Power.

---

## Option 3 – STM32H7 Custom MCU

The STM32H7 microcontroller provides exceptional energy efficiency with a power consumption of only **0.4 W** and a hardware cost of approximately **₹3,500 per truck**.

### Deployment Cost

- **85 trucks (Pilot):** ₹2.98 lakh
- **265 trucks (Full Deployment):** ₹9.28 lakh

Despite its excellent cost and power characteristics, the STM32H7 lacks dedicated AI acceleration and offers limited memory and computational capability.

While it is suitable for TinyML or rule-based monitoring applications, it cannot efficiently support:

- Advanced machine learning inference
- Local MQTT services
- Secure edge processing
- Docker containers
- Edge MLOps
- Future software scalability

**Constraint Triangle Position:** Optimised for Cost and Power but constrained by Performance.

---

## Recommended Hardware

Among the three evaluated platforms, the **Raspberry Pi 5 (8 GB) with the Hailo-8L AI HAT+** is the most appropriate hardware solution for the LogiEdge deployment.

The platform provides sufficient AI performance to satisfy the **90-second fault detection requirement** while remaining within the **10 W power budget**. Its moderate acquisition cost also enables economical deployment across both the **85-truck pilot fleet** and the planned expansion to **265 trucks**.

In comparison, the **Jetson Orin Nano Super** offers substantially more computational capability than required but exceeds the power budget and significantly increases deployment costs.

The **STM32H7 MCU**, while inexpensive and highly energy efficient, lacks the processing capability and software ecosystem required for reliable Edge AI inference, secure local processing, MQTT communication, and future model scalability.

Considering **performance, power consumption, cost, and scalability**, the **Raspberry Pi 5 with the Hailo-8L AI accelerator** is the recommended hardware platform for the LogiEdge Edge AI system.

---

# Task B2 – Arithmetic Intensity and Roofline Analysis

## Roofline Analysis of the LogiEdge Inference Model

The Roofline Model is used to determine whether the inference workload is limited by processor computation or memory bandwidth.

### Given Parameters

| Parameter | Value |
|-----------|------:|
| Model Computation | 45 MFLOPs |
| Memory Access | 18 MB |
| Raspberry Pi 5 Compute Performance | 16 GFLOP/s |
| Memory Bandwidth | 12 GB/s |

---

## Step 1 – Arithmetic Intensity

Arithmetic Intensity (AI) is calculated as:

```
AI = Floating Point Operations / Data Movement
```

Model computation:

```
45 MFLOPs = 45 × 10⁶ FLOPs
```

Data accessed:

```
18 MB = 18 × 10⁶ Bytes
```

Therefore,

```
AI = (45 × 10⁶) / (18 × 10⁶)

AI = 2.5 FLOPs/Byte
```

**Arithmetic Intensity = 2.5 FLOPs/Byte**

---

## Step 2 – Ridge Point

The ridge point separates memory-bound and compute-bound execution.

```
Ridge Point = Peak Compute Performance / Memory Bandwidth
```

Substituting the given values:

```
= 16 GFLOP/s / 12 GB/s

= 1.33 FLOPs/Byte
```

**Ridge Point = 1.33 FLOPs/Byte**

---

## Step 3 – Performance Classification

| Metric | Value |
|--------|------:|
| Arithmetic Intensity | **2.5 FLOPs/Byte** |
| Ridge Point | **1.33 FLOPs/Byte** |

Since:

```
2.5 > 1.33
```

the inference model lies **to the right of the ridge point** on the Roofline graph.

Therefore, the workload is classified as **compute-bound** rather than **memory-bandwidth bound**.

This indicates that processor computation dominates inference time instead of memory transfers.

---

## Step 4 – Recommended Optimisation

Since the workload is compute-bound, reducing computational complexity will improve latency more effectively than increasing memory bandwidth.

Recommended optimisation techniques include:

- **Model Quantisation (FP32 → INT8)** to reduce computational complexity.
- **Model Pruning** to remove redundant parameters and decrease floating-point operations.
- **Hardware Acceleration** using the Hailo-8L AI accelerator to offload inference from the Raspberry Pi CPU.
- **Operator Fusion and Compiler Optimisation** using TensorFlow Lite, ONNX Runtime, and the Hailo compiler.

Increasing memory bandwidth alone would provide minimal performance improvement because the workload is already limited by computation.

---

## Conclusion

The calculated **Arithmetic Intensity is 2.5 FLOPs/Byte**, while the Raspberry Pi 5 has a **ridge point of 1.33 FLOPs/Byte**.

Since the Arithmetic Intensity exceeds the ridge point, the LogiEdge inference model is **compute-bound**.

Therefore, latency optimisation should focus on reducing computational workload through **quantisation, pruning, compiler optimisation, and AI hardware acceleration** rather than improving memory bandwidth.
