# Tracking

*7 entries — [← Back to Index](../index.md)*

## DAiR Radar – Device and Operation Summary
**Reichman** · 2026 · None

This document describes the DAiR tactical multi-mission X-band radar system developed for UAV detection and tracking, covering its hardware architecture, signal processing principles, and data output formats. The radar operates at 9-10 GHz with a software-defined architecture featuring a 320-element digital receive array enabling simultaneous beamforming, Track-While-Search operation, and GPU-based processing. Key outputs include per-CPI detection plots, tracks with full kinematics, and range-Doppler cubes that enable micro-Doppler signature extraction for discriminating UAVs from birds. The document serves as a technical reference for algorithm developers working on classification and tracking using the radar's ICD data model.

**Key contribution:** Provides a comprehensive technical specification of the DAiR X-band radar system—including its antenna configuration, FMCW/Doppler processing chain, and ICD data model—serving as the foundational reference for UAV-focused radar algorithm development.

**Relevance:** This document directly describes the radar hardware, signal model, and data format used in the Reichman UAV Radar Project, making it essential reference material for developing UAV detection, classification, and tracking algorithms from DAiR radar data.

---

## Situational Awareness enabled by Integrated Sensing And Communication in 6G (SAISAC)
**Chatterjee, Thobaben, Bengtsson, et al.** · 2025 · NSTC-SSF Collaborative Research Framework

The SAISAC project proposes to develop situational awareness capabilities using Integrated Sensing and Communication (ISAC) in 6G networks, with a primary focus on detecting, classifying, and tracking drones and electromagnetic emitters. The core challenges addressed include the absence of labeled data for hostile objects, distributed data availability across multiple base stations, and the need for rapid adaptation to new scenarios. The proposed approach combines unsupervised and semi-supervised learning, federated/distributed learning across 6G base stations, and foundational AI models augmented with multimodal data. The system targets autonomous operation with minimal human intervention, leveraging sparsity-aware signal processing and deep neural networks.

**Key contribution:** The project proposes an autonomous, distributed ISAC-based situational awareness framework combining unsupervised learning and federated learning to detect, deinterleave, and track drones without requiring labeled training data.

**Relevance:** This project is directly relevant to UAV radar research as it specifically targets drone detection, classification, and tracking using radar-like sensing within 6G ISAC infrastructure, addressing key challenges of unlabeled data and multi-station distributed sensing.

---

## UAV Classification with Mamba
**Raanan** · 2024 · MLDS, Reichman University (Final Project Report)

This paper addresses the problem of classifying flying objects (UAV, bird, airplane, static-object) using trajectory time-series data rather than image-based approaches. The proposed method trains a separate Mamba generative forecasting model per class, then classifies an unknown trajectory by comparing prediction errors across all class models, assigning the label of the model with the lowest error. The Walaris dataset, consisting of 3D directional tracking data at ~25 fps, is used for evaluation, and classification accuracy is assessed at multiple time intervals (5–30 seconds) after first encounter. Results are compared against feature-based baseline methods (e.g., Random Forest, SVM), demonstrating the potential of Mamba's state-space model architecture for real-time, low-latency UAV classification.

**Key contribution:** A comparative forecasting framework using per-class Mamba models classifies UAV trajectories in real-time by selecting the class whose model yields the lowest prediction error, enabling early and incremental classification from trajectory data alone.

**Relevance:** This work directly addresses UAV detection and classification using trajectory data that can complement radar-based sensing, particularly for long-range scenarios where image resolution is insufficient.

---

## Estimating Optimal Tracking Filter Performance for Manned Maneuvering Targets
**Singer** · 1970 · IEEE Transactions on Aerospace and Electronic Systems

This paper addresses the problem of accurately tracking manned maneuverable vehicles (aircraft, ships, submarines) using radar and other sensors. The author derives an optimal Kalman filter based on a three-state target motion model that represents acceleration as a correlated random process with exponential autocorrelation, driven by white noise. The model is simpler (3 states vs 4) than prior work while achieving over 30% better performance by assuming a constant velocity baseline trajectory. Parametric tracking accuracy data are generated as a function of maneuver characteristics, sensor noise, and data rate to enable rapid a priori performance estimates.

**Key contribution:** The Singer acceleration model—representing target maneuvers as an exponentially correlated random process—enables a tractable, optimal Kalman filter that significantly outperforms prior discrete-time approaches for tracking maneuvering airborne targets.

**Relevance:** This foundational paper establishes the Singer target model and optimal Kalman filter for tracking maneuvering aerial targets from radar measurements, forming a cornerstone methodology directly applicable to UAV tracking filter design.

---

## Synthetic Motion Pretraining Improves Next-Step Real UAV Trajectory Prediction Across Neural Architectures
**Raytsfeld, Kipnis** · None · None

This paper addresses the scarcity of real labeled UAV trajectory data for training neural sequence models by investigating synthetic motion pretraining as a sim-to-real transfer strategy. Physically plausible UAV trajectories are generated via a closed-loop PX4/Gazebo simulation and aligned with real optical-sensor measurements in a shared 3D unit-normalized directional representation. Three architectures (LSTM, S4, Mamba) are evaluated under real-only training, zero-shot transfer, and synthetic pretraining plus fine-tuning, with synthetic pretraining yielding 33–35% MSE reduction over real-only baselines. All synthetic-pretrained neural models outperform a classical IMM filter, whereas real-only trained versions underperformed it.

**Key contribution:** Synthetic pretraining with physically plausible closed-loop simulated UAV trajectories consistently and significantly improves next-step trajectory prediction across multiple neural architectures, outperforming a classical IMM baseline and substantially reducing dependence on scarce real labeled data.

**Relevance:** The sim-to-real trajectory prediction methodology and use of physics-based synthetic data generation directly support UAV tracking research, including radar-based contexts where real labeled data is similarly scarce.

---

## Survey of Radar-Based UAV Detection Methods
**** · ? · 

A comprehensive survey covering radar-based methods for unmanned aerial vehicle detection, reviewing current approaches, techniques, and challenges in the field. The resource synthesizes existing literature to provide an overview of the state of the art in radar-based UAV detection.

**Key contribution:** 

**Relevance:** 

---

## Papers With Code: Object Detection Benchmarks and Methods
**** · ? · 

A comprehensive collection of object detection papers, state-of-the-art benchmarks, and associated code implementations. Provides leaderboards and comparisons across standard datasets useful for adapting detection methods to UAV radar applications.

**Key contribution:** 

**Relevance:** 

---
