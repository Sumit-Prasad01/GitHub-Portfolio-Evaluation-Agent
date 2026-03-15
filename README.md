# 🚀 GitHub Portfolio Evaluation Agent

An AI-powered system that analyzes GitHub repositories and generates a
**developer portfolio evaluation** using repository metrics, AI
reasoning, and a scoring engine.

This project was built as part of the **Agentic JSO (Job Search
Optimization) ecosystem** to automatically evaluate technical portfolios
and help recruiters quickly assess candidate capabilities.

------------------------------------------------------------------------

# ✨ Features

-   🔎 Fetch GitHub repository metadata via GitHub API
-   🧠 AI-powered project evaluation using **LangChain + Groq (LLM)**
-   📊 Portfolio scoring engine based on repository complexity and
    activity
-   🧾 Skill detection from repository languages and project metadata
-   💾 Persistent storage using **SQLite + SQLAlchemy**
-   ⚡ Fast backend API built with **FastAPI**
-   🎨 User interface built with **Streamlit**
-   🧩 Modular production-style architecture

------------------------------------------------------------------------

# 🏗️ System Architecture

User → Streamlit Frontend → FastAPI API → PortfolioAgent → GitHub API +
AI Evaluation → SQLite Database

Components:

-   **GitHubService** → Fetch repository data
-   **RepoParser** → Extract features from repository
-   **ScoringEngine** → Calculate portfolio score
-   **AIEvaluator** → AI evaluation using LangChain + Groq
-   **PortfolioAgent** → Orchestrates the evaluation pipeline

------------------------------------------------------------------------

# 📂 Project Structure

    github-portfolio-agent/
    │
    ├── app/
    │   ├── api/
    │   ├── agents/
    │   ├── services/
    │   ├── models/
    │   ├── repositories/
    │   ├── core/
    │   ├── utils/
    │   └── prompts/
    │
    ├── frontend/
    │   └── app.py
    │
    ├── scripts/
    │   └── init_db.py
    │
    ├── tests/
    │
    ├── docker/
    │
    ├── requirements.txt
    ├── README.md
    └── .env

------------------------------------------------------------------------

# ⚙️ Installation

### 1️⃣ Clone the repository

    git clone https://github.com/Sumit-Prasad01/GitHub-Portfolio-Evaluation-Agent.git
    cd github-portfolio-agent

### 2️⃣ Create virtual environment

Windows:

    python -m venv venv
    venv\Scripts\activate

Mac/Linux:

    python3 -m venv venv
    source venv/bin/activate

### 3️⃣ Install dependencies

    pip install -r requirements.txt

------------------------------------------------------------------------

# 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

    GITHUB_TOKEN=your_github_token
    GROQ_API_KEY=your_groq_api_key
    DATABASE_URL=sqlite:///./portfolio.db
    GITHUB_API_URL=https://api.github.com
    DEBUG=True

------------------------------------------------------------------------

# 🗄️ Initialize Database

Run:

    python scripts/init_db.py

This will create:

    portfolio.db

Tables:

-   users
-   repositories
-   portfolio_analysis
-   skills
-   evaluation_logs

------------------------------------------------------------------------

# ▶️ Run the Backend

    uvicorn app.main:app --reload

API Docs:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

# 🎨 Run the Frontend

    streamlit run frontend/app.py

Open:

    http://localhost:8501

------------------------------------------------------------------------

# 🧪 Example Request

    POST /analyze-repository

Body:

    {
      "repo_url": "https://github.com/langchain-ai/langchain"
    }

Example Response:

    {
      "repository": "langchain",
      "portfolio_score": 84.3,
      "skills": ["Python", "Dockerfile"],
      "insights": "Strong open-source project with modular architecture..."
    }

------------------------------------------------------------------------

# 🧠 Scoring Metrics

Portfolio score is calculated using:

-   Project complexity
-   Repository size
-   Language diversity
-   Activity (stars, forks, watchers)
-   Documentation quality

Score Range:

  Score     Interpretation
  --------- ---------------------
  80--100   Excellent portfolio
  60--79    Good portfolio
  40--59    Moderate portfolio
  \<40      Needs improvement

------------------------------------------------------------------------

# 🔮 Future Improvements

-   LangGraph multi-agent workflow
-   Background evaluation jobs (Celery + Redis)
-   GitHub commit analysis
-   Code quality analysis with AST tools
-   Vector embeddings for repository understanding
-   Developer portfolio dashboard
-   Deployment on cloud infrastructure

------------------------------------------------------------------------

# 🛠️ Tech Stack

Backend: - FastAPI - SQLAlchemy - SQLite - LangChain - Groq LLM

Frontend: - Streamlit

External APIs: - GitHub API

------------------------------------------------------------------------


