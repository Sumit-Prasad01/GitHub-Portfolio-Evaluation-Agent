from sqlalchemy.orm import Session
from fastapi import Depends

from app.core.database import get_db
from app.agents.portfolio_agent import PortfolioAgent


def get_database(db: Session = Depends(get_db)) -> Session:
    """
    Provides database session dependency.
    """
    return db


def get_portfolio_agent() -> PortfolioAgent:
    """
    Provides PortfolioAgent instance.
    """
    return PortfolioAgent()