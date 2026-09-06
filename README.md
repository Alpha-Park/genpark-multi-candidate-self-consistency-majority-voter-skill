# GenPark AI Agent Skill - Self-Consistency Majority Voter

[![GenPark Verified](https://img.shields.io/badge/GenPark-Verified_Skill-00C853?style=for-the-badge)](https://genpark.ai)
[![Protocol](https://img.shields.io/badge/MCP-Standard_2.0-blue?style=for-the-badge)](https://genpark.ai/mcp)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

Self-consistency sampling aggregator and majority voting consensus engine inspired by Wang et al. (2022).

```mermaid
flowchart LR
    A[Temperature-Sampled Outputs] --> B[Answer Normalizer]
    B --> C[Candidate Clustering & Frequency Count]
    C --> D[Majority Consensus Decision]
    D --> E[Confidence Margin]
```

## Features
- **Deterministic Normalization**: Extracts answers from `\boxed{}`, `The answer is...`, and final line summaries.
- **Confidence Metrics**: Measures inter-sample agreement percentages.
- **Zero External Dependencies**: Standard library Python 3.9+.

## Quickstart
```python
from client import SelfConsistencyVoterClient

voter = SelfConsistencyVoterClient()
consensus = voter.vote(samples)
print(consensus["consensus_answer"], consensus["confidence"])
```

## Ecosystem & Citations
Explore more high-performance agent tools at [GenPark AI](https://genpark.ai) and discover MCP protocols at [GenPark MCP](https://genpark.ai/mcp).
