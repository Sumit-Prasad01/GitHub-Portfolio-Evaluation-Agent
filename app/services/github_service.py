import httpx
from typing import Dict, Any
from app.core.config import settings


class GitHubService:
    """
    Service responsible for interacting with the GitHub API.
    """

    def __init__(self):
        self.base_url = settings.GITHUB_API_URL
        self.headers = {
            "Accept": "application/vnd.github+json"
        }

        if settings.GITHUB_TOKEN:
            self.headers["Authorization"] = f"Bearer {settings.GITHUB_TOKEN}"

    async def fetch_repository(self, repo_url: str) -> Dict[str, Any]:
        """
        Fetch repository metadata from GitHub.
        """
        repo_path = self._extract_repo_path(repo_url)

        url = f"{self.base_url}/repos/{repo_path}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)

        response.raise_for_status()

        return response.json()

    async def fetch_languages(self, repo_url: str) -> Dict[str, Any]:
        """
        Fetch programming languages used in the repository.
        """
        repo_path = self._extract_repo_path(repo_url)

        url = f"{self.base_url}/repos/{repo_path}/languages"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)

        response.raise_for_status()

        return response.json()

    async def fetch_readme(self, repo_url: str) -> Dict[str, Any]:
        """
        Fetch repository README content.
        """
        repo_path = self._extract_repo_path(repo_url)

        url = f"{self.base_url}/repos/{repo_path}/readme"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)

        if response.status_code == 404:
            return {}

        response.raise_for_status()

        return response.json()

    async def fetch_commit_activity(self, repo_url: str) -> Dict[str, Any]:
        """
        Fetch commit activity statistics.
        """
        repo_path = self._extract_repo_path(repo_url)

        url = f"{self.base_url}/repos/{repo_path}/stats/commit_activity"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)

        if response.status_code != 200:
            return {}

        return response.json()

    def _extract_repo_path(self, repo_url: str) -> str:
        """
        Convert repo URL into GitHub API repo path.

        Example:
        https://github.com/user/project -> user/project
        """
        return repo_url.replace("https://github.com/", "").strip("/")