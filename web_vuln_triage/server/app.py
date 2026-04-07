"""
FastAPI application for the Web Vulnerability Triage Environment.
"""

from openenv.core.env_server.http_server import create_app

try:
    from ..models import WebVulnTriageAction, WebVulnTriageObservation
    from .web_vuln_triage_environment import WebVulnTriageEnvironment
except ModuleNotFoundError:
    from models import WebVulnTriageAction, WebVulnTriageObservation
    from server.web_vuln_triage_environment import WebVulnTriageEnvironment



app = create_app(
    WebVulnTriageEnvironment,
    WebVulnTriageAction,
    WebVulnTriageObservation,
    env_name="web_vuln_triage",
    max_concurrent_envs=1,
)


def main():
    """
    REQUIRED by OpenEnv validator.
    Must be callable with NO arguments.
    """
    import uvicorn

    uvicorn.run(
        app,               
        host="0.0.0.0",
        port=8000,
    )



if __name__ == "__main__":
    main()