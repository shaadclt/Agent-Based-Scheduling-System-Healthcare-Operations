from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import create_agent

app = FastAPI(
    title="Agent-Based Scheduling System",
    description="API for an event-driven scheduling agent using LlamaIndex and ReAct",
    version="1.0.0"
)


class AgentRequest(BaseModel):
    query: str


class AgentResponse(BaseModel):
    output: str
    traces: list


@app.post("/run", response_model=AgentResponse)
async def run_agent(request: AgentRequest):
    agent, tracer = create_agent("data/doctors.json")
    result = await agent.run(request.query)

    return {
        "output": result,
        "traces": tracer.get_traces()
    }
