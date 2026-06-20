# BlogWritingCrew 🚀

Welcome to BlogWritingCrew, a collaborative AI project built with crewAI. This framework enables you to orchestrate multiple AI agents working together on complex tasks—like blog writing, research, and content generation—maximizing efficiency and creativity.

<img width="1337" height="692" alt="output 1" src="https://github.com/user-attachments/assets/a4370583-eba0-4fc4-8968-15b18ee1acf1" />

<img width="1341" height="846" alt="output 2" src="https://github.com/user-attachments/assets/97017446-4596-497d-b817-537e350ad77b" />

<img width="1296" height="736" alt="output 7" src="https://github.com/user-attachments/assets/05da1502-fcc0-4636-a3bb-cb68f5081598" />

<img width="1276" height="545" alt="output 8" src="https://github.com/user-attachments/assets/686bbe76-72a6-4bd4-bb1a-0b4121c5c889" />


## 📦 Installation

Before starting, ensure you have Python >=3.10 and <3.14 installed.
This project uses UV for dependency management.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### ⚙️ Configuration

To customize your crew:

- Add your GEMINI_API_KEY in the .env file.
- Define agents in src/blog_writing_crew/config/agents.yaml.
- Define tasks in src/blog_writing_crew/config/tasks.yaml.
- Add logic, tools, and arguments in src/blog_writing_crew/crew.py.
- Provide custom inputs in src/blog_writing_crew/main.py.

This modular setup ensures flexibility—you can tailor agents and tasks to fit your workflow.

## ▶️ Running the Project
To launch your crew of AI agents:

```
crewai run
```

This command initializes the BlogWritingCrew, assembles agents, and executes tasks as defined in your configuration.

By default, the example run generates a report.md file in the root directory containing research on LLMs (Large Language Models).

## 👥 Understanding Your Crew
The BlogWritingCrew is composed of multiple AI agents, each with unique roles, goals, and tools.

- Agents are defined in config/agents.yaml.
- Tasks are defined in config/tasks.yaml.
- Agents collaborate to complete tasks, leveraging their collective intelligence to produce high-quality outputs.

This design allows you to scale from simple blog posts to complex multi-step workflows.

## 📚 Support & Resources
Need help or want to explore more?
- https://docs.crewai.com/?utm_source=copilot.com
- https://learn.nextwork.org/projects/ai-crewai-blog-writing-crew?track=high
