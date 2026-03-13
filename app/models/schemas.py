from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime



class RepoAnalyzeRequest(BaseModel):
    """
    Request body for repository analysis
    """
    repo_url: HttpUrl


class SkillResponse(BaseModel):
    skill_name: str

    class Config:
        from_attributes = True



class RepositoryResponse(BaseModel):
    id: int
    repo_name: str
    repo_url: str
    language: Optional[str]
    stars: int
    forks: int

    class Config:
        from_attributes = True


class PortfolioAnalysisResponse(BaseModel):
    repository: RepositoryResponse

    complexity_score: float
    documentation_score: float
    activity_score: float
    portfolio_score: float

    ai_insights: Optional[str]

    skills: List[SkillResponse] = []

    created_at: datetime

    class Config:
        from_attributes = True


class RepoAnalysisResult(BaseModel):
    """
    Lightweight response for API
    """
    portfolio_score: float
    skills: List[str]
    insights: str