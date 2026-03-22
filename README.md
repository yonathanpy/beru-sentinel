<p align="center">
  <img src="https://wallpapercave.com/wp/wp13373871.png" width="1200" height="400" />
</p>

<h1 align="center">BERU SENTINEL</h1>
<p align="center">High-Performance Log Intelligence & Anomaly Detection Engine</p>
---

## 1. Overview

Beru Sentinel is a multi-threaded log processing engine designed to analyze large-scale log datasets and detect anomalous behavior using deterministic rule-based detection.

Optimized for:
- High-throughput log ingestion
- Concurrent processing
- Pattern-based anomaly detection
- IP-based behavioral tracking

---

## 2. Core Capabilities

### 2.1 Throughput
- Processes ~50k–150k log lines per minute (hardware-dependent)
- Streaming-based processing (no full file load)
- Thread batching for controlled concurrency

### 2.2 Detection Layers
1. **Pattern Matching Engine** — signature-based detection
2. **Behavioral Detection** — frequency tracking per IP
3. **Payload Heuristics** — length anomaly detection

### 2.3 Concurrency Model
- Thread-per-task execution (batched)
- Mutex-protected shared storage
- Configurable thread cap (default: 50)

---

## 3. Architecture
