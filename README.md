# Agentic AI Systems — Lab Assignments & Course Project Repository

**Student Name:** Pratiksha Magadum  
**USN:** 02FE23BCI045  
**GitHub Profile:** [PRATISTHAMAGADUM](https://github.com/PRATISTHAMAGADUM)  
**Repository:** [https://github.com/PRATISTHAMAGADUM/02FE23BCI045_AgenticAI_Sourcecode](https://github.com/PRATISTHAMAGADUM/02FE23BCI045_AgenticAI_Sourcecode)  
**Course:** Agentic AI Systems (School of Computer Science & Engineering, KLE Technological University)  

---
Faculty Appraisal Management System – Agentic AI Multi-Agent System

A Python-based, autonomous multi-agent implementation exploring practical Agentic AI concepts (Labs 1 through 12) applied to academic performance evaluation. The system automates faculty evidence collection, multi-source validation, deterministic scoring, and human-in-the-loop appraisal report synthesis.

The project is structured as a modular, production-grade workbench combining specialized domain agents, an OpenCLA-style execution runtime, educational Model Context Protocol (MCP) connectors, stateful node graphs, decentralized peer swarms, deep bibliometric research, cloud telemetry, an agentic SDLC factory, and cryptographic governance.

Overview

This system automates the preparation, verification, and audit of annual faculty appraisal dossiers. Reviewing academic performance manually across scholarship, pedagogy, and institutional administration is time-consuming, prone to inconsistent scoring, and vulnerable to missed or duplicate records.

The workbench integrates 12 core Agentic AI architectural concepts into a cohesive educational application:

Domain agents operate proactively across parallel threads to ingest faculty records from files and relational databases.
An independent validation agent filters corrupted or unverified records before deterministic scoring rules are applied.
Advanced agentic patterns—such as DAG workflow orchestration, peer-reviewed swarm consensus, bibliometric citation truth verification, telemetry-driven self-healing, automated SDLC delivery, and SHA-256 rolling audit chains—ensure system reliability, transparency, and safety.
The system includes a central CLI runner (run.py), an interactive Streamlit dashboard (12 views), and a FastAPI backend.

All faculty records used in the repository are synthetic demo records, and the appraisal scoring policy serves as a configurable educational reference.

Technology Stack
Category	Technologies
Programming Language	Python 3.10+
Agent Architecture	OpenCLA / OpenClaw-Style Generic Runtime, Multi-Agent Collaboration
Agent Protocol & Connectors	Model Context Protocol (MCP) Educational Server & Client Pattern
Workflow & State Orchestration	Directed Acyclic Graph (DAG), StateGraph, Checkpoint & Resume Engine
User Interfaces & APIs	Streamlit (Interactive Multi-Tab Dashboard), FastAPI, Uvicorn
Data Storage & Persistence	SQLite (Relational Schema & Faculty-Scoped Key-Value Memory), JSON
Data Processing & Parsing	Pandas, Regular Expressions (Regex PII Redactor), CSV, AST
Concurrency & Swarms	Python ThreadPoolExecutor, Shared MessageBoard Multi-Round Consensus
Document Generation	fpdf2 (Formal PDF Appraisal Dossiers), Python JSON Engine
Testing & Quality Assurance	Pytest (31 Automated Unit & Integration Tests)
Safety, Audit & Governance	Cryptographic SHA-256 Rolling Hash Chain, State Rollback Engine, EEOC Four-Fifths Parity Evaluator
Lab Modules & Core Concept Mapping

The project implements and maps the 12 Core Agentic AI Concepts:

Lab	Module	Key Implementation in This Project
01	Agent vs Chatbot	6 autonomous domain agents (Research, Teaching, Administration, Validation, Scoring, Report) executing proactive PLAN ➔ ACT ➔ OBSERVE ➔ DECIDE cycles with explicit anomaly handling.
02	Tool-Using Agent	12 atomic execution tools spanning CSV parsing, SQLite relational queries, deterministic arithmetic calculations, and PDF/JSON generation managed via a centralized ToolRegistry.
03	Reusable Skills	6 high-level domain skills governed by individual SKILL.md specifications and code classes loaded through dynamic SKILL_REGISTRY.
04	Agent Memory & Retrieval	Persistent, user-scoped memory backed by SQLite (faculty:FAC001) preventing cross-faculty context leakage and enabling multi-session historical analysis without vector hallucinations.
05	Agent Connectors (MCP)	Educational Model Context Protocol (MCP) Server exposing a discoverable CAPABILITIES manifest, client caller whitelisting, directory traversal guards, and SELECT-only SQL enforcement.
06	Agent Runtime (OpenCLA)	Domain-agnostic execution runtime (receive_task(), dynamic select_skill(), structured audit logging, failure recovery) extensible without altering the runtime core.
07	Agentic Node Graph	Explicit Directed Acyclic Graph (StateGraph) with parallel collection branches, conditional evidence-quality routing, and checkpointed HumanGateNode state persistence.
08	Parallel Specialist Swarms	Decentralized 4-peer agent collaboration (ResearchPeer, PedagogyPeer, GovernancePeer, QAPeer) exchanging proposals and critiques over a shared MessageBoard with automated consensus resolution.
09	Deep Research Agent	Autonomous 5-phase research loop (Question ➔ Search ➔ Extract ➔ Compare ➔ Synthesize), bibliometric cross-referencing (Scopus/WoS), Citation Truth Table, and Research Integrity Quotient.
10	Cloud Operations Agent	Live infrastructure telemetry signal probing (latency, storage, error rate), root-cause diagnostics, and risk-tiered self-healing remediation plans guarded by human approval gates.
11	Agentic SDLC Factory	Autonomous software delivery factory: policy requirement intake, formal specification synthesis, code diff generation, automated test synthesis, regression runner, and human release sign-off.
12	Safety, Evaluation & Governance	Tamper-evident SHA-256 rolling hash audit chain, state snapshot & rollback engine, EEOC Four-Fifths demographic parity evaluator, and automated regex PII masking.
Key Implementation Details
1. Multi-Agent Domain Architecture

Six specialized domain agents operate under the coordination of the Appraisal Coordinator:

Research Data Collection Agent: Ingests publications, conference papers, patents, and sponsored grants.
Teaching-Learning Data Collection Agent: Ingests teaching loads, student feedback, attendance, and pass rates.
Administrative Data Collection Agent: Extracts committee appointments, coordinator roles, and institutional service.
Evidence Validation Agent: Performs independent checks for file existence, data completeness, and duplicates, classifying evidence as VALID, INVALID, or NEEDS_REVIEW.
API Calculation Agent: Applies deterministic scoring rules exclusively to VALID records using config/scoring_rules.json.
Report Generation Agent: Formats formal appraisal reports marked "Awaiting Human Review".
2. Tool and Skill Registry Separation
Tools (Lab 2): Low-level execution primitives (read_csv, query_faculty_data, calculate_weighted_score, export_pdf_report) registered in ToolRegistry.
Skills (Lab 3): High-level capability packages adhering to a strict SKILL.md specification and registered dynamically in SKILL_REGISTRY.
3. Persistent Scoped Memory

Backed by SQLite, the key-value memory store is scoped strictly per faculty identifier (e.g., faculty:FAC001). This eliminates the risk of cross-faculty data leakage and avoids non-deterministic vector database retrieval errors for sensitive numerical appraisal scoring.

4. MCP Security & Connector Protocol

An educational Model Context Protocol (MCP) client-server architecture enforces access boundaries:

Dynamic capability discovery via standard manifest.
Enforcement of SELECT-only SQL queries (blocking malicious or accidental UPDATE/DELETE/DROP statements).
Directory path traversal checks restricting file access strictly to authorized faculty directories.
5. Graph-Based Workflow Orchestration

A stateful DAG engine (StateGraph) compiles and executes the appraisal workflow:

Forks parallel data extraction across multiple branches.
Uses conditional edge evaluations to route clean submissions directly to scoring while flagging anomalous submissions for manual triage.
Enforces an interruptible HumanGateNode that halts pipeline execution, saves state checkpoints (CKPT-*), and resumes only upon human evaluator approval.
6. Decentralized Swarm Consensus

Four peer agents evaluate faculty dossiers from distinct perspectives without a centralized coordinator:

ResearchPeerAgent: Evaluates scholarship depth and publication metrics.
PedagogyPeerAgent: Assesses teaching consistency and student feedback.
GovernancePeerAgent: Evaluates compliance and administrative duties.
QualityAssurancePeerAgent: Checks data validity and penalty deductions. The swarm posts multi-round proposals and critiques to a shared MessageBoard, resolving score discrepancies into a unified consensus appraisal dossier.
7. Deep Research & Bibliometric Truth Verification

An autonomous 5-phase research agent verifies claimed publication metrics:

Cross-references claimed citations against indexed bibliometric sources (Scopus, Web of Science, IEEE, ACM).
Flags citation inflation and unindexed journal claims.
Calculates an overall Research Integrity Quotient (RIQ).
8. Cloud Telemetry & Risk-Gated Remediation

Monitors host storage, audit error rates, and pipeline latency:

Automatically diagnoses infrastructure degradation.
Separates remediation into LOW risk (automated safe cache/report pruning) and HIGH risk (database VACUUM compaction, worker resets), requiring administrator approval before execution.
9. Agentic SDLC Delivery Factory

Translates high-level accreditation requirements (e.g., NBA/NAAC scoring updates) into production code updates:

Synthesizes specifications and code diffs for scoring_rules.json.
Automatically generates boundary and regression unit tests.
Executes tests in a sandboxed runner and produces an SDLCReleaseDossier ready for lead architect approval.
10. Responsible Autonomy & Cryptographic Governance
Cryptographic Hash Chain: Every audit event links to the preceding block using SHA-256 hashes (previous_hash + timestamp + payload), providing immediate detection of any unauthorized database modification.
State Rollback Engine: Creates point-in-time state snapshots, allowing disputed evaluations to be rolled back safely.
EEOC Four-Fifths Parity: Evaluates appraisal score distributions across departments to detect disparate impact.
PII Masking: Sanitizes email addresses, phone numbers, and confidential medical identifiers prior to report export.
Project Structure
text
faculty-appraisal-agentic-ai/
│
├── app/
│   ├── agents/                   # Lab 1: 6 Domain Agents + Coordinator
│   │   ├── base_agent.py
│   │   ├── research_agent.py
│   │   ├── teaching_agent.py
│   │   ├── administration_agent.py
│   │   ├── validation_agent.py
│   │   ├── api_calculation_agent.py
│   │   ├── report_agent.py
│   │   └── coordinator.py
│   │
│   ├── tools/                    # Lab 2: 12 Atomic Tools
│   │   ├── file_tools.py
│   │   ├── database_tools.py
│   │   ├── calculation_tools.py
│   │   └── report_tools.py
│   │
│   ├── skills/                   # Lab 3: 6 Reusable Skills + SKILL.md specs
│   │   ├── base_skill.py
│   │   ├── research_appraisal/
│   │   ├── teaching_appraisal/
│   │   ├── administration_appraisal/
│   │   ├── evidence_validation/
│   │   ├── api_calculation/
│   │   └── report_generation/
│   │
│   ├── runtime/                  # Lab 4 & 6: OpenCLA Runtime & Scoped Memory
│   │   ├── runtime.py
│   │   ├── skill_registry.py
│   │   ├── tool_registry.py
│   │   ├── memory.py
│   │   └── audit.py
│   │
│   ├── mcp/                      # Lab 5: Educational MCP Server & Client
│   │   ├── server.py
│   │   ├── client.py
│   │   ├── capabilities.py
│   │   └── security.py
│   │
│   ├── graph/                    # Lab 7: StateGraph DAG & Human Gate
│   │   ├── engine.py
│   │   └── appraisal_graph.py
│   │
│   ├── swarm/                    # Lab 8: Parallel Swarm & Message Board
│   │   ├── swarm.py
│   │   ├── peers.py
│   │   └── message_board.py
│   │
│   ├── research/                 # Lab 9: Deep Research & Bibliometrics
│   │   └── deep_research.py
│   │
│   ├── cloud/                    # Lab 10: Telemetry & Cloud Operations
│   │   └── cloud_agent.py
│   │
│   ├── sdlc/                     # Lab 11: Agentic SDLC Delivery Factory
│   │   └── sdlc_factory.py
│   │
│   ├── governance/               # Lab 12: Audit Hash Chain & Safety Engine
│   │   └── responsible_autonomy.py
│   │
│   ├── database/                 # SQLite Database Schema & Seed Data
│   │   ├── schema.sql
│   │   ├── database.py
│   │   └── seed.py
│   │
│   └── api/                      # FastAPI Backend Endpoints
│       └── main.py
│
├── dashboard/                    # Streamlit Interactive Dashboard (12 Tabs)
│   └── streamlit_app.py
│
├── config/                       # Scoring Weights & Evaluation Policy
│   └── scoring_rules.json
│
├── data/                         # Synthetic Faculty Records (FAC001)
│   └── faculty/
│
├── reports/                      # Generated PDF & JSON Appraisal Reports
│
├── tests/                        # Automated Pytest Suite (31 Tests)
│   ├── test_agents.py
│   ├── test_tools.py
│   ├── test_skills.py
│   ├── test_memory.py
│   ├── test_mcp.py
│   ├── test_runtime.py
│   ├── test_scoring.py
│   └── test_concepts_7_to_12.py
│
├── docs/                         # Lab Manuals & Viva Preparation
│   ├── architecture.md
│   ├── lab1.md to lab12.md
│   ├── demo-script.md
│   └── viva.md
│
├── requirements.txt              # Project Dependencies
├── run.py                        # Unified Command-Line Runner
└── README.md                     # Comprehensive Project Documentation
Installation and Setup
Prerequisites
Python 3.10 or later
pip (Python package installer)
Git
1. Clone the Repository
bash
git clone https://github.com/<your-username>/faculty-appraisal-agentic-ai.git
2. Navigate to the Project Directory
bash
cd faculty-appraisal-agentic-ai/faculty-appraisal-agentic-ai
3. Create and Activate a Virtual Environment

Windows (PowerShell):

powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

Linux / macOS:

bash
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
bash
pip install -r requirements.txt
5. Seed the Database

Populate the SQLite database with synthetic faculty data for testing:

bash
python run.py seed
Running the Application & Demos

The project includes a unified CLI runner (run.py) to launch applications and execute specific lab concept demonstrations.

Interactive User Interfaces
Launch the Streamlit Dashboard (Primary Interface)
bash
python run.py dashboard

Access the dashboard in your browser at http://localhost:8501 to view all 12 interactive lab tabs.

Launch the FastAPI REST Server
bash
python run.py api

Access interactive Swagger documentation at http://127.0.0.1:8000/docs.

Executing Individual Lab Demonstrations

You can execute standalone concept demonstrations directly from the CLI:

bash
# Demo Lab 7: Agentic Node Graph & Human Gate
python run.py graph
# Demo Lab 8: Parallel Swarm & Decentralized Consensus
python run.py swarm
# Demo Lab 9: Deep Research & Citation Truth Matrix
python run.py research
# Demo Lab 10: Cloud Operations & Telemetry Remediation
python run.py cloud
# Demo Lab 11: Agentic SDLC Delivery Factory
python run.py sdlc
# Demo Lab 12: Responsible Autonomy, Audit Hash Chain & PII Masking
python run.py governance
Testing

The workbench includes an automated test suite comprising 31 unit and integration tests covering all 12 core concepts.

To run the full test suite via run.py:

bash
python run.py test

Or run directly with pytest:

bash
python -m pytest -v
Test Coverage Highlights:
Agents & Pipeline (test_agents.py): Multi-agent collection and end-to-end pipeline execution.
Tools (test_tools.py): Atomic file parsing, math scoring, and directory containment.
Memory (test_memory.py): Isolation of scoped faculty records without cross-contamination.
MCP Security (test_mcp.py): Capability discovery, SELECT-only SQL enforcement, and path traversal rejection.
Runtime (test_runtime.py): OpenCLA runtime task processing and dynamic skill registration.
Scoring (test_scoring.py): Bounds validation and capping logic verification.
Concepts 7 to 12 (test_concepts_7_to_12.py): Node graph checkpoints, 4-peer swarm consensus, 5-phase deep research loop, cloud risk gates, SDLC diff synthesis, SHA-256 rolling audit chains, and PII masking.
Implementation Scope & Academic Boundaries

This project serves as an educational and practical implementation of agentic AI principles. Key architectural boundaries include:

Synthetic Data: All faculty records, publication entries, attendance sheets, and student evaluations are synthetic demo datasets.
Deterministic Appraisal Scoring: Scoring rules are driven by config/scoring_rules.json and evaluated deterministically rather than generated via LLM inference to prevent hallucinations.
Internal MCP-Style Protocol: The connector layer implements an educational Model Context Protocol pattern rather than relying on external remote MCP transports.
Local Bibliometric Corpus: Lab 9 deep research cross-references claims against local bibliometric indexes rather than querying live paywalled scientific databases.
Simulated Telemetry Signals: Lab 10 cloud operations monitors local process telemetry (latency, database size, error logs) rather than mutating public cloud infrastructure.
Human-in-the-Loop Governance: AI generated appraisals remain in a DRAFT state until an authorized human evaluator formally reviews and approves the dossier.
Contributors

Developed as an academic project for the Agentic AI Course:

Pratiksha K. (and Team Members)
Department of Computer Science and Engineering
KLE Technological University, Dr. M. S. Sheshagiri Campus, Belagavi

Academic Year: 2026–27
