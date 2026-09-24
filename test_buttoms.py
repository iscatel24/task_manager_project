import unittest
import pytest

from buttoms import (update_task, delete_task, add_task, mark_task, save_tasks, load_tasks
, show_incomplete, tasks_counter, show_all_tasks,find_task)

tasks_n_empty= [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]

empty_tasks = []

class Test_buttoms(unittest.TestCase):
    def test_add_empty(self):
        self.assertEqual(add_task(empty_tasks,"123","l"),{'id': 1, 'title': '123', 'completed': False, 'priority': 'low'})

    def test_add_notempty(self):
        self.assertEqual(add_task(tasks_n_empty,"123","l"),{'id': 2, 'title': '123', 'completed': False, 'priority': 'low'})


    def test_showtasks_empty(self):
        self.assertIsNone(show_all_tasks(empty_tasks))

    def test_showtasks_notempty(self):
        self.assertIsNotNone(show_all_tasks(tasks_n_empty))


    def test_findtask_empty(self):
        self.assertIsNone(find_task(empty_tasks,1))

    def test_findtask_notempty(self):
        self.assertEqual(find_task(tasks_n_empty,1),{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'})

    def test_update_empty(self):
        self.assertIsNone(update_task(empty_tasks,1,"123w","l"))

    def test_update_notempty(self):
        self.assertEqual(update_task(tasks_n_empty,1,"123w","l"),{'id': 1, 'title': '123w', 'completed': False, 'priority': 'low'})
        self.assertIsNone(update_task(tasks_n_empty,2,"123w","l"))
        self.assertIsNone(update_task(tasks_n_empty,1,"123w","i"))


