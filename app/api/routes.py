from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.schemas import RepoAnalyzeRequest
from app.repositories.portfolio_repo import PortfolioRepository
from app.api.dependencies import get_database, get_portfolio_agent

router = APIRouter()


@router.post("/analyze-repository")
async def analyze_repository(
    request: RepoAnalyzeRequest,
    db: Session = Depends(get_database),
    agent = Depends(get_portfolio_agent)
):

    repo_url = str(request.repo_url)

    result = await agent.analyze_repository(repo_url)

    repo_db = PortfolioRepository(db)

    repo = repo_db.create_repository(
        repo_name=result["repository"],
        repo_url=repo_url,
        language=result["skills"][0] if result["skills"] else None,
        stars=0,
        forks=0
    )

    analysis = repo_db.save_analysis(
        repository_id=repo.id,
        complexity_score=0,
        documentation_score=0,
        activity_score=0,
        portfolio_score=result["portfolio_score"],
        ai_insights=result["insights"]
    )

    repo_db.save_skills(
        analysis_id=analysis.id,
        skills=result["skills"]
    )

    return result