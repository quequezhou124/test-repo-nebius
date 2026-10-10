"""Regression tests for the task-service fixture."""

import unittest

from service.api import complete_task_endpoint, create_task_endpoint
from service.tasks import TaskStore


class TaskApiTests(unittest.TestCase):
    def test_create_and_complete_task(self):
        store = TaskStore()
        created = create_task_endpoint(store, {"title": "Review PR"})
        self.assertEqual(created, {"id": 1, "title": "Review PR", "status": "pending"})
        completed = complete_task_endpoint(store, 1)
        self.assertEqual(completed, {"id": 1, "title": "Review PR", "status": "completed"})
        self.assertEqual(store.get_task(1).status, "completed")

    def test_extended_title_limit(self):
        created = create_task_endpoint(TaskStore(), {"title": "x" * 120})
        self.assertEqual(len(created["title"]), 120)

    def test_too_long_title_rejected(self):
        with self.assertRaises(ValueError):
            create_task_endpoint(TaskStore(), {"title": "x" * 121})

    def test_complete_missing_task_rejected(self):
        with self.assertRaises(KeyError):
            complete_task_endpoint(TaskStore(), 99)


if __name__ == "__main__":
    unittest.main()
