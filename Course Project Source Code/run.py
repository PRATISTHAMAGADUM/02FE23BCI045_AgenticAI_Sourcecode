"""
Unified Launcher for Faculty Appraisal Management System
Allows launching Streamlit dashboard, FastAPI backend, running tests,
or executing demonstrations for Core Concepts 7 through 12.

Usage:
  python run.py dashboard    # Launch Streamlit Dashboard
  python run.py api          # Launch FastAPI server
  python run.py test         # Run pytest test suite (31 tests)
  python run.py seed         # Re-seed SQLite database with demo data
  python run.py graph        # Demo Lab 7: Node Graph Execution & State Machine
  python run.py swarm        # Demo Lab 8: Parallel Swarm & Consensus Conflict Resolution
  python run.py research     # Demo Lab 9: Deep Research & Citation Cross-Referencing
  python run.py cloud        # Demo Lab 10: Cloud Operations Agent & Telemetry
  python run.py sdlc         # Demo Lab 11: Agentic SDLC Factory & Policy Verification
  python run.py governance   # Demo Lab 12: Responsible Autonomy, Audit Chain & Rollback
"""
import sys
import os
import subprocess


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("Defaulting to launching Streamlit Dashboard...")
        target = "dashboard"
    else:
        target = sys.argv[1].lower()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, base_dir)

    if target == "dashboard":
        streamlit_app = os.path.join(base_dir, "dashboard", "streamlit_app.py")
        print(f"Starting Streamlit dashboard on http://localhost:8501 ...")
        subprocess.run([sys.executable, "-m", "streamlit", "run", streamlit_app])

    elif target == "api":
        print("Starting FastAPI backend on http://127.0.0.1:8000 ...")
        subprocess.run([sys.executable, "-m", "uvicorn", "app.api.main:app", "--reload", "--port", "8000"])

    elif target == "test":
        print("Running pytest test suite (31 tests across Labs 1-12)...")
        subprocess.run([sys.executable, "-m", "pytest", "-v"])

    elif target == "seed":
        print("Re-seeding database with synthetic demo data...")
        seed_script = os.path.join(base_dir, "app", "database", "seed.py")
        subprocess.run([sys.executable, seed_script])

    elif target == "graph":
        from app.graph.appraisal_graph import create_appraisal_node_graph
        print("\n=== DEMO LAB 7: AGENTIC NODE GRAPH EXECUTION ===")
        g = create_appraisal_node_graph()
        print("Mermaid Structure:")
        print(g.to_mermaid())
        print("\nExecuting DAG Workflow for FAC001 (auto-advance gate)...")
        res = g.run({"faculty_id": "FAC001", "auto_advance_human_gate": True})
        print(f"Graph Status: {res['graph_status']} | Total Steps: {res['total_steps']}")
        print(f"Computed API Score: {res.get('total_score')} / 100")
        print(f"Final Artifact: {res.get('pdf_path')}")

    elif target == "swarm":
        from app.swarm.swarm import AppraisalSwarm
        from app.agents.coordinator import AppraisalCoordinator
        print("\n=== DEMO LAB 8: PARALLEL SWARMS & CONSENSUS RESOLUTION ===")
        coord = AppraisalCoordinator()
        print("Collecting domain evidence...")
        pipe_res = coord.run_appraisal_pipeline("FAC001")
        swarm = AppraisalSwarm()
        print("Executing 4-Peer Swarm Collaboration on Message Board...")
        swarm_res = swarm.run_swarm(pipe_res)
        print(f"Swarm Status: {swarm_res['status']}")
        print(f"Consensus Scores: {swarm_res['consensus_scores']}")
        print(f"Conflicts Resolved: {len(swarm_res['conflicts_resolved'])}")
        print(f"Total Peer Messages Exchanged: {len(swarm_res['message_board_trace'])}")

    elif target == "research":
        from app.research.deep_research import DeepResearchAgent
        print("\n=== DEMO LAB 9: DEEP RESEARCH & CITATION CROSS-REFERENCING ===")
        dra = DeepResearchAgent()
        print("Running 5-Phase Research Loop (Question -> Search -> Extract -> Compare -> Synthesize)...")
        res = dra.run_research_loop("FAC001")
        print(f"Research Integrity Quotient: {res['research_integrity_quotient']}%")
        print(f"Bibliometric Summary: {res['bibliometric_summary']}")
        print(f"Verified Papers Matrix: {len(res['evidence_verification_matrix'])} items")

    elif target == "cloud":
        from app.cloud.cloud_agent import CloudOperationsAgent
        print("\n=== DEMO LAB 10: CLOUD OPERATIONS & TELEMETRY AGENT ===")
        ca = CloudOperationsAgent()
        signals = ca.observe_signals()
        print(f"Observed {len(signals)} Infrastructure Signals:")
        for s in signals:
            print(f"  [{s.status}] {s.name}: {s.value} {s.unit} ({s.message})")
        plan = ca.diagnose_and_plan(signals)
        print(f"\nDiagnostic Plan: {plan.diagnosis}")
        print(f"Proposed Remediation Actions: {len(plan.actions)}")
        for a in plan.actions:
            print(f"  - {a.action_type} (Risk: {a.risk_level}, Approval Required: {a.requires_approval})")

    elif target == "sdlc":
        from app.sdlc.sdlc_factory import AgenticSDLCFactory
        print("\n=== DEMO LAB 11: AGENTIC SDLC FACTORY ===")
        factory = AgenticSDLCFactory()
        req = "Add NBA Criterion 5.2 patent commercialization weighting"
        print(f"Intake Requirement: '{req}'")
        dossier = factory.process_requirement(req)
        print(f"Release ID: {dossier.release_id} | Status: {dossier.status}")
        print(f"Verification Tests Passed: {dossier.test_results['all_tests_passed']}")
        print("Human Lead Signing off release...")
        rel = factory.approve_release(dossier.release_id, "Prof. Lead Architect")
        print(f"Result: {rel['status']} - {rel['message']}")

    elif target == "governance":
        from app.governance.responsible_autonomy import ResponsibleAutonomyEngine
        print("\n=== DEMO LAB 12: RESPONSIBLE AUTONOMY & GOVERNANCE ===")
        gov = ResponsibleAutonomyEngine()
        gov.append_audit_block("APPRAISAL_CALCULATED", "RUN-DEMO", {"faculty_id": "FAC001", "score": 94.0})
        gov.append_audit_block("HUMAN_APPROVED", "RUN-DEMO", {"approved_by": "Dean of Engineering"})
        valid, msg = gov.verify_audit_chain()
        print(f"Cryptographic Hash Chain: {msg}")
        fairness = gov.evaluate_fairness()
        print(f"Demographic Parity: {fairness.demographic_parity_status} (Disparate Impact: {fairness.disparate_impact_ratio})")
        masked = gov.sanitize_pii("Contact Dr. Rao at ananya@kletech.ac.in or call 9876543210.")
        print(f"PII Privacy Sanitization: {masked}")

    else:
        print(f"Unknown target: '{target}'. Options: dashboard, api, test, seed, graph, swarm, research, cloud, sdlc, governance")


if __name__ == "__main__":
    main()
