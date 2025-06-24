from pydantic import BaseModel, Field
from typing import List, Dict, Any
import os
from dotenv import load_dotenv
from agents import function_tool
from utils.logging_config import get_logger

load_dotenv()
logger = get_logger(__name__)

class SpecialistOutput(BaseModel):
    """Output schema for specialist agents"""
    content: str = Field(..., description="The main content/analysis in markdown format")
    sources: List[str] = Field(default_factory=list, description="List of source URLs")

class ResearchReport(BaseModel):
    """Schema for final research reports from the orchestrator"""
    title: str = Field(..., description="Title of the research report")
    executive_summary: str = Field(..., description="Brief executive summary")
    detailed_analysis: str = Field(..., description="Detailed analysis in markdown")
    key_findings: List[str] = Field(..., description="List of key findings")
    sources: List[str] = Field(default_factory=list, description="All sources used")
    methodology: str = Field(..., description="Research methodology used")

def tavily_search(query: str, search_depth: str = "advanced", max_results: int = 7) -> Dict[str, Any]:
    """
    Perform a web search using Tavily Search API.
    """
    valid_depths = ["basic", "advanced"]
    if search_depth not in valid_depths:
        logger.warning(f"Invalid search_depth '{search_depth}' provided. Defaulting to 'advanced'.")
        search_depth = "advanced"

    logger.info(f"Performing Tavily search for query: '{query}' with depth '{search_depth}'")
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        logger.error("TAVILY_API_KEY environment variable not found.")
        return {"error": "Tavily API key not configured."}
        
    try:
        from tavily import TavilyClient
        
        client = TavilyClient(api_key=api_key)
        
        response = client.search(
            query=query,
            search_depth=search_depth,
            max_results=max_results,
            include_raw_content=False
        )
        
        results = {
            "query": query,
            "results": [
                {
                    "title": r.get("title", ""),
                    "url": r.get("url", ""),
                    "content": r.get("content", ""),
                    "score": r.get("score", 0)
                }
                for r in response.get("results", [])
            ],
            "sources": [r["url"] for r in response.get("results", []) if r.get("url")]
        }
        
        logger.info(f"Tavily search successful, found {len(results['sources'])} sources.")
        return results
        
    except Exception as e:
        logger.error(f"Tavily search failed for query '{query}': {e}", exc_info=True)
        return {"error": f"Search failed: {str(e)}"}

@function_tool
def search_web(query: str, search_depth: str = "advanced", max_results: int = 7) -> dict:
    """Search the web for recent, high-quality information using the advanced Tavily API search."""
    return tavily_search(query, search_depth, max_results) 