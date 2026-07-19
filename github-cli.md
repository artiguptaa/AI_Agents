# GitHub CLI Setup Guide

## Overview
This document provides guidance on using the GitHub CLI (`gh`) for interacting with GitHub repositories.

## Prerequisites
- Git is installed
- GitHub CLI is installed (`gh --version`)
- Authentication is configured (`gh auth login`)

## Authentication

### Verify Authentication Status
```bash
gh auth status
```

### Login to GitHub
```bash
gh auth login
```

## Common GitHub CLI Commands

### Issues
```bash
# List open issues
gh issue list

# List all issues (open and closed)
gh issue list --state all

# View a specific issue
gh issue view <issue-number>

# Create a new issue
gh issue create --title "Issue title" --body "Description"
```

### Pull Requests
```bash
# List pull requests
gh pr list

# View a specific pull request
gh pr view <pr-number>

# Create a pull request
gh pr create --title "PR title" --body "Description"

# Merge a pull request
gh pr merge <pr-number>
```

### Repository Information
```bash
# View repository details
gh repo view

# List branches
gh repo list
```

### Workflow & CI/CD
```bash
# View workflow runs
gh run list

# View run details
gh run view <run-id>
```

## Best Practices

1. **Always verify the repository**: Use `git remote get-url origin` to confirm you're working with the correct repository
2. **Test locally first**: Make changes and test them locally before pushing to remote
3. **Use descriptive commit messages**: Clear messages help with tracking changes
4. **Request approval before state-changing operations**: Before pushing, merging, or creating PRs that affect the remote repository
5. **Respect branch protection rules**: Follow repository policies and branch protection settings

## Security

- Never expose authentication tokens
- Never print or share secrets
- Never bypass branch protection rules
- Never force push without explicit approval

## Troubleshooting

### Authentication Issues
If you encounter authentication errors, log in again:
```bash
gh auth logout
gh auth login
```

### Permission Denied
Ensure your account has the necessary permissions for the repository.

### CLI Not Found
Install the GitHub CLI from https://cli.github.com/

## Resources
- [GitHub CLI Documentation](https://cli.github.com/manual)
- [GitHub CLI Repository](https://github.com/cli/cli)
