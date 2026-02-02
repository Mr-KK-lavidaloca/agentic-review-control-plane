from core.graphs.reviewer_graph import build_graph
from fastapi import HTTPException

graph = build_graph()

async def run_review(design: str) -> dict:
    try:
        result = await graph.ainvoke({"design": design})

        if "final" not in result:
            raise HTTPException(status_code=500, detail="Agent did not return final output")

        return result["final"]

    except TimeoutError:
        raise HTTPException(status_code=504, detail="LLM processing timed out")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def run_analysis(design: str) -> dict:
    result = await graph.ainvoke({"design": design})

    if "final" not in result:
        raise HTTPException(status_code=500, detail="Agent did not return final output")

    final = result["final"]

    return {
        "key_risks": final.get("top_risks", [])[:3],
        "quick_suggestions": final.get("priority_fixes", [])[:3]
    }


