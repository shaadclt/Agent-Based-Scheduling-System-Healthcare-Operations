import asyncio
from app.agent import create_agent


async def run_agent(user_input: str):
    agent, tracer = create_agent("data/doctors.json")
    result = await agent.run(user_input)
    tracer.pretty_print()
    return result


if __name__ == "__main__":
    output = asyncio.run(
        run_agent("Find a neurologist and schedule an appointment")
    )
    print("FINAL OUTPUT:\n", output)
