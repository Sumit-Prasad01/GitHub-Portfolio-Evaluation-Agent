from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class User(Base):
    """
    Stores platform users who connect their GitHub accounts.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    github_url = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    repositories = relationship("Repository", back_populates="user")


class Repository(Base):
    """
    Stores repositories submitted for analysis.
    """
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    repo_name = Column(String, nullable=False)
    repo_url = Column(String, nullable=False)

    language = Column(String, nullable=True)
    stars = Column(Integer, default=0)
    forks = Column(Integer, default=0)

    user_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="repositories")
    analysis = relationship("PortfolioAnalysis", back_populates="repository", uselist=False)


class PortfolioAnalysis(Base):
    """
    Stores AI evaluation results for repositories.
    """
    __tablename__ = "portfolio_analysis"

    id = Column(Integer, primary_key=True, index=True)

    repository_id = Column(Integer, ForeignKey("repositories.id"))

    complexity_score = Column(Float)
    documentation_score = Column(Float)
    activity_score = Column(Float)
    portfolio_score = Column(Float)

    ai_insights = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    repository = relationship("Repository", back_populates="analysis")
    skills = relationship("Skill", back_populates="analysis")


class Skill(Base):
    """
    Stores skills detected from repositories.
    """
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    analysis_id = Column(Integer, ForeignKey("portfolio_analysis.id"))

    skill_name = Column(String)

    analysis = relationship("PortfolioAnalysis", back_populates="skills")


class EvaluationLog(Base):
    """
    Stores logs of AI evaluations for auditing and debugging.
    """
    __tablename__ = "evaluation_logs"

    id = Column(Integer, primary_key=True, index=True)

    repo_url = Column(String)
    evaluation_status = Column(String)
    message = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)