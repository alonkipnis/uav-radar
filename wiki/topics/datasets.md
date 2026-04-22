# Datasets

*5 entries — [← Back to Index](../index.md)*

## Millimeter Wave Radar Measurements: Distinguishing UAS and Birds Based on 60 GHz micro-Doppler Signatures
**Kang, Forsten, Skrimponis, et al.** · 2024 · VTC2024-Fall

This paper addresses the challenge of distinguishing small UAVs from birds using a 60 GHz FMCW MIMO millimeter-wave radar by analyzing micro-Doppler signatures arising from rotating propellers versus flapping wings. Measurements were conducted in an anechoic chamber across multiple azimuth and elevation angles for two DJI drones and a bionic bird, producing amplitude and phase radar data. A CNN was applied to amplitude features and a ConvLSTM to phase difference features for classification. Results show that phase-based classification can reliably differentiate drones from birds even under high noise variance, demonstrating strong potential for airport security applications.

**Key contribution:** Phase difference of 60 GHz micro-Doppler radar signals, exploited via a ConvLSTM model, enables robust classification of UAVs versus birds even in high-noise conditions.

**Relevance:** This paper directly addresses UAV detection and classification using radar micro-Doppler signatures at mmWave frequencies, providing both a measurement dataset and neural network classification approaches applicable to UAV radar research.

---

## UAV Classification with Mamba
**Raanan** · 2024 · MLDS, Reichman University (Final Project Report)

This paper addresses the problem of classifying flying objects (UAV, bird, airplane, static-object) using trajectory time-series data rather than image-based approaches. The proposed method trains a separate Mamba generative forecasting model per class, then classifies an unknown trajectory by comparing prediction errors across all class models, assigning the label of the model with the lowest error. The Walaris dataset, consisting of 3D directional tracking data at ~25 fps, is used for evaluation, and classification accuracy is assessed at multiple time intervals (5–30 seconds) after first encounter. Results are compared against feature-based baseline methods (e.g., Random Forest, SVM), demonstrating the potential of Mamba's state-space model architecture for real-time, low-latency UAV classification.

**Key contribution:** A comparative forecasting framework using per-class Mamba models classifies UAV trajectories in real-time by selecting the class whose model yields the lowest prediction error, enabling early and incremental classification from trajectory data alone.

**Relevance:** This work directly addresses UAV detection and classification using trajectory data that can complement radar-based sensing, particularly for long-range scenarios where image resolution is insufficient.

---

## Synthetic Motion Pretraining Improves Next-Step Real UAV Trajectory Prediction Across Neural Architectures
**Raytsfeld, Kipnis** · None · None

This paper addresses the scarcity of real labeled UAV trajectory data for training neural sequence models by investigating synthetic motion pretraining as a sim-to-real transfer strategy. Physically plausible UAV trajectories are generated via a closed-loop PX4/Gazebo simulation and aligned with real optical-sensor measurements in a shared 3D unit-normalized directional representation. Three architectures (LSTM, S4, Mamba) are evaluated under real-only training, zero-shot transfer, and synthetic pretraining plus fine-tuning, with synthetic pretraining yielding 33–35% MSE reduction over real-only baselines. All synthetic-pretrained neural models outperform a classical IMM filter, whereas real-only trained versions underperformed it.

**Key contribution:** Synthetic pretraining with physically plausible closed-loop simulated UAV trajectories consistently and significantly improves next-step trajectory prediction across multiple neural architectures, outperforming a classical IMM baseline and substantially reducing dependence on scarce real labeled data.

**Relevance:** The sim-to-real trajectory prediction methodology and use of physics-based synthetic data generation directly support UAV tracking research, including radar-based contexts where real labeled data is similarly scarce.

---

## Open UAV Radar Dataset with Annotations
**** · ? · 

An open-source UAV radar dataset hosted on GitHub that includes annotated radar data for UAV detection research. The dataset provides labeled examples suitable for training and evaluating UAV detection and classification algorithms.

**Key contribution:** 

**Relevance:** 

---

## Papers With Code: Object Detection Benchmarks and Methods
**** · ? · 

A comprehensive collection of object detection papers, state-of-the-art benchmarks, and associated code implementations. Provides leaderboards and comparisons across standard datasets useful for adapting detection methods to UAV radar applications.

**Key contribution:** 

**Relevance:** 

---
