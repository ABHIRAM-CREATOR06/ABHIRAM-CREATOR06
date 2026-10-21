# Abhiram P

<img src="https://avatars.githubusercontent.com/u/175493779?v=4&s=240" alt="Profile photo of Abhiram P" width="120" height="120" align="right">

Systems-oriented software engineer working on network simulation, applied cryptography, and backend tooling, mostly in Rust, Node.js, and C#.

Computer Science at SNGCE (APJ AKTU), Kerala · class of 2027

## Selected projects

### [Halonyx](https://github.com/ABHIRAM-CREATOR06/Halonyx)

A self-hostable end-to-end encrypted messenger, built as a from-first-principles implementation of the Signal Protocol.

Node.js, WebSocket, and SQLite, with X3DH and the Double Ratchet implemented on Web Crypto rather than wrapped around `libsignal`.

- **Key verification:** 60-digit Safety Numbers and key-change warnings help users detect identity-key substitution by a malicious server.
- **Data handling:** identity details and operational data live in separate SQLite databases linked only by a hash. Files move peer to peer over WebTorrent. Group membership is carried inside client-side encrypted envelopes, using pairwise ratchet fan-out.
- **Client-side DLP:** scans outgoing messages for cloud credentials, tokens, private keys, and Luhn-validated card numbers before encryption, and can block or warn.
- **Testing:** protocol and authentication tests run in CI on Node.js 20, 22, and 24. The build fails if the X25519 tests are skipped instead of passed.
- **Documented limits:** the threat model lists 25 threats, each with a status. Open items include WebRTC IP exposure, signup email enumeration, and missing WebSocket origin validation. The project has not been independently audited and is not meant for production use.

[Threat model](https://github.com/ABHIRAM-CREATOR06/Halonyx/blob/main/specification_docs/security_docs/datathreat.md) · [Benchmarks](https://github.com/ABHIRAM-CREATOR06/Halonyx/blob/main/specification_docs/benchmark/benchmark.md) · [Protocol security analysis](https://github.com/ABHIRAM-CREATOR06/Halonyx/blob/main/protocol/SECURITY_ANALYSIS.md) · [Protocol simulator](https://github.com/ABHIRAM-CREATOR06/Halonyx/tree/main/simulator) · [Live demo](https://halonyx.onrender.com)

### [PulseCast](https://github.com/ABHIRAM-CREATOR06/Network-Pulse-Mapper)

A network simulator that shows how congestion spreads and lets you test routing strategies against it.

A Rust/Tokio simulation core streams live telemetry over WebSocket to a React, D3, and Canvas front end.

- **Network model:** virtual nodes with bounded packet queues, connected by links with configurable bandwidth, latency, jitter, and loss. Effective loss rises as endpoint queues fill.
- **Forecasting:** a diffusion heuristic (no ML) scores each node's congestion risk ten seconds ahead and logs its error against actual queue occupancy.
- **Routing:** four strategies, switchable at runtime per node or globally: shortest path, congestion-aware, predictive reroute, and memory-based.
- **Fault injection:** eight scenarios, including traffic bursts, cascading congestion, link failure, and bandwidth collapse.
- **Status:** working MVP, localhost only. A forecast-error view and side-by-side routing comparison are still planned.

[Architecture](https://github.com/ABHIRAM-CREATOR06/Network-Pulse-Mapper/blob/main/architecture.md) · [Design system](https://github.com/ABHIRAM-CREATOR06/Network-Pulse-Mapper/blob/main/design.md)

### [AXIS](https://github.com/ABHIRAM-CREATOR06/Acess1)

A Windows desktop tool that checks web pages against WCAG 2.2 and reports what to fix.

Built with WPF and .NET 9. It audits a URL or a local HTML file.

- **Rendering:** loads JavaScript-heavy pages in headless Chrome through PuppeteerSharp, with an HTTP fallback.
- **Checks:** alt text, form labels, heading hierarchy, color contrast, font readability, and the WCAG 2.2 criteria for target size (2.5.8) and redundant entry (3.3.7).
- **Reports:** severity-coded findings, a 0 to 100 score, TXT or PDF export, and a page carbon-footprint estimate.
- **SDK:** AXIS-CORE for .NET, JavaScript, and Rust. The [Rust crate](https://docs.rs/axis-core) is published and fetches pages over HTTP rather than rendering them.
- **Scope:** Windows only. Automated checks cover a subset of WCAG and complement manual review.

[SDK docs](https://github.com/ABHIRAM-CREATOR06/Acess1/blob/main/AXIS-CORE-SDK-DOCS.md) · [Roadmap](https://github.com/ABHIRAM-CREATOR06/Acess1/blob/main/ROADMAP.md)

### [Trinetra](https://github.com/ABHIRAM-CREATOR06/Trinetra)

A research prototype that combines SIM, device, and point-of-sale signals into a fraud-risk score for investigators.

Rust, Axum, SQLx, and SQLite, exposing an API for scoring subscribers and managing investigations.

- **Rules:** six weighted checks: SIM concentration, shared devices, blacklisted IMEIs, fraud reports, suspicious points of sale, and geographic anomalies.
- **Workflow:** scores map to LOW, MEDIUM, HIGH, or VERY HIGH. HIGH and above opens an investigation record. Endpoints support status updates and an audit log.
- **Data:** a Python generator creates 500+ synthetic subscribers and eight fraud scenarios.
- **Scope:** rule weights are set by hand, and nothing has been tested on real telecom data.

## Skills

- **Languages:** Rust, JavaScript, TypeScript, C#, Python
- **Systems and networking:** Tokio, WebSocket, UDP, WebRTC, WebTorrent, routing algorithms
- **Security and cryptography:** X3DH, Double Ratchet, AES-256-GCM, HKDF, HMAC, Web Crypto (X25519, P-256), STRIDE threat modelling, JWT auth, rate limiting
- **Backend:** Node.js, Express, Axum, warp, SQLite, REST APIs
- **Frontend and desktop:** React, D3, Vite, .NET 9, WPF
- **CI:** GitHub Actions

Currently exploring Apache Spark and Databricks.

## Elsewhere

[DEV](https://dev.to/abhiramp_2005) · [Medium](https://medium.com/@abhirampraneeth2005) · [LinkedIn](https://www.linkedin.com/in/abhiram-p-3a1b49290/)
