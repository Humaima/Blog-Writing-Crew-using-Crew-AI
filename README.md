# 📝 AI CrewAI Blog Writing Crew

An AI-powered collaborative system for automated blog writing, built using [CrewAI](https://www.crewai.com/) and designed to streamline the process of generating structured, high-quality blog content with multiple specialized agents.

<img width="1337" height="692" alt="output 1" src="https://github.com/user-attachments/assets/f6c360ab-63b4-431a-9d22-140659434c03" />

<img width="1341" height="846" alt="output 2" src="https://github.com/user-attachments/assets/ed8111eb-9a37-4680-a516-19ca3cd79437" />

<img width="1296" height="736" alt="output 7" src="https://github.com/user-attachments/assets/1864eb3f-298a-4342-8b06-bf596eca2a97" />

---

## 🚀 Project Overview
This project leverages CrewAI to orchestrate a team of AI agents that work together to:
- Research topics
- Generate outlines
- Write blog drafts
- Edit and refine content
- Produce final polished articles

The workflow ensures that each agent contributes its expertise, resulting in coherent and engaging blog posts.

---

## 📂 Features
- **Multi-Agent Collaboration**: Specialized agents for research, drafting, editing, and publishing.
- **Automated Blog Workflow**: End-to-end pipeline from idea generation to final article.
- **Customizable Roles**: Define agent responsibilities based on project needs.
- **Scalable Content Creation**: Easily extendable to multiple topics or domains.

---

## 🛠️ Tech Stack
- **Python** (core implementation)
- **CrewAI Framework**
- **LangChain / LLM Integrations**
- **OpenAI API** (or other LLM providers)
- **Markdown / HTML Export** for blog-ready content

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/ai-crewai-blog-writing-crew.git
cd ai-crewai-blog-writing-crew
pip install -r requirements.txt
```

## ▶️ Usage
Run the main script to start the blog writing crew:

```bash
python main.py
```
You can configure agents and topics in the config/ folder.

## 📊 Workflow Diagram
```
flowchart TD
    A[Topic Input] --> B[Research Agent]
    B --> C[Outline Agent]
    C --> D[Draft Writing Agent]
    D --> E[Editing Agent]
    E --> F[Final Blog Output]
```

## 📑 Example Output
- **Input:** "AI in Education"
- **Output:** A structured blog post with introduction, body sections, and conclusion, ready for publishing.

## 🤝 Contributing
Contributions are welcome! Please fork the repo and submit a pull request.

## 📜 License
This project is licensed under the MIT License.

## 🌐 Links
- https://learn.nextwork.org/projects/ai-crewai-blog-writing-crew?track=high&utm_source=copilot.com
- https://www.crewai.com/?utm_source=copilot.com
