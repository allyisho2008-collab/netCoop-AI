class InfrastructureAgent:
    def analyze(self, data):
        m = data.get("metrics", {})
        ev, iss = [], []
        if m.get("cpu_utilization_pct",0) > 80:
            ev.append({"metric":"cpu_utilization_pct","value":m["cpu_utilization_pct"],"interpretation":"High CPU"}); iss.append("device_overload")
        if m.get("interface_errors",0) > 5:
            ev.append({"metric":"interface_errors","value":m["interface_errors"],"interpretation":"Interface errors"}); iss.append("ethernet_fault")
        return {"agent":"infrastructure_agent","issues_detected":iss,"evidence":ev,"confidence":0.85 if iss else 0.3}
