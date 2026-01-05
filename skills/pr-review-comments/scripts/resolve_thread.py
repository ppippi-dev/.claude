#!/usr/bin/env python3
"""
Resolve or unresolve a GitHub PR review thread using GraphQL API.

Usage:
    ./resolve_thread.py <thread_id> [--unresolve]

The thread_id is the GraphQL node ID (starts with 'PRRT_')
"""

import argparse
import json
import subprocess
import sys


RESOLVE_MUTATION = """
mutation($threadId: ID!) {
  resolveReviewThread(input: {threadId: $threadId}) {
    thread {
      id
      isResolved
    }
  }
}
"""

UNRESOLVE_MUTATION = """
mutation($threadId: ID!) {
  unresolveReviewThread(input: {threadId: $threadId}) {
    thread {
      id
      isResolved
    }
  }
}
"""


def run_mutation(mutation: str, thread_id: str) -> dict:
    """Execute GraphQL mutation using gh cli."""
    cmd = [
        "gh", "api", "graphql",
        "-f", f"query={mutation}",
        "-f", f"threadId={thread_id}"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    return json.loads(result.stdout)


def main():
    parser = argparse.ArgumentParser(
        description="Resolve or unresolve a PR review thread"
    )
    parser.add_argument("thread_id", help="Thread ID (GraphQL node ID)")
    parser.add_argument(
        "--unresolve", action="store_true", help="Unresolve instead of resolve"
    )

    args = parser.parse_args()

    mutation = UNRESOLVE_MUTATION if args.unresolve else RESOLVE_MUTATION
    action = "unresolve" if args.unresolve else "resolve"

    data = run_mutation(mutation, args.thread_id)

    if "errors" in data:
        print(f"Failed to {action} thread: {data['errors']}", file=sys.stderr)
        sys.exit(1)

    key = "unresolveReviewThread" if args.unresolve else "resolveReviewThread"
    thread = data.get("data", {}).get(key, {}).get("thread", {})

    print(json.dumps({
        "success": True,
        "action": action,
        "thread_id": thread.get("id"),
        "is_resolved": thread.get("isResolved")
    }, indent=2))


if __name__ == "__main__":
    main()
