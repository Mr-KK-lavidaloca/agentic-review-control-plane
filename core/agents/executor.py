import json
import time
from typing import Type
from pydantic import BaseModel, ValidationError


class LLMExecutionError(Exception):
    pass


class LLMExecutor:
    def __init__(self, llm, timeout_s: int = 20, max_retries: int = 1):
        self.llm = llm
        self.timeout_s = timeout_s
        self.max_retries = max_retries

    def _extract_json(self, text: str) -> dict:
        start = text.find("{")
        end = text.rfind("}") + 1
        if start == -1 or end == -1:
            raise LLMExecutionError("No JSON object found in response")
        return json.loads(text[start:end])

    def run(
        self,
        prompt: str,
        output_model: Type[BaseModel],
    ) -> dict:
        last_error = None

        for attempt in range(self.max_retries + 1):
            start_time = time.time()

            response = self.llm.invoke(prompt).content

            if time.time() - start_time > self.timeout_s:
                raise LLMExecutionError("LLM call timed out")

            try:
                raw = self._extract_json(response)
                validated = output_model(**raw)
                return validated.model_dump()
            except (json.JSONDecodeError, ValidationError, LLMExecutionError) as e:
                last_error = e

        raise LLMExecutionError(f"Failed after retries: {last_error}")
