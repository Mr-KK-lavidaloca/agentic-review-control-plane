"""
Re-export shim.

This file preserves backward compatibility.
All agent construction lives in registry.py.
"""

from core.agents.registry import (
    backend_agent,
    ml_agent,
    security_agent,
    infra_agent,
    lead_agent,
)

__all__ = [
    "backend_agent",
    "ml_agent",
    "security_agent",
    "infra_agent",
    "lead_agent",
]

