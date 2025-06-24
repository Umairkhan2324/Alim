from .agent_schema import SpecialistOutput, ResearchReport, search_web
import os
import sys

def setup_project_path():
    """Setup project root path for imports"""
    # Get the directory two levels up (project root)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

# Setup path when module is imported
setup_project_path()

__all__ = ['SpecialistOutput', 'ResearchReport', 'search_web', 'setup_project_path'] 