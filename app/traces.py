from datetime import datetime
from typing import List, Dict


class AgentTraceLogger:
    def __init__(self):
        self.traces: List[Dict] = []

    def log(self, step: str, detail: str):
        self.traces.append({
            "timestamp": datetime.utcnow().isoformat(),
            "step": step,
            "detail": detail,
        })

    def get_traces(self) -> List[Dict]:
        return self.traces

    def pretty_print(self):
        print("\n=== AGENT TRACE ===")
        for t in self.traces:
            print(f"[{t['timestamp']}] {t['step']}: {t['detail']}")
        print("===================\n")
