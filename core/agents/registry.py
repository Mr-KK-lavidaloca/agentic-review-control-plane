from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from core.schemas.review import AgentReview, FinalReview
from core.agents.executor import LLMExecutor
from core.agents.agent import Agent
from core.agents.prompts import (
    LEAD_PROMPT,
    BACKEND_PROMPT,
    ML_PROMPT,
    SECURITY_PROMPT,
    INFRA_PROMPT,
)

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

executor = LLMExecutor(
    llm=llm,
    timeout_s=20,
    max_retries=1,
)

backend_agent = Agent(
    name="backend",
    prompt=PromptTemplate(template=BACKEND_PROMPT, input_variables=["design"]),
    output_model=AgentReview,
    executor=executor,
)

ml_agent = Agent(
    name="ml",
    prompt=PromptTemplate(template=ML_PROMPT, input_variables=["design"]),
    output_model=AgentReview,
    executor=executor,
)

security_agent = Agent(
    name="security",
    prompt=PromptTemplate(template=SECURITY_PROMPT, input_variables=["design"]),
    output_model=AgentReview,
    executor=executor,
)

infra_agent = Agent(
    name="infra",
    prompt=PromptTemplate(template=INFRA_PROMPT, input_variables=["design"]),
    output_model=AgentReview,
    executor=executor,
)

lead_agent = Agent(
    name="lead",
    prompt=PromptTemplate(
        template=LEAD_PROMPT,
        input_variables=["backend", "ml", "security", "infra"],
    ),
    output_model=FinalReview,
    executor=executor,
)
