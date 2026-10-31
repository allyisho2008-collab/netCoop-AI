class ConnectivityAgent:
    def analyze(self, data):
        topo = data.get("topology", {})
        ev = []
        if topo.get("link_status")=="degraded": ev.append({"metric":"link_status","value":"degraded","interpretation":"Link degraded"})
        return {"agent":"connectivity_agent","issues_detected":["connectivity_degradation"] if ev else [],"evidence":ev,"affected_devices":topo.get("affected_devices",[]),"confidence":0.8}
