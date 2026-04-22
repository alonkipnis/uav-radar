# Uav Detection

*9 entries — [← Back to Index](../index.md)*

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

## Classification by Prediction for UAV and Bird Recognition Using Direct Phase Imagery from Millimeter-Wave Radar
**Teperovich, Kipnis** · None · IEEE Conference

This paper addresses the challenge of distinguishing small UAVs from birds using 60 GHz millimeter-wave radar, where both target types can appear similar in range and radar cross-section. The proposed Classification by Prediction (CBP) framework trains class-conditional models to predict the next radar phase frame, assigning labels based on whichever class-specific predictor achieves lower prediction error, thereby explicitly learning target motion dynamics rather than optimizing solely for label separation. CBP instantiated with ConvLSTM achieves the best overall accuracy and macro-F1 among all tested methods, including direct classifiers using ConvLSTM, Mamba, Transformer, ConvNet, and XGBoost backbones. The CBP-ConvLSTM approach also demonstrates superior robustness under varying SNR conditions with additive complex Gaussian noise.

**Key contribution:** The Classification by Prediction (CBP) framework, which uses class-conditional next-frame predictors on radar phase sequences, outperforms direct discriminative classifiers for UAV/bird recognition and is more robust at low SNR.

**Relevance:** This work directly addresses UAV detection and classification from radar data, proposing a novel prediction-based framework that leverages micro-Doppler and phase sequence dynamics to discriminate UAVs from birds using millimeter-wave FMCW MIMO radar.

---

## Synthetic Motion Pretraining Improves Next-Step Real UAV Trajectory Prediction Across Neural Architectures
**Raytsfeld, Kipnis** · None · None

This paper addresses the scarcity of real labeled UAV trajectory data for training neural sequence models by investigating synthetic motion pretraining as a sim-to-real transfer strategy. Physically plausible UAV trajectories are generated via a closed-loop PX4/Gazebo simulation and aligned with real optical-sensor measurements in a shared 3D unit-normalized directional representation. Three architectures (LSTM, S4, Mamba) are evaluated under real-only training, zero-shot transfer, and synthetic pretraining plus fine-tuning, with synthetic pretraining yielding 33–35% MSE reduction over real-only baselines. All synthetic-pretrained neural models outperform a classical IMM filter, whereas real-only trained versions underperformed it.

**Key contribution:** Synthetic pretraining with physically plausible closed-loop simulated UAV trajectories consistently and significantly improves next-step trajectory prediction across multiple neural architectures, outperforming a classical IMM baseline and substantially reducing dependence on scarce real labeled data.

**Relevance:** The sim-to-real trajectory prediction methodology and use of physics-based synthetic data generation directly support UAV tracking research, including radar-based contexts where real labeled data is similarly scarce.

---

## Discriminating UAV from non-UAVs, based on Time-series Location Data
**Ouattara, Kipnis** · None · None

This paper addresses the problem of discriminating UAVs from non-UAVs (airplanes, helicopters, birds, static objects) using azimuth and elevation time-series measurements collected via an EO/IR tracking system. Two approaches are compared: feature extraction combined with XGBoost/SVM classification, and a Transformer-based sequence classification neural network operating directly on position sequences. The Transformer consistently achieves ~95% F1 score outperforming XGBoost (~90% F1), particularly on challenging data slices identified through freaAI analysis. The study also introduces a careful train/test splitting strategy to prevent sequence overlap and ensure fair evaluation.

**Key contribution:** Transformer-based sequence classification outperforms XGBoost feature-extraction methods for UAV discrimination, especially on difficult data slices, demonstrating the advantage of end-to-end deep learning on raw position time-series.

**Relevance:** This work directly addresses UAV versus non-UAV discrimination from radar-like track data (azimuth/elevation), comparing classical feature engineering against deep learning sequence models, which is central to UAV detection and classification in radar research.

---

## Survey of Radar-Based UAV Detection Methods
**** · ? · 

A comprehensive survey covering radar-based methods for unmanned aerial vehicle detection, reviewing current approaches, techniques, and challenges in the field. The resource synthesizes existing literature to provide an overview of the state of the art in radar-based UAV detection.

**Key contribution:** 

**Relevance:** 

---

## Open UAV Radar Dataset with Annotations
**** · ? · 

An open-source UAV radar dataset hosted on GitHub that includes annotated radar data for UAV detection research. The dataset provides labeled examples suitable for training and evaluating UAV detection and classification algorithms.

**Key contribution:** 

**Relevance:** 

---
