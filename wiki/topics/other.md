# Other

*5 entries — [← Back to Index](../index.md)*

## Situational Awareness enabled by Integrated Sensing And Communication in 6G (SAISAC)
**Chatterjee, Thobaben, Bengtsson, et al.** · 2025 · NSTC-SSF Collaborative Research Framework

The SAISAC project proposes to develop situational awareness capabilities using Integrated Sensing and Communication (ISAC) in 6G networks, with a primary focus on detecting, classifying, and tracking drones and electromagnetic emitters. The core challenges addressed include the absence of labeled data for hostile objects, distributed data availability across multiple base stations, and the need for rapid adaptation to new scenarios. The proposed approach combines unsupervised and semi-supervised learning, federated/distributed learning across 6G base stations, and foundational AI models augmented with multimodal data. The system targets autonomous operation with minimal human intervention, leveraging sparsity-aware signal processing and deep neural networks.

**Key contribution:** The project proposes an autonomous, distributed ISAC-based situational awareness framework combining unsupervised learning and federated learning to detect, deinterleave, and track drones without requiring labeled training data.

**Relevance:** This project is directly relevant to UAV radar research as it specifically targets drone detection, classification, and tracking using radar-like sensing within 6G ISAC infrastructure, addressing key challenges of unlabeled data and multi-station distributed sensing.

---

## Koopman Operator Theory for Nonlinear Dynamic Modeling using Dynamic Mode Decomposition
**Snyder, Song** · 2021 · arXiv

This paper addresses the challenge of modeling and controlling nonlinear dynamical systems by applying Koopman operator theory to lift nonlinear dynamics into an infinite-dimensional linear space. The authors use data-driven methods, specifically Dynamic Mode Decomposition (DMD) and Extended DMD (EDMD), to approximate a finite-dimensional linear representation of the Koopman operator. They demonstrate the approach through numerical simulations on classic dynamical systems (inverted pendulum and cart-pole), showing that linear control strategies such as LQR can be applied to inherently nonlinear systems. The results illustrate the effectiveness and limitations of DMD-based Koopman approximations for system identification and control.

**Key contribution:** The paper demonstrates that Extended DMD can approximate a finite-dimensional Koopman operator representation of nonlinear systems, enabling linear control design without linearization around fixed points.

**Relevance:** Koopman operator and DMD-based linear modeling of nonlinear dynamics could be applied to UAV motion modeling and tracking from radar data, enabling linear filtering and control methods on inherently nonlinear UAV flight dynamics.

---

## Forecasting Sequential Data Using Consistent Koopman Autoencoders
**Azencot, Erichson, Lin, Mahoney** · 2020 · ICML

This paper addresses the problem of forecasting high-dimensional nonlinear dynamical systems from sequential data by proposing a Consistent Koopman Autoencoder model. The approach leverages both forward and backward dynamics through Koopman operator theory, embedding nonlinear dynamics into a linear latent space via an autoencoder network with physics-based consistency constraints. The model is evaluated on systems such as pendulum, cylinder flow, vortex flow, and climate data, achieving accurate predictions over significant horizons while remaining robust to noise. Key advantages include time reversibility and stable behavior over long prediction horizons.

**Key contribution:** A Consistent Koopman Autoencoder that jointly leverages forward and backward dynamics to produce accurate, noise-robust forecasts of nonlinear sequential data within a physics-constrained learning framework.

**Relevance:** While not directly focused on UAV radar, the Koopman-based framework for modeling nonlinear dynamical systems could be applicable to radar-based UAV tracking, where the motion dynamics of UAVs are nonlinear and sequential state estimation is critical.

---

## Learning Koopman Invariant Subspaces for Dynamic Mode Decomposition
**Takeishi, Kawahara, Yairi** · 2017 · NIPS

This paper addresses the problem of performing Koopman spectral analysis and dynamic mode decomposition (DMD) on nonlinear dynamical systems without requiring manually crafted observable functions. The authors propose a data-driven method called Learning Koopman Invariant Subspaces (LKIS) that uses neural networks to learn a set of observables which span a Koopman invariant subspace by minimizing the residual sum of squares of linear least-squares regression. The approach automatically discovers the nonlinear feature transformations needed for DMD to work correctly on unknown nonlinear dynamics. Empirical evaluations on several nonlinear dynamical systems demonstrate the feasibility and effectiveness of the LKIS-based DMD framework.

**Key contribution:** A fully data-driven neural network-based method to automatically learn Koopman invariant subspaces for dynamic mode decomposition, eliminating the need for manually designed observable functions in nonlinear dynamical system analysis.

**Relevance:** While not directly focused on UAV radar, the Koopman operator and DMD framework proposed here could be applied to nonlinear dynamics modeling of UAV motion patterns extracted from radar time-series data for tracking or classification purposes.

---

## Synthetic Motion Pretraining Improves Next-Step Real UAV Trajectory Prediction Across Neural Architectures
**Raytsfeld, Kipnis** · None · None

This paper addresses the scarcity of real labeled UAV trajectory data for training neural sequence models by investigating synthetic motion pretraining as a sim-to-real transfer strategy. Physically plausible UAV trajectories are generated via a closed-loop PX4/Gazebo simulation and aligned with real optical-sensor measurements in a shared 3D unit-normalized directional representation. Three architectures (LSTM, S4, Mamba) are evaluated under real-only training, zero-shot transfer, and synthetic pretraining plus fine-tuning, with synthetic pretraining yielding 33–35% MSE reduction over real-only baselines. All synthetic-pretrained neural models outperform a classical IMM filter, whereas real-only trained versions underperformed it.

**Key contribution:** Synthetic pretraining with physically plausible closed-loop simulated UAV trajectories consistently and significantly improves next-step trajectory prediction across multiple neural architectures, outperforming a classical IMM baseline and substantially reducing dependence on scarce real labeled data.

**Relevance:** The sim-to-real trajectory prediction methodology and use of physics-based synthetic data generation directly support UAV tracking research, including radar-based contexts where real labeled data is similarly scarce.

---
