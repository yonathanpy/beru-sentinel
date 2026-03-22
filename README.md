<p align="center">
  <img src="https://img.icons8.com/external-flat-juicy-fish/200/external-ant-animal-flat-flat-juicy-fish.png" width="200" />
</p>

# Beru Sentinel

Beru Sentinel is a high-performance log analysis engine designed for detecting anomalies and suspicious activity patterns in large-scale log datasets.

## Overview

The system processes raw log data and applies layered detection mechanisms including:

- Pattern-based attack detection
- Behavioral analysis (IP frequency tracking)
- Payload anomaly detection

## Key Features

- Multi-threaded processing
- Configurable detection thresholds
- Modular architecture
- Thread-safe storage engine
- Fast parsing pipeline

## Detection Capabilities

- SQL Injection patterns
- Cross-site scripting indicators
- Local file inclusion attempts
- Brute-force behavior detection
- Oversized payload detection

## Execution

```bash
python cli.py logs.txt
