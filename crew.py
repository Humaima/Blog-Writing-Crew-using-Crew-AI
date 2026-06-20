from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class BlogWritingCrew():
    """Blog Writing Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def social_media_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['social_media_manager'],  # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],  # type: ignore[index]
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],  # type: ignore[index]
        )

    @task
    def editing_task(self) -> Task:
        return Task(
            config=self.tasks_config['editing_task'],  # type: ignore[index]
            output_file='output/blog_post.md'
        )

    @task
    def social_media_task(self) -> Task:
        return Task(
            config=self.tasks_config['social_media_task'],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,   # auto-populated by @agent decorator
            tasks=self.tasks,     # auto-populated by @task decorator
            process=Process.sequential,
            verbose=True
        )