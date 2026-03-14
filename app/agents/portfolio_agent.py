from app.services.github_service import GitHubService
from app.services.repo_parser import RepoParser
from app.services.scoring_engine import ScoringEngine
from app.services.ai_evaluator import AIEvaluator


class PortfolioAgent:
    """
    Main agent responsible for orchestrating the
    GitHub portfolio evaluation pipeline.
    """

    def __init__(self):
        self.github_service = GitHubService()
        self.repo_parser = RepoParser()
        self.scoring_engine = ScoringEngine()
        self.ai_evaluator = AIEvaluator()

    async def analyze_repository(self, repo_url):
        """
        Complete evaluation pipeline.
        """

        repo_url = str(repo_url)
        
        repo_data = await self.github_service.fetch_repository(repo_url)

        languages_data = await self.github_service.fetch_languages(repo_url)

        readme_data = await self.github_service.fetch_readme(repo_url)

        repo_features = self.repo_parser.build_repo_features(
            repo_data,
            languages_data,
            readme_data
        )

        portfolio_score = self.scoring_engine.calculate_final_score(repo_features)

        ai_insights = self.ai_evaluator.evaluate_repository(repo_features)

        detected_skills = repo_features.get("languages", [])

        result = {
            "repository": repo_features.get("repo_name"),
            "portfolio_score": portfolio_score,
            "skills": detected_skills,
            "insights": ai_insights
        }

        return result