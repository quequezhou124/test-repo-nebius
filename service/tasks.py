"""In-memory task storage; intentionally dependency-free."""

from dataclasses import dataclass, replace
from service.config import ALLOWED_TASK_STATUSES, DEFAULT_TASK_STATUS, MAX_TASK_TITLE_LENGTH


@dataclass(frozen=True)
class Task:
    id: int
    title: str
    status: str = DEFAULT_TASK_STATUS


class TaskStore:
    def __init__(self):
        self._tasks = {}

    def create_task(self, title: str) -> Task:
        if not title or not title.strip():
            raise ValueError("title must not be empty")
        if len(title) > MAX_TASK_TITLE_LENGTH:
            raise ValueError("title too long")
        task = Task(id=len(self._tasks) + 1, title=title.strip())
        self._tasks[task.id] = task
        return task

    def get_task(self, task_id: int) -> Task:
        return self._tasks[task_id]

    def complete_task(self, task_id: int) -> Task:
        task = self.get_task(task_id)
        completed = replace(task, status=ALLOWED_TASK_STATUSES[1])
        self._tasks[task_id] = completed
        return completed
