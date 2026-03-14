from urllib.parse import urlparse


def extract_repo_path(repo_url: str) -> str:
    """
    Extract 'owner/repo' from GitHub URL.

    Example:
    https://github.com/user/project -> user/project
    """
    parsed = urlparse(repo_url)
    path = parsed.path.strip("/")

    parts = path.split("/")

    if len(parts) < 2:
        raise ValueError("Invalid GitHub repository URL")

    owner = parts[0]
    repo = parts[1]

    return f"{owner}/{repo}"


def normalize_repo_url(repo_url: str) -> str:
    """
    Normalize GitHub repository URL.
    Removes trailing slash and query params.
    """
    repo_url = repo_url.split("?")[0]
    repo_url = repo_url.rstrip("/")

    return repo_url


def is_valid_github_repo(repo_url: str) -> bool:
    """
    Basic validation for GitHub repository URLs.
    """
    try:
        parsed = urlparse(repo_url)

        if "github.com" not in parsed.netloc:
            return False

        parts = parsed.path.strip("/").split("/")

        if len(parts) < 2:
            return False

        return True

    except Exception:
        return False