
# ResearchCrew Crew

Welcome to **ResearchCrew Crew**, a project designed to showcase the power of collaborative AI agents, powered by [crewAI](https://crewai.com). This project uses advanced agent-based systems to generate insightful blog posts based on your chosen topic.

## Table of Contents

- [ResearchCrew Crew](#researchcrew-crew)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [Environment Setup](#environment-setup)
  - [Usage](#usage)
    - [Example](#example)
  - [Configuration](#configuration)
  - [Contributing](#contributing)
  - [License](#license)

---

## Features

- **AI Collaboration**: Multiple AI agents with specialized roles work together to accomplish tasks.
- **Customizable Workflows**: Define tasks and agent roles via configuration files.
- **Markdown Blog Post Generation**: Automatically generate well-structured blog posts for any given topic.
- **Streamlined Setup**: Simplified dependency management using [UV](https://docs.astral.sh/uv/).

---

## Installation

### Prerequisites

- **Python**: Ensure you have Python 3.12 installed.
- **UV**: This project uses UV for dependency management.

Install UV if you haven’t already:

```bash
pip install uv
```

### Setup

Sync the project dependencies by running:

```bash
uv sync
```

---

## Environment Setup

Configure your environment for seamless execution by adding the necessary environment variables to a `.env` file. For detailed guidance on setting up your LLM (Large Language Model) configuration, refer to the [crewAI documentation](https://docs.crewai.com/concepts/llms).

Example `.env` file:

```plaintext
LLM_API_KEY=your_api_key_here
MODEL_TYPE=your_model_type_here
```

---

## Usage

To start the project and generate a blog post for your chosen topic, execute the following command in the root directory:

```bash
make run topic="<Your topic here>"
```

### Example

```bash
make run topic="The future of AI in healthcare"
```

This will initialize the ResearchCrew Crew, assemble AI agents, and produce a Markdown file containing a blog post about your specified topic.

---

## Configuration

The project relies on two main configuration files:

1. **`config/tasks.yaml`**: Defines the tasks and their workflows for the AI agents.
2. **`config/agents.yaml`**: Outlines the roles, goals, and tools available to each AI agent.

Feel free to customize these files to adapt the behavior of the AI agents to your needs.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this project as per the license terms.

---
