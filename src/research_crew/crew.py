from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class ResearchCrew:
    """ResearchCrew crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def planner(self) -> Agent:
        return Agent(
            config=self.agents_config["planner"], allow_delegation=False, verbose=True
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config["writer"], allow_delegation=False, verbose=True
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config["editor"], allow_delegation=False, verbose=True
        )

    @task
    def plan(self) -> Task:
        return Task(config=self.tasks_config["plan"])

    @task
    def write(self) -> Task:
        return Task(config=self.tasks_config["write"])

    @task
    def edit(self) -> Task:
        return Task(config=self.tasks_config["edit"])

    @crew
    def crew(self) -> Crew:
        """Creates the ResearchCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
