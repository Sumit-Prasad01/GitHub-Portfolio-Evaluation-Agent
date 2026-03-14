import httpx
import base64
from typing import Dict, Any

from app.core.config import settings
from app.utils.github_helpers import extract_repo_path


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

        self.client = httpx.AsyncClient()

    async def fetch_repository(self, repo_url: str) -> Dict[str, Any]:
        """
        Fetch repository metadata from GitHub.
        """

        repo_path = extract_repo_path(repo_url)

        url = f"{self.base_url}/repos/{repo_path}"

        response = await self.client.get(url, headers=self.headers)

        response.raise_for_status()

        return response.json()

    async def fetch_languages(self, repo_url: str) -> Dict[str, Any]:
        """
        Fetch programming languages used in the repository.
        """

        repo_path = extract_repo_path(repo_url)

        url = f"{self.base_url}/repos/{repo_path}/languages"

        response = await self.client.get(url, headers=self.headers)

        response.raise_for_status()

        return response.json()

    async def fetch_readme(self, repo_url: str) -> Dict[str, Any]:
        """
        Fetch repository README content.
        """

        repo_path = extract_repo_path(repo_url)

        url = f"{self.base_url}/repos/{repo_path}/readme"

        response = await self.client.get(url, headers=self.headers)

        if response.status_code == 404:
            return {}

        response.raise_for_status()

        data = response.json()

        if "content" in data:

            decoded = base64.b64decode(data["content"]).decode("utf-8")

            return {
                "content": decoded
            }

        return {}

    async def fetch_commit_activity(self, repo_url: str) -> Dict[str, Any]:
        """
        Fetch commit activity statistics.
        """

        repo_path = extract_repo_path(repo_url)

        url = f"{self.base_url}/repos/{repo_path}/stats/commit_activity"

        response = await self.client.get(url, headers=self.headers)

        if response.status_code != 200:
            return {}

        return response.json()