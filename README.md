<p align="center">
  <img src="assets/beru.png" width="220"/>
</p>

<h1 align="center">BERU SENTINEL</h1>
<p align="center">High-Performance Log Intelligence Engine</p>
## 1. Overview

Beru Sentinel is a multi-threaded log processing engine designed to analyze large-scale log datasets and extract anomalous patterns using deterministic detection techniques.

The system is optimized for:
- High throughput log ingestion
- Concurrent analysis
- Rule-based anomaly detection
- Behavioral tracking using frequency models

---

## 2. Core Capabilities

### 2.1 Throughput
- Processes ~50,000 to 150,000 log lines per minute (hardware dependent)
- Streaming-based processing (no full memory load)
- Thread batching for controlled concurrency

### 2.2 Detection Layers
1. Pattern Matching Engine (signature-based)
2. Behavioral Detection (IP frequency tracking)
3. Payload Heuristics (length anomaly detection)

### 2.3 Concurrency Model
- Thread-per-task execution (batched)
- Mutex-protected shared storage
- Configurable thread cap (default: 50)

---

## 3. Architecture
