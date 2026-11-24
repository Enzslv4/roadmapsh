import urllib
import json
from enum import Enum

class Types(Enum):
    PUSH = "PushEvent"
    CREATE = "CreateEvent"
    DELETE = "DeleteEvent"
    WATCH = "WatchEvent"
    FORK = "ForkEvent"
    FORK_APPLY = "ForkApplyEvent"
    MEMBER = "MemberEvent"
    PUBLIC = "PublicEvent"
    GIST = "GistEvent"
    ISSUES = "IssuesEvent"
    ISSUE_COMMENT = "IssueCommentEvent"
    PULL_REQUEST = "PullRequestEvent"
    PULL_REQUEST_REVIEW = "PullRequestReviewEvent"
    PULL_REQUEST_REVIEW_COMMENT = "PullRequestReviewCommentEvent"
    COMMIT_COMMENT = "CommitCommentEvent"
    GOLLUM = "GollumEvent"
    DOWNLOAD = "DownloadEvent"
    FOLLOW = "FollowEvent"
    PAGE_BUILD = "PageBuildEvent"
    STATUS = "StatusEvent"
    DEPLOYMENT = "DeploymentEvent"
    DEPLOYMENT_STATUS = "DeploymentStatusEvent"
    REPOSITORY = "RepositoryEvent"
    RELEASE = "ReleaseEvent"
    TEAM_ADD = "TeamAddEvent"
    DISCUSSION = "DiscussionEvent"
    SPONSORSHIP = "SponsorshipEvent"

class QueryFileError(Exception):
    """Raised when the JSON file exists but can't be used."""

class GHActivity:
    def __init__(self):
        self.user_activities = []

    def query_user(self, username):
        QUERY = f"https://api.github.com/users/{username}/events"
        self.user_activities = urllib.request.get(QUERY).json()
        with open(f"backend/github-user-activity/data/{username}_activity.json", "w", encoding="utf-8") as f:
            json.dump(self.user_activities, f, indent=4, ensure_ascii=False)
        return self.user_activities

    def treat_data(self):
        counts = {}
        for e in self.user_activities:
            key = (e["type"], e["repo"]["name"])
            counts[key] = counts.get(key, 0) + 1
