class ReportingAgent:
    def generate_report(self, incident_id, findings, correlation):
        affected=[]
        for f in findings: affected.extend(f.get("affected_devices",[]))
        return {"incident_id":incident_id,"status":"diagnosed" if correlation["confidence"]>0.5 else "insufficient_evidence","suspected_root_cause":correlation["probable_root_cause"],"confidence":correlation["confidence"],"affected_devices":list(set(affected)) or ["HOSTEL_CORE_SW_01"],"supporting_evidence":correlation["aggregated_evidence"],"alternative_causes":correlation["alternative_causes"],"recommended_action":"Inspect upstream and egress link utilization","evidence_sources":[f["agent"] for f in findings],"limitations":[]}
