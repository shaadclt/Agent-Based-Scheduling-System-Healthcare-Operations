from time import time
from typing import Optional

from llama_index.utils.workflow import Workflow, Event
from llama_index.core.llms import ChatMessage

from app.memory import ConversationMemory
from app.tools import (
    search_doctors_tool,
    schedule_appointment_tool,
)
from app.traces import AgentTraceLogger
from app.evaluation import AgentEvaluator


# =========================
# Workflow Events
# =========================

class PrepEvent(Event):
    """Prepare and normalize input before LLM reasoning"""
    pass


class InputEvent(Event):
    """Structured input passed to the LLM"""
    pass


class ToolCallEvent(Event):
    """Represents a tool execution decision"""
    pass


class StopEvent(Event):
    """Deterministic termination event"""
    pass


# =========================
# Scheduling Workflow
# =========================

class SchedulingWorkflow(Workflow):
    """
    Event-driven scheduling agent using ReAct-style reasoning.
    Includes structured traces and evaluation metrics.
    """

    def __init__(
        self,
        memory: ConversationMemory,
        index,
        tracer: AgentTraceLogger,
        evaluator: Optional[AgentEvaluator] = None,
    ):
        super().__init__()
        self.memory = memory
