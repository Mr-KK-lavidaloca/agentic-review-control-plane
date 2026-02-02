import pytest
from pydantic import BaseModel

from core.agents.executor import LLMExecutor


# ---- Dummy schema ----
class DummyOutput(BaseModel):
    foo: str
    bar: int


# ---- Fake LLM ----
class FakeLLM:
    def invoke(self, prompt: str):
        class Response:
            content = '{"foo": "ok", "bar": 42}'
        return Response()


def test_executor_success():
    llm = FakeLLM()
    executor = LLMExecutor(
        llm=llm,
        timeout_s=5,
        max_retries=0,
    )

    result = executor.run(
        prompt="irrelevant",
        output_model=DummyOutput,
    )

    assert result == {"foo": "ok", "bar": 42}
