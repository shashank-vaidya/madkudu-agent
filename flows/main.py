from tools import tool_functions

# Register tools globally
import builtins
builtins.tool_functions = tool_functions

from flows.lead_score_flow import LeadScoreFlow

if __name__ == "__main__":
    flow = LeadScoreFlow()
    flow.kickoff()

