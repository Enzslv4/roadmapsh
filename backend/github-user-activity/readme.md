# GitHub User Activity

Solution to the [GitHub User Activity](https://roadmap.sh/projects/github-user-activity) project from [roadmap.sh](https://roadmap.sh).

A command line tool that fetches a GitHub user's recent public activity from the GitHub API and prints a summary in the terminal. Written in pure Python.

## Features

- Pass any GitHub username as an argument
- Fetches recent events from `https://api.github.com/users/<username>/events`
- Groups events by type and repository and prints one line per group
- Clear error messages for invalid usernames, API failures and rate limits

## Project structure

```
.
├── gh_activity.py       # GHActivity class: fetches and summarizes events
├── gh_activity_cli.py   # Entry point: reads the username and prints the result
├── pyproject.toml       # Package config (creates the github-activity command)
└── README.md
```

The fetching and summarizing logic (`GHActivity`) is kept separate from the command line interface, so it can be reused elsewhere.

## Requirements

- Python 3.8+
- No external dependencies

## Running

Run the script directly:

```bash
python3 gh_activity_cli.py <username>
```

Or install it to get the `github-activity` command:

```bash
python3 -m venv .venv
source .venv/bin/activate      # on Windows: .venv\Scripts\activate
pip install -e .

github-activity <username>
```

## Example

```bash
github-activity kamranahmedse
```

```
- Pushed 3 times to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- ...
```

## Error handling

| Situation | Behavior |
|---|---|
| No username / extra arguments | Prints usage and exits with code 1 |
| User not found (404) | `Error: user '<username>' not found` |
| Rate limit reached (403) | Explains the unauthenticated limit (60 requests/hour) |
| No internet / API down | `Error: could not reach the GitHub API` |
| User with no recent activity | `No recent activity found.` |

## Notes

- The API only returns **public** events from roughly the last 90 days, limited to the most recent ones.
- Unauthenticated requests are limited to 60 per hour per IP.

## Progress against the roadmap.sh spec

- [x] Accept the username as a command line argument
- [x] Fetch activity from the GitHub events endpoint
- [ ] Use only the standard library to fetch data (`urllib` instead of `requests`)
- [ ] Display activity grouped by event type and repository
- [ ] Human-readable message for every event type, with a fallback for unknown ones
- [ ] Graceful handling of invalid usernames, API failures and rate limits

### Possible extensions

- [ ] Filter by event type (`github-activity <username> --type PushEvent`)
- [ ] Cache responses to avoid hitting the rate limit
- [ ] More structured output (table, colors)

## What I practiced

- Consuming a REST API with the Python standard library
- Parsing and aggregating JSON data
- Handling HTTP errors and edge cases
- Packaging a CLI with `pyproject.toml`