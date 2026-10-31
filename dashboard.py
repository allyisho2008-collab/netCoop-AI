import streamlit as st, json, os
st.set_page_config(page_title="NetCoop AI", layout="wide")
st.title("🌐 NetCoop AI - Multi-Agent Network Diagnosis")
st.sidebar.header("Run Diagnosis")
if st.sidebar.button("Run Diagnosis", type="primary"):
    import main
    report = main.run_diagnosis(main.SAMPLE_INPUT)
    st.session_state['report']=report

if os.path.exists("final_report.json"):
    with open("final_report.json") as f: r=json.load(f)
    c1,c2,c3=st.columns(3)
    c1.metric("Incident", r['incident_id'])
    c2.metric("Confidence", f"{r['confidence']*100:.1f}%")
    c3.metric("Status", r['status'])
    st.subheader(f"Root Cause: {r['suspected_root_cause']}")
    st.json(r)
    st.subheader("Agent Collaboration")
    st.write("Evidence Sources:", ", ".join(r['evidence_sources']))
    for ev in r['supporting_evidence']:
        st.warning(f"{ev['metric']}: {ev['value']} - {ev['interpretation']}")
else:
    st.info("Click Run Diagnosis")

cat > README.md << 'MD'
# NetCoop AI - Multi-Agent Network Fault Diagnosis

IIT Bhubaneswar network diagnosis using collaborating AI agents.

## Architecture
- telemetry_agent: latency, packet loss, link utilization
- infrastructure_agent: CPU, memory, errors
- connectivity_agent: topology, affected devices
- correlation_agent: correlates evidence, root cause
- reporting_agent: final JSON report

## Run
## Test Cases
- link_congestion: high utilization + queue drops
- device_overload: high CPU
- normal: all OK

## Final Report Format
Matches hackathon spec with confidence scoring and evidence.
MD

cat > requirements.txt << 'REQ'
streamlit
REQ

ls -R
