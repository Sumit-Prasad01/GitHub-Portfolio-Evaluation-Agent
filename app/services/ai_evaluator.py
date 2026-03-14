from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.core.config import settings


class AIEvaluator:
    """
    Uses an LLM to evaluate GitHub repositories and provide insights.
    """

    def __init__(self):

        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model="llama3-70b-8192",
            temperature=0.2
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
            You are an expert software engineer and technical recruiter.

            Evaluate the following GitHub repository features:

            Repository Name: {repo_name}
            Description: {description}
            Stars: {stars}
            Forks: {forks}
            Primary Language: {primary_language}
            Languages Used: {languages}
            Repository Size: {size}

            Provide the following:

            1. Project complexity assessment
            2. Strengths of the repository
            3. Weaknesses of the project
            4. Improvement suggestions
            5. Skills demonstrated by the developer

            Keep the answer structured and concise.
            """
        )

        self.chain = self.prompt | self.llm | StrOutputParser()

    def evaluate_repository(self, repo_features: dict) -> str:
        """
        Generate AI insights for the repository.
        """

        response = self.chain.invoke(repo_features)

        return response