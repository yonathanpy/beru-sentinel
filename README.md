<p align="center">
  <img src="https://i.pinimg.com/originals/XX/XX/XXXXXX.jpg" width="100%" style="max-width: 600px;">
</p>
----
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

The Beru Sentinel Engine is designed for high-throughput log processing with strict thread safety and a modular architecture.

### System Overview

```text
CLI
│
▼
Engine
├── Parser
├── Analyzer
│   ├── Pattern Engine
│   └── Behavioral Tracker
├── Storage (thread-safe)
└── Logger
````


- **Parser:** Converts raw log lines into structured entries.
- **Analyzer:** Runs multiple detection layers (pattern, behavior, payload length).
- **Storage:** Keeps alerts and metadata in memory with thread locks.
- **Logger:** Outputs structured results for monitoring.

---

## 4. Module Breakdown

### 4.1 Parser Layer
- Extracts IP addresses with regex: `(\d+\.\d+\.\d+\.\d+)`  
- Identifies HTTP methods: GET, POST, PUT, DELETE  
- Captures payload length  
- Handles up to 1500 characters per line  

Time complexity: **O(n)** per line  

### 4.2 Analyzer Layer
- **Pattern Matching:** Detects SQLI, XSS, LFI using pre-defined signatures  
- **Behavioral Detection:** Tracks IP activity. Example: `if requests > 40 → BRUTE_FORCE`  
- **Payload Heuristics:** Alerts on unusually long payloads  

Complexity: **O(p × l)** where `p = # patterns`, `l = line length`

### 4.3 Storage Layer
- Thread-safe dictionary: `alert_type → [entries]`  
- Memory-efficient in-memory storage  
- Dynamically allocates storage for large datasets

### 4.4 Execution Model
1. Stream log lines from file or stdin  
2. Spawn worker threads  
3. Parse → Analyze → Store → Log  
4. Join threads and output results

Thread control:
```python
if active_threads >= thread_limit:
    join_all_threads()
```
5. Configuration

File: config.json
```{
  "thread_limit": 50,
  "bruteforce_threshold": 40,
  "max_line_length": 1500
}
````
````
| Key                  | Description                  | Default |
| -------------------- | ---------------------------- | ------- |
| thread_limit         | Max concurrent threads       | 50      |
| bruteforce_threshold | Requests per IP before alert | 40      |
| max_line_length      | Payload anomaly threshold    | 1500    |
````
6. Usage
````
python cli.py logs.txt
````
Requirements:

Input: plain text logs
UTF-8 preferred (other encodings handled safely)
Line-separated entries

6.1 Keys & Security Tokens

Beru Sentinel supports optional API keys and access tokens for integration with external services (like SIEMs, alert systems, or dashboards). All keys are stored locally in keys.json and never sent externally by default.

Example keys.json:
````
Optional Keys (placeholders):
- Slack webhook: `https://hooks.slack.com/services/...`
- PagerDuty token: `PDxxxxxxxxxx`
- Email token: `SMTP-USER:SMTP-PASS`
````
````
| Key               | Purpose                       | Notes    |
| ----------------- | ----------------------------- | -------- |
| slack_webhook     | Send alerts to Slack channels | Optional |
| pagerduty_token   | Trigger PagerDuty incidents   | Optional |
| email_alert_token | Send email alerts             | Optional |
````
Usage with CLI
````
python cli.py logs.txt --keys keys.json
````
The tool reads the keys.json file if provided.
Alerts are sent only if keys are valid.
Keys are encrypted at rest using internal AES-256 (built-in).
Security Notes
Never commit real tokens to public repositories.
Use placeholders or .env files for sensitive keys.
Beru Sentinel validates key format before sending alerts to prevent misfires.

7. Output Example
````
[SQLI] (12)
GET /index.php?id=1 UNION SELECT ...
...

[BRUTE_FORCE] (5)
POST /login ...
...
````
Alerts are grouped by type and count.

| Metric          | Value              |
| --------------- | ------------------ |
| Throughput      | 50k–150k lines/min |
| Memory Usage    | 5–50 MB            |
| CPU Scaling     | Near-linear        |
| Max Tested File | 1.2 GB             |

9. Limitations
In-memory storage only
Signature-based detection (no ML)
No distributed processing
Thread overhead beyond 200 threads

10. Extension Points
Add new detection patterns: core/patterns.py
Extend Analyzer logic: core/analyzer.py
Swap Storage backend: core/storage.py (SQLite / Redis / File)

11. Security Scope
Non-intrusive: Does not scan or attack any targets
Defensive use only: Analyzes logs you provide
Suitable for: Incident response, monitoring, and alert generation

12. Roadmap
Async processing (event loop)
Plugin system for custom detections
Database integration (SQLite / PostgreSQL)
REST API support
Real-time streaming ingestion

13. Design Principles
Deterministic processing
Minimal dependencies
High performance
Modular and extensible.

