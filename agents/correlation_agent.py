class CorrelationAgent:
    def correlate(self, findings):
        issues, ev = [], []
        for f in findings:
            issues.extend(f.get("issues_detected",[])); ev.extend(f.get("evidence",[]))
        if "link_congestion" in issues and "queue_congestion" in issues:
            rc, conf = "Likely link congestion causing egress queue drops", 0.87
        elif "device_overload" in issues:
            rc, conf = "Device CPU overload causing degradation", 0.82
        else:
            rc, conf = "Insufficient evidence", 0.35
        return {"probable_root_cause":rc,"alternative_causes":list(set(issues)),"aggregated_evidence":ev,"confidence":conf}
