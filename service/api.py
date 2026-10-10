"""Framework-independent API handlers for task operations."""

from dataclasses import asdict
from service.tasks import TaskStore


def create_task_endpoint(store: TaskStore, payload: dict) -> dict:
    """Create a task from a request-like payload and return its representation."""
    return asdict(store.create_task(payload["title"]))


def complete_task_endpoint(store: TaskStore, task_id: int) -> dict:
    """Mark an existing task complete and return its updated representation."""
    return asdict(store.complete_task(task_id))
