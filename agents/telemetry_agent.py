class TelemetryAgent:
    def analyze(self, data):
        m = data.get("metrics", {})
        ev, iss = [], []
        if m.get("link_utilization_pct",0) > 85:
            ev.append({"metric":"link_utilization_pct","value":m["link_utilization_pct"],"interpretation":"High link utilization"}); iss.append("link_congestion")
        if m.get("egress_queue_drops",0) > 100:
            ev.append({"metric":"queue_drops","value":m["egress_queue_drops"],"interpretation":"Elevated packet drops"}); iss.append("queue_congestion")
        if m.get("latency_ms",0) > 100:
            ev.append({"metric":"latency_ms","value":m["latency_ms"],"interpretation":"Elevated latency"})
        return {"agent":"telemetry_agent","issues_detected":iss,"evidence":ev,"confidence":0.9 if iss else 0.2}
