from typing import Dict


class ScoringEngine:
    """
    Computes portfolio scores based on repository features.
    """

    def calculate_complexity_score(self, features: Dict) -> float:
        """
        Estimate project complexity based on repository size and language diversity.
        """
        size = features.get("size", 0)
        language_count = features.get("language_count", 0)

        size_score = min(size / 1000, 10)  # normalize repo size
        language_score = min(language_count * 2, 10)

        return round(size_score + language_score, 2)

    def calculate_activity_score(self, features: Dict) -> float:
        """
        Activity score based on stars, forks, and watchers.
        """
        stars = features.get("stars", 0)
        forks = features.get("forks", 0)
        watchers = features.get("watchers", 0)

        score = (stars * 0.4) + (forks * 0.3) + (watchers * 0.3)

        return min(score / 10, 20)

    def calculate_documentation_score(self, features: Dict) -> float:
        """
        Score based on documentation quality.
        """
        doc_score = features.get("documentation_score", 0)

        return min(doc_score, 10)

    def calculate_tech_diversity_score(self, features: Dict) -> float:
        """
        Evaluate diversity of technologies used.
        """
        language_count = features.get("language_count", 0)

        return min(language_count * 2, 10)

    def calculate_final_score(self, features: Dict) -> float:
        """
        Compute final portfolio score (0–100).
        """

        complexity = self.calculate_complexity_score(features)
        activity = self.calculate_activity_score(features)
        documentation = self.calculate_documentation_score(features)
        tech_diversity = self.calculate_tech_diversity_score(features)

        final_score = complexity + activity + documentation + tech_diversity

        return round(min(final_score, 100), 2)