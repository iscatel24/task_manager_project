import unittest
import os
from pathlib import Path
from unittest.mock import mock_open

from buttons import (update_task, delete_task, add_task, mark_task, save_tasks, load_tasks
, show_completed, tasks_counter, show_all_tasks,find_task,show_incomplete)




class TestButtons(unittest.TestCase):
    def test_add_empty(self):
        empty_tasks = []
        self.assertEqual(add_task(empty_tasks,"123","l"),{'id': 1, 'title': '123', 'completed': False, 'priority': 'low'})

    def test_add_notempty(self):
        tasks_n_empty = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
        self.assertEqual(add_task(tasks_n_empty,"123","l"),{'id': 2, 'title': '123', 'completed': False, 'priority': 'low'})


    def test_showtasks_empty(self):
        empty_tasks = []
        self.assertIsNone(show_all_tasks(empty_tasks))

    def test_showtasks_notempty(self):
        tasks_n_empty = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
        self.assertIsNotNone(show_all_tasks(tasks_n_empty))


    def test_findtask_empty(self):
        empty_tasks = []
        self.assertIsNone(find_task(empty_tasks,1))

    def test_findtask_notempty(self):
        tasks_n_empty = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
        self.assertEqual(find_task(tasks_n_empty,1),{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'})

    def test_update_empty(self):
        empty_tasks = []
        self.assertIsNone(update_task(empty_tasks,1,"123w","l"))

    def test_update_notempty(self):
        tasks_n_empty = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
        self.assertEqual(update_task(tasks_n_empty,1,"123w","l"),{'id': 1, 'title': '123w', 'completed': False, 'priority': 'low'})
        self.assertIsNone(update_task(tasks_n_empty,2,"123w","l"))
        self.assertIsNone(update_task(tasks_n_empty,1,"123w","i"))


    def test_delete_empty(self):
        empty_tasks = []
        self.assertIsNone(delete_task(empty_tasks,1,"y"))
        self.assertIsNone(delete_task(empty_tasks, 1, "n"))

    def test_delete_notempty(self):
        empty_tasks = []
        tasks_n_empty_ = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
        self.assertEqual(delete_task(tasks_n_empty_, 1, "y"),
                          empty_tasks)
        self.assertIsNone(delete_task(tasks_n_empty_, 1, "n"))

    def test_marktask_empty(self):
        empty_tasks = []
        self.assertIsNone(mark_task(empty_tasks, 1, "y"))
        self.assertIsNone(mark_task(empty_tasks, 1, "n"))
        self.assertIsNone(mark_task(empty_tasks, 1, "123"))

    def test_marktask_notempty(self):
        tasks_n_empty = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
        self.assertEqual(mark_task(tasks_n_empty, 1, "c"),[{'id': 1, 'title': 'gdfg', 'completed': True, 'priority': 'medium'}])
        self.assertEqual(mark_task(tasks_n_empty, 1, "n"),[{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}])
        self.assertIsNone(mark_task(tasks_n_empty, 1, "123"))

    def test_savetasks_empty(self):
        empty_tasks = []
        fake_file = Path(__file__).resolve().parent / "tasks"
        self.assertIsNone(save_tasks(empty_tasks,fake_file))

    def test_savetasks_notempty(self):
        tasks_n_empty = [{'id': 1, 'title': 'gdfg1', 'completed': False, 'priority': 'medium'}]
        fake_file = Path(__file__).resolve().parent / "tasks"
        self.assertIsNone(save_tasks(tasks_n_empty,fake_file))

    def test_showcompleted_empty(self):
        empty_tasks = []
        self.assertIsNone(show_completed(empty_tasks))

    def test_showcompleted_notempty(self):
        tasks_n_empty = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
        tasks_n_empty_True = [{'id': 1, 'title': 'gdfg', 'completed': True, 'priority': 'medium'}]
        self.assertIsNone(show_completed(tasks_n_empty))
        self.assertEqual(show_completed(tasks_n_empty_True),[{"id": 1, "completed": "X","title": 'Gdfg', "priority": 'medium'}])


    def test_showincomplete_empty(self):
        empty_tasks = []
        self.assertIsNone(show_incomplete(empty_tasks))

    def test_showincomplete_notempty(self):
        tasks_n_empty = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
        tasks_n_empty_True = [{'id': 1, 'title': 'gdfg', 'completed': True, 'priority': 'medium'}]
        self.assertEqual(show_incomplete(tasks_n_empty),[{"id": 1, "completed": "","title": 'Gdfg', "priority": 'medium'}])
        self.assertIsNone(show_incomplete(tasks_n_empty_True))

    def test_counting_empty(self):
        empty_tasks = []
        self.assertEqual(tasks_counter(empty_tasks),{"completed": 0, "incomplete": 0, "total": 0})

    def test_counting_notempty(self):
        tasks_n_empty = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
        tasks_n_empty_True = [{'id': 1, 'title': 'gdfg', 'completed': True, 'priority': 'medium'}]
        self.assertEqual(tasks_counter(tasks_n_empty),{"completed": 0, "incomplete": 1, "total": 1})
        self.assertEqual(tasks_counter(tasks_n_empty_True), {"completed": 1, "incomplete": 0, "total": 1})

    def test_loadtasks_empty(self):
        empty_tasks = []
        fake_file = Path(__file__).resolve().parent / "tasks_for_loadtest_empty"
        self.assertEqual(load_tasks(fake_file),empty_tasks)

    def test_loadtasks_notempty(self):
        tasks_n_empty = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
        fake_file = Path(__file__).resolve().parent / "tasks_for_loadtest_notempty"
        self.assertEqual(load_tasks(fake_file), tasks_n_empty)

