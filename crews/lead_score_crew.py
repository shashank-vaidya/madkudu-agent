import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from custom_types.custom_types import CandidateScore

# Utility function to load YAML configurations
def load_yaml(file_path):
    """Utility function to load YAML configuration."""
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@CrewBase
class LeadScoreCrew:
    """Lead Score Crew"""

    # Configuration file paths
    agents_config = "crews/config/agents.yaml"
    tasks_config = "crews/config/tasks.yaml"

    @agent
    def lead_scoring_agent(self) -> Agent:
        """Defines the lead scoring agent."""
        agent_config = load_yaml(self.agents_config)["lead_scoring_agent"]
        return Agent(
            config=agent_config,
            verbose=True,
        )

    @task
    def score_leads_task(self) -> Task:
        """Defines the task for scoring leads."""
        task_config = load_yaml(self.tasks_config)["score_leads"]
        return Task(
            config=task_config,
            output_pydantic=CandidateScore,  # CandidateScore maps to the scoring result
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Lead Scoring Crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Tasks are executed in sequence
            verbose=True,
        )
