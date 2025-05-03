from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama
import re

# Initialize LLM
llm = Llama(
    model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8
)

app = FastAPI()

# Request schema
class PredictRequest(BaseModel):
    error: str
    integration: str

# Valid classification values
valid_priorities = {"Low", "Medium", "High"}
valid_types = {"Technical", "Functional"}
valid_domains = {
    "Integration", "Finance", "HR", "Payments", "Benefits",
    "Payroll", "Compliance", "IT", "Security"
}

@app.post("/predict")
def predict(req: PredictRequest):
    # Prompt with explicit fallback instruction
    prompt = (
        f"Integration: {req.integration}. Error: {req.error}\n"
        f"Classify the error with:\n"
        f"- Priority: Low, Medium, or High\n"
        f"- Type: Technical or Functional\n"
        f"- Domain: Integration, Finance, HR, Payments, etc.\n"
        f"If you're unsure or no match is found, respond with 'I don't know'.\n\n"
        f"Respond in this format:\n"
        f"Priority: <priority>\nType: <type>\nDomain: <domain>"
    )

    # Generate from Mistral
    result = llm(prompt, max_tokens=200)
    text = result["choices"][0]["text"].strip()

    # Extract using regex
    priority_match = re.search(r"Priority:\s*(\w+)", text, re.IGNORECASE)
    type_match = re.search(r"Type:\s*(\w+)", text, re.IGNORECASE)
    domain_match = re.search(r"Domain:\s*([\w\s&-]+)", text, re.IGNORECASE)

    # Parse results
    priority = priority_match.group(1).capitalize() if priority_match else "I don't know"
    error_type = type_match.group(1).capitalize() if type_match else "I don't know"
    domain = domain_match.group(1).strip().title() if domain_match else "I don't know"

    # Validate
    if priority not in valid_priorities:
        priority = "I don't know"
    if error_type not in valid_types:
        error_type = "I don't know"
    if domain not in valid_domains:
        domain = "I don't know"

    return {
        "priority": priority,
        "type": error_type,
        "domain": domain,
        "raw_response": text
    }
