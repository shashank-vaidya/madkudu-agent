from tools import tool_functions
from crewai.project import CrewBase, agent, task, crew

import yaml
from pathlib import Path
from tools import tool_functions

print(f"Tools available in tool_functions: {list(tool_functions.keys())}")

print("Resolved agents.yaml path:", Path("crews/config/agents.yaml").resolve())
with open("crews/config/agents.yaml", "r", encoding="utf-8") as file:
    print("Agents config content:", yaml.safe_load(file))

@CrewBase
class LeadResponseCrew:
    """Lead Response Crew"""

    tools = tool_functions  # Pass tool_functions explicitly to CrewBase

    # Use absolute paths
    agents_config = str(Path("crews/config/agents.yaml").resolve())
    tasks_config = str(Path("crews/config/tasks.yaml").resolve())

    @agent
    def email_followup_agent(self):
        """Defines the email follow-up agent."""
        from crewai import Agent

        agent_config = self.agents_config["email_followup_agent"]
        print("Agent Configuration:", agent_config)  # Debug statement

        return Agent(
            config=agent_config,
            verbose=True,
            allow_delegation=False,
        )


    @task
    def send_followup_email_task(self):
        """Defines the task for sending follow-up emails."""
        from crewai import Task

        # Use the already-loaded tasks_config
        task_config = self.tasks_config["send_followup_email"]
        return Task(
            config=task_config,
            verbose=True,
            expected_output="Email content generated for follow-up."
        )



    @crew
    def crew(self):
        """Creates the Lead Response Crew."""
        from crewai import Crew, Process
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
