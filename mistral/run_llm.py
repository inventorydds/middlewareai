from llama_cpp import Llama

llm = Llama(
    model_path="/models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",  # Make sure name matches actual file
    n_ctx=2048,
    n_threads=8
)

response = llm("Q: What is Retrieval-Augmented Generation? A:", max_tokens=100)
print(response["choices"][0]["text"])
