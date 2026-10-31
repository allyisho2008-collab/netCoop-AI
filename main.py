from agents.telemetry_agent import TelemetryAgent
from agents.infrastructure_agent import InfrastructureAgent
from agents.connectivity_agent import ConnectivityAgent
from agents.correlation_agent import CorrelationAgent
from agents.reporting_agent import ReportingAgent
import json

SAMPLE_INPUT = {
  "incident_id": "INC_0012",
  "timestamp": "2026-10-31T18:00:00Z",
  "device_id": "HOSTEL_CORE_SW_01",
  "metrics": {"latency_ms": 185, "jitter_ms": 25, "packet_loss_pct": 4.2, "throughput_mbps": 45, "bandwidth_mbps": 100, "link_utilization_pct": 96, "cpu_utilization_pct": 88, "memory_utilization_pct": 75, "egress_queue_drops": 1245, "interface_errors": 12},
  "topology": {"affected_devices": ["HOSTEL_CORE_SW_01", "HOSTEL_AP_12"], "link_status": "degraded"}
}

def run_diagnosis(data):
    print("=== NetCoop AI Started ===\n")
    tel = TelemetryAgent().analyze(data)
    infra = InfrastructureAgent().analyze(data)
    conn = ConnectivityAgent().analyze(data)
    corr = CorrelationAgent().correlate([tel, infra, conn])
    report = ReportingAgent().generate_report(data["incident_id"], [tel, infra, conn], corr)
    print(json.dumps(report, indent=2))
    with open("final_report.json", "w") as f: json.dump(report, f, indent=2)
    print("\nSaved to final_report.json")
    return report

if __name__ == "__main__":
    run_diagnosis(SAMPLE_INPUT)
