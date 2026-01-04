# Agent-Based Scheduling System for Healthcare Operations 🏥

An agent-based scheduling system that uses LlamaIndex workflows and the ReAct pattern to automate doctor discovery and appointment coordination through structured reasoning and tool execution.

## Overview

This project implements a conversational AI agent that helps patients:
- Search for doctors by disease/specialty
- View doctor information (experience, contact details)
- Schedule appointments with selected doctors
- Maintain conversation context across multiple interactions

## Why This Project

Manual scheduling in healthcare and service-based industries is time-consuming,error-prone, and difficult to scale. This project demonstrates how agent-basedsystems can automate scheduling workflows by combining semantic search, reasoning, and tool execution in a controlled pipeline.

## Features

- **Semantic Search**: Uses vector embeddings to search doctors by specialty or disease
- **Automated Scheduling**: Books appointments with selected doctors
- **ReAct Agent Pattern**: Employs reasoning and action steps for intelligent decision-making
- **Memory Management**: Maintains conversation history for contextual responses
- **Tool Integration**: Combines multiple tools (search + scheduling) seamlessly

## Architecture

The system uses LlamaIndex workflows with three main events:
1. **PrepEvent**: Prepares the request for processing
2. **InputEvent**: Formats input for the LLM
3. **ToolCallEvent**: Triggers appropriate tool calls

```
User Input → PrepEvent → InputEvent → LLM Processing → ToolCallEvent → Response
                ↑                                              ↓
                └──────────────────────────────────────────────┘
```

### Agent Workflow

The scheduling agent follows an event-driven workflow using LlamaIndex
workflows and the ReAct (Reasoning + Acting) pattern.

- User input enters through a StartEvent and is normalized in a PrepEvent
- Conversation history is reconstructed to maintain multi-turn context
- The LLM reasons over the structured input and decides whether to:
  - respond directly, or
  - invoke scheduling/search tools
- Tool results are fed back into the workflow, enabling iterative reasoning
- The process terminates deterministically via a StopEvent

This design ensures controlled tool usage, clear reasoning boundaries,
and safe agent execution.

<img width="1849" height="866" alt="Scheduling agent workflow" src="https://github.com/user-attachments/assets/0cdc2308-5c07-4a79-9d9f-a48ba9920ff9" />

## Prerequisites

- Python 3.8+
- Google Colab (recommended) or Jupyter Notebook
- Groq API Key
- Required Python packages (see Installation)

## Installation

```bash
# Install required packages
pip install llama-index
pip install llama-index-llms-groq
pip install llama-index-embeddings-huggingface
pip install llama-index-readers-json
pip install llama-index-utils-workflow
```

## Setup

1. **API Key Configuration**
   - Obtain a Groq API key from [Groq Console](https://console.groq.com)
   - In Google Colab, store it as a secret named `GROQ_API_KEY`

2. **Prepare Data Files**
   - `Doctors database.json`: JSON file containing doctor information
     ```json
     [
       {
         "name": "Dr. John Smith",
         "specialty": "Cardiology",
         "experience": "15 years",
         "email": "john.smith@hospital.com"
       }
     ]
     ```

3. **Upload Required Files**
   - Upload `Doctors database.json` to your Colab environment
   - The system will create `Doctor appointment requests.csv` automatically

## Usage

### Basic Examples

```python
# Search for doctors by specialty
response = await scheduling_agent.run(
    input="Which doctors are cardiologists?"
)
print(response.get("response"))

# Schedule an appointment
response = await scheduling_agent.run(
    input="Please setup an appointment with John Smith for Ben Jones next week in the afternoons"
)
print(response.get("response"))

# Combined search and scheduling
response = await scheduling_agent.run(
    input="Find a neurologist and request an appointment for Beth Wilson at the earliest"
)
print(response.get("response"))
```


## How It Works

### 1. Document Processing
- Loads doctor database from JSON
- Splits documents into chunks using `SentenceSplitter`
- Creates vector embeddings using HuggingFace's `BAAI/bge-small-en-v1.5`
- Indexes documents for semantic search

### 2. Tool Definition
- **Doctor Query Tool**: Searches for doctors by specialty/disease
- **Appointment Tool**: Schedules appointments with selected doctors

### 3. ReAct Agent Workflow
- Receives user input
- Reasons about which tools to use
- Executes tool calls
- Synthesizes final response
- Maintains conversation memory

### Scheduling Decision Logic

The agent:
1. Identifies intent (search vs scheduling)
2. Resolves specialty constraints
3. Extracts patient and timing preferences
4. Selects learned tools via ReAct reasoning
5. Confirms or gracefully fails if constraints cannot be met

## Configuration

### LLM Settings
```python
llm = Groq(
    model="llama-3.3-70b-versatile",
    api_key=userdata.get('GROQ_API_KEY')
)
```

### Embedding Model
```python
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)
```

### Chunk Size
```python
splitter = SentenceSplitter(chunk_size=200)
```

## Output Files

- **Doctor appointment requests.csv**: Contains all scheduled appointments with fields:
  - Requested Date
  - Patient Name
  - Doctor Name
  - Scheduling Comments

### Example Flow

User: "Find a neurologist and schedule an appointment next week"

Agent reasoning:
- Identifies specialty = Neurology
- Uses semantic search to retrieve matching doctors
- Selects scheduling tool
- Writes appointment request to CSV
- Responds with confirmation summary

## Error Handling

The agent includes robust error handling:
- Tool parsing errors
- Non-existent tool calls
- Tool execution failures
- LLM response parsing issues

## Limitations

- Requires internet connection for LLM API calls
- JSON database must be properly formatted
- Appointment scheduling writes to CSV (no calendar integration)
- No real-time availability checking

## Future Enhancements

- [ ] Integration with calendar APIs
- [ ] Real-time doctor availability checking
- [ ] Email notifications to doctors and patients
- [ ] Multi-language support
- [ ] Web interface for non-technical users
- [ ] Database backend instead of CSV

## Dependencies

- `llama-index`: Core framework
- `llama-index-llms-groq`: Groq LLM integration
- `llama-index-embeddings-huggingface`: Embedding models
- `llama-index-readers-json`: JSON document reader
- `llama-index-utils-workflow`: Workflow visualization
- `nest-asyncio`: Async support in notebooks

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project for your own purposes.

## Acknowledgments

- Built with [LlamaIndex](https://www.llamaindex.ai/)
- Powered by [Groq](https://groq.com/)
- Embeddings from [HuggingFace](https://huggingface.co/)

## Contact

For questions or issues, please open an issue in the GitHub repository.

---

**Note**: This is a demonstration project. For production use, implement proper security, authentication, and data validation.
