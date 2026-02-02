from langchain_core.prompts import PromptTemplate
from core.agents.executor import LLMExecutor


class Agent:
    def __init__(self, *, name: str, prompt: PromptTemplate, output_model, executor: LLMExecutor):
        self.name = name
        self.prompt = prompt
        self.output_model = output_model
        self.executor = executor

    def run(self, **inputs) -> dict:
        formatted_prompt = self.prompt.format(**inputs)
        return self.executor.run(
            prompt=formatted_prompt,
            output_model=self.output_model,
        )
