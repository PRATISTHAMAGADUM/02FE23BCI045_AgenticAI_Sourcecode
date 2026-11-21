# Faculty Appraisal Management System (Agentic AI)

**Student Name:** Pratiksha Magadum  
**USN:** 02FE23BCI045  
**Course:** Agentic AI (Comprehensive Labs 1–12 Implementation)  
**Department:** School of Computer Science & Engineering, KLE Technological University, Dr. M. S. Sheshagiri Campus, Belagavi  
**Academic Year:** 2026–27  

> **Notice:** *This is an educational prototype using synthetic data.*  
> **Scoring Policy Disclaimer:** *Demo Appraisal Policy — configurable; not official institutional scoring policy.*

---

## Executive Summary

The Faculty Appraisal Management System is an autonomous multi-agent workbench that automates the preparation of annual faculty appraisal dossiers. It brings together evidence from research, teaching, and institutional administration, using specialized domain agents to collect and validate submissions.

After validation, the system calculates a deterministic score using configurable demo rules and generates PDF and JSON reports for human review. A coordinator manages the workflow, while the SQLite-backed system records appraisal data and execution activity.

The project demonstrates 12 Agentic AI concepts, including tool use, memory, agent collaboration, workflow graphs, deep research, and responsible autonomy. It also provides a Streamlit dashboard, a FastAPI backend, and a CLI runner (`run.py`).

---

## 1. System Architecture & Complete 12 Core Concepts Mapping

| Course Lab | Core Concept | Implementation in This Project |
|---|---|---|
| **Lab 1** | **Agent vs Chatbot** | Autonomous domain agents executing proactive `PLAN ➔ ACT ➔ OBSERVE ➔ DECIDE` cycles; explicit exception handling. |
| **Lab 2** | **Tool-Using Agent** | 12 modular tools across files, database, arithmetic calculation, and PDF/JSON generation managed via `ToolRegistry`. |
| **Lab 3** | **Skill Creation** | 6 reusable skills with `SKILL.md` specifications and code classes loaded through dynamic `SKILL_REGISTRY`. |
| **Lab 4** | **Memory & Retrieval** | Persistent scoped memory backed by SQLite (`faculty:FAC001`) preventing cross-faculty contamination; comparative multi-session analysis. |
| **Lab 5** | **MCP-Style Connector** | Educational MCP Server exposing discoverable `CAPABILITIES` manifest (`file_read`, `db_query`, `api_get`), allowed callers, SELECT-only guards, directory traversal protection. |
| **Lab 6** | **OpenCLA Runtime** | Domain-agnostic runtime (`receive_task()`, dynamic `select_skill()`, audit logging, failure recording, extensibility without core rewrites). |
| **Lab 7** | **Node Graphs** | Explicit Directed Acyclic Graph (`StateGraph`) with parallel branches, conditional quality routing, and checkpointed `HumanGateNode`. |
| **Lab 8** | **Parallel Swarms** | Decentralized 4-peer agent collaboration over a shared `MessageBoard` with independent proposals, peer cross-critiques, and automated consensus conflict resolution. |
| **Lab 9** | **Deep Research** | Autonomous 5-phase research loop (`Question ➔ Search ➔ Extract ➔ Compare ➔ Synthesize`), bibliometric cross-referencing, Citation Truth Table, and Research Integrity Quotient. |
| **Lab 10** | **Cloud Operations** | Live telemetry signal probing (latency, storage, error rate), root-cause diagnostic engine, and self-healing remediation plans guarded by human approval gates. |
| **Lab 11** | **Agentic SDLC** | Agent-run software delivery factory: requirement intake, specification, code diff synthesis, automated test synthesis, regression runner, and release sign-off. |
| **Lab 12** | **Responsible Autonomy** | Cryptographic SHA-256 rolling hash audit chain (tamper-evident log), state snapshot & rollback engine, EEOC Four-Fifths demographic parity evaluator, and PII masking. |

---

## 2. The Six Domain Agents & Coordinator

### Domain Agents
1. **Research Data Collection Agent (`research_agent.py`):** Collects publications, conferences, patents, and funded research grants.
2. **Teaching-Learning Data Collection Agent (`teaching_agent.py`):** Analyzes course loads, student evaluations, monthly attendance, and pass rates.
3. **Administrative Data Collection Agent (`administration_agent.py`):** Gathers committee memberships, coordinator roles, and institutional event responsibilities.
4. **Evidence Validation Agent (`validation_agent.py`):** Checks evidence completeness, verifies file integrity, detects duplicates, and assigns `VALID`, `INVALID`, or `NEEDS_REVIEW`.
5. **API Calculation Agent (`api_calculation_agent.py`):** Deterministically calculates appraisal scores from strictly `VALID` evidence using `config/scoring_rules.json`. *(Note: "API" refers to faculty appraisal scoring, not REST APIs).*
6. **Report Generation Agent (`report_agent.py`):** Generates formal PDF and JSON draft appraisal documents marked *"Awaiting Human Review"*.

### Coordinator (Infrastructure Orchestrator)
The **Coordinator (`coordinator.py`)** is orchestration infrastructure (not counted among the 6 domain agents). It executes Research, Teaching, and Administration data collection in parallel threads, pipelines results through Validation, Scoring, and Reporting, tracks execution duration, and records the overall run state.

---

## 3. Technology Stack

- **Language:** Python 3.10+
- **Agent Runtime:** OpenCLA/OpenClaw-style registry architecture
- **Connector:** Model Context Protocol (MCP) educational server pattern
- **Backend API:** FastAPI & Uvicorn
- **Dashboard UI:** Streamlit
- **Persistence & Audit:** SQLite (normalized relational schema & key-value memory)
- **Document Generation:** `fpdf2` (PDF) and Python `json`
- **Data Parsing:** `pandas` and standard `csv`
- **Test Framework:** `pytest` (31 tests)

---

## 4. Installation & Quickstart

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Seed Database with Synthetic Demo Data
```bash
python run.py seed
```

### 3. Launch Streamlit Dashboard
```bash
python run.py dashboard
```
*Access the interactive interface at `http://localhost:8501`.*

### 4. Run FastAPI Backend
```bash
python run.py api
```
*Access REST API docs at `http://127.0.0.1:8000/docs`.*

---

## 5. Running Concept Demonstrations & Tests

```bash
# Run pytest automated test suite (31 tests across Labs 1-12)
python run.py test

# Demo Lab 7: Agentic Node Graph
python run.py graph

# Demo Lab 8: Swarm Consensus Resolution
python run.py swarm

# Demo Lab 9: Deep Research & Citation Truth Table
python run.py research

# Demo Lab 10: Cloud Operations Agent & Telemetry
python run.py cloud

# Demo Lab 11: Agentic SDLC Delivery Factory
python run.py sdlc

# Demo Lab 12: Responsible Autonomy & Audit Hash Chain
python run.py governance
```

---

## 6. Contributors

- **Pratiksha Magadum** (USN: `02FE23BCI045`)  
- **Department of Computer Science and Engineering**  
- **KLE Technological University, Dr. M. S. Sheshagiri Campus, Belagavi**  
- **Academic Year:** 2026–27
