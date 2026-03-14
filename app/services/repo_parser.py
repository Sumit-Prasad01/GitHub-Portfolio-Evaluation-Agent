from typing import Dict, Any


class RepoParser:
    """
    Parses raw GitHub repository data into structured metrics
    used by the scoring engine.
    """

    def parse_repository(self, repo_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract important metadata from GitHub API response.
        """

        parsed_data = {
            "repo_name": repo_data.get("name"),
            "description": repo_data.get("description"),
            "stars": repo_data.get("stargazers_count", 0),
            "forks": repo_data.get("forks_count", 0),
            "watchers": repo_data.get("watchers_count", 0),
            "open_issues": repo_data.get("open_issues_count", 0),
            "language": repo_data.get("language"),
            "size": repo_data.get("size", 0),
            "has_wiki": repo_data.get("has_wiki", False),
            "has_projects": repo_data.get("has_projects", False),
            "has_issues": repo_data.get("has_issues", False),
        }

        return parsed_data

    def parse_languages(self, languages_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract language diversity and dominant language.
        """

        if not languages_data:
            return {
                "language_count": 0,
                "primary_language": None,
                "languages": []
            }

        sorted_languages = sorted(
            languages_data.items(),
            key=lambda x: x[1],
            reverse=True
        )

        primary_language = sorted_languages[0][0]

        return {
            "language_count": len(languages_data),
            "primary_language": primary_language,
            "languages": list(languages_data.keys())
        }

    def calculate_activity_score(self, repo_data: Dict[str, Any]) -> float:
        """
        Calculate activity score based on stars, forks, and watchers.
        """

        stars = repo_data.get("stargazers_count", 0)
        forks = repo_data.get("forks_count", 0)
        watchers = repo_data.get("watchers_count", 0)

        score = (stars * 0.5) + (forks * 0.3) + (watchers * 0.2)

        return round(score, 2)

    def documentation_score(self, readme_data: Dict[str, Any]) -> float:
        """
        Evaluate documentation quality based on README presence.
        """

        if not readme_data:
            return 0

        return 10.0

    def build_repo_features(
        self,
        repo_data: Dict[str, Any],
        languages_data: Dict[str, Any],
        readme_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Combine all parsed features into one object.
        """

        parsed_repo = self.parse_repository(repo_data)
        parsed_languages = self.parse_languages(languages_data)

        activity_score = self.calculate_activity_score(repo_data)
        doc_score = self.documentation_score(readme_data)

        features = {
            **parsed_repo,
            **parsed_languages,
            "activity_score": activity_score,
            "documentation_score": doc_score
        }

        return features