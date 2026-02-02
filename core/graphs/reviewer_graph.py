from typing import TypedDict
from langgraph.graph import StateGraph, END
import logging

from core.agents.agents import (
    lead_agent,
    backend_agent,
    ml_agent,
    security_agent,
    infra_agent,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------------------------
# State definition
# -------------------------
class ReviewState(TypedDict):
    design: str
    backend: dict
    ml: dict
    security: dict
    infra: dict
    final: dict


# -------------------------
# Agent nodes
# -------------------------
def backend_node(state: ReviewState):
    logger.info("Backend agent started")
    result = backend_agent.run(design=state["design"])
    return {"backend": result}


def ml_node(state: ReviewState):
    logger.info("ML agent started")
    result = ml_agent.run(design=state["design"])
    return {"ml": result}


def security_node(state: ReviewState):
    logger.info("Security agent started")
    result = security_agent.run(design=state["design"])
    return {"security": result}


def infra_node(state: ReviewState):
    logger.info("Infra agent started")
    result = infra_agent.run(design=state["design"])
    return {"infra": result}


def lead_node(state: ReviewState):
    logger.info("Lead agent started")
    result = lead_agent.run(
        backend=state["backend"],
        ml=state["ml"],
        security=state["security"],
        infra=state["infra"],
    )
    return {"final": result}


# -------------------------
# Graph construction
# -------------------------
def build_graph():
    graph = StateGraph(ReviewState)

    graph.add_node("backend", backend_node)
    graph.add_node("ml", ml_node)
    graph.add_node("security", security_node)
    graph.add_node("infra", infra_node)
    graph.add_node("lead", lead_node)

    # Fan-out
    graph.set_entry_point("backend")
    graph.add_edge("backend", "ml")
    graph.add_edge("backend", "security")
    graph.add_edge("backend", "infra")

    # Fan-in
    graph.add_edge("ml", "lead")
    graph.add_edge("security", "lead")
    graph.add_edge("infra", "lead")

    graph.add_edge("lead", END)

    return graph.compile()

