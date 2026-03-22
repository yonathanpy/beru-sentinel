<p align="center">
  <img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/security.svg" width="180" />
</p>

<h1 align="center">BERU SENTINEL</h1>
<p align="center">High-Performance Log Intelligence & Anomaly Detection Engine</p>

---

## 1. Overview

Beru Sentinel is a multi-threaded log processing engine designed to analyze large-scale log datasets and extract anomalous patterns using deterministic detection techniques.

The system is optimized for:
- High throughput log ingestion
- Concurrent analysis
- Rule-based anomaly detection
- Behavioral tracking using frequency models

It is intended for defensive security analysis, monitoring, and research.

---

## 2. Core Capabilities

### 2.1 Throughput
- Handles ~50k–150k log lines/minute (depends on CPU threads and I/O)
- Thread batching model with configurable limits
- Memory-efficient streaming (no full file load)

### 2.2 Detection Layers
1. Pattern Matching Engine (string-based signatures)
2. Behavioral Detection (IP frequency tracking)
3. Payload Heuristics (length-based anomaly detection)

### 2.3 Concurrency Model
- Thread-per-line execution (batched)
- Lock-based shared storage
- Configurable thread cap (default: 50)

---

## 3. Architecture
