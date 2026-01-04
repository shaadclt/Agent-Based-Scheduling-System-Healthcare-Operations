from app.config import setup_models
from app.memory import ConversationMemory
from app.tools import build_doctor_index
from app.workflow import SchedulingWorkflow
from app.traces import AgentTraceLogger


def create_agent(data_path: str):
    setup_models()

    memory = ConversationMemory()
    tracer = AgentTraceLogger()
    index = build_doctor_index(data_path)

    workflow = SchedulingWorkflow(
        memory=memory,
        index=index,
        tracer=tracer
    )

    return workflow, tracer
