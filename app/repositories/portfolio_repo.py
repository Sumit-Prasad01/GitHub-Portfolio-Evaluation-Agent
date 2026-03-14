from sqlalchemy.orm import Session

from app.models.db_models import Repository, PortfolioAnalysis, Skill


class PortfolioRepository:
    """
    Handles database operations related to portfolio analysis.
    """

    def __init__(self, db: Session):
        self.db = db


    def create_repository(self, repo_name: str, repo_url: str, language: str, stars: int, forks: int):
        repo = Repository(
            repo_name=repo_name,
            repo_url=repo_url,
            language=language,
            stars=stars,
            forks=forks
        )

        self.db.add(repo)
        self.db.commit()
        self.db.refresh(repo)

        return repo

    def get_repository_by_url(self, repo_url: str):
        return (
            self.db.query(Repository)
            .filter(Repository.repo_url == repo_url)
            .first()
        )


    def save_analysis(
        self,
        repository_id: int,
        complexity_score: float,
        documentation_score: float,
        activity_score: float,
        portfolio_score: float,
        ai_insights: str
    ):
        analysis = PortfolioAnalysis(
            repository_id=repository_id,
            complexity_score=complexity_score,
            documentation_score=documentation_score,
            activity_score=activity_score,
            portfolio_score=portfolio_score,
            ai_insights=ai_insights
        )

        self.db.add(analysis)
        self.db.commit()
        self.db.refresh(analysis)

        return analysis

    def get_analysis_by_repo(self, repository_id: int):
        return (
            self.db.query(PortfolioAnalysis)
            .filter(PortfolioAnalysis.repository_id == repository_id)
            .first()
        )


    def save_skills(self, analysis_id: int, skills: list):

        skill_objects = []

        for skill in skills:
            skill_obj = Skill(
                analysis_id=analysis_id,
                skill_name=skill
            )

            self.db.add(skill_obj)
            skill_objects.append(skill_obj)

        self.db.commit()

        return skill_objects