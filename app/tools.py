import csv
from datetime import datetime
from llama_index.core import VectorStoreIndex
from llama_index.readers.json import JSONReader


def build_doctor_index(json_path: str) -> VectorStoreIndex:
    documents = JSONReader().load_data(json_path)
    return VectorStoreIndex.from_documents(documents)


def search_doctors_tool(index: VectorStoreIndex, query: str) -> str:
    engine = index.as_query_engine()
    response = engine.query(query)
    return str(response)


def schedule_appointment_tool(
    patient_name: str,
    doctor_name: str,
    preferred_time: str,
    csv_path: str = "data/doctor_appointment_requests.csv",
) -> str:
    with open(csv_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.utcnow().isoformat(),
            patient_name,
            doctor_name,
            preferred_time,
        ])

    return f"Appointment request recorded for {patient_name} with {doctor_name} ({preferred_time})."
