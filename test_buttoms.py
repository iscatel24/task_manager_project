import unittest
import pytest

from buttoms import (update_task, delete_task, add_task, mark_task, save_tasks, load_tasks
, show_complete, tasks_counter, show_all_tasks,find_task,show_incomplete)

tasks_n_empty = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
tasks_n_empty_ = [{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}]
tasks_n_empty_True = [{'id': 1, 'title': 'gdfg', 'completed': True, 'priority': 'medium'}]

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


    def test_delete_empty(self):
        self.assertIsNone(delete_task(empty_tasks,1,"y"))
        self.assertIsNone(delete_task(empty_tasks, 1, "n"))

    def test_delete_notempty(self):
         self.assertEqual(delete_task(tasks_n_empty_, 1, "y"),
                          empty_tasks)
         self.assertIsNone(delete_task(tasks_n_empty_, 1, "n"))

    def test_marktask_empty(self):
        self.assertIsNone(mark_task(empty_tasks, 1, "y"))
        self.assertIsNone(mark_task(empty_tasks, 1, "n"))
        self.assertIsNone(mark_task(empty_tasks, 1, "123"))

    def test_marktask_notempty(self):
        self.assertEqual(mark_task(tasks_n_empty, 1, "c"),[{'id': 1, 'title': 'gdfg', 'completed': True, 'priority': 'medium'}])
        self.assertEqual(mark_task(tasks_n_empty, 1, "n"),[{'id': 1, 'title': 'gdfg', 'completed': False, 'priority': 'medium'}])
        self.assertIsNone(mark_task(tasks_n_empty, 1, "123"))

    def test_savetasks_empty(self):
        self.assertIsNone(save_tasks(empty_tasks))

    def test_savetasks_notempty(self):
        self.assertIsNone(save_tasks(tasks_n_empty))

    def test_showcompleted_empty(self):
        self.assertIsNone(show_complete(empty_tasks))

    def test_showcompleted_notempty(self):
        self.assertIsNone(show_complete(tasks_n_empty))
        self.assertEqual(show_complete(tasks_n_empty_True),[{"id": 1, "completed": "X","title": 'Gdfg', "priority": 'medium'}])


    def test_showincompleted_empty(self):
        self.assertIsNone(show_incomplete(empty_tasks))

    def test_showincompleted_notempty(self):
        self.assertEqual(show_incomplete(tasks_n_empty),[{"id": 1, "completed": "","title": 'Gdfg', "priority": 'medium'}])
        self.assertIsNone(show_incomplete(tasks_n_empty_True))

    def test_counting_empty(self):
        self.assertEqual(tasks_counter(empty_tasks),{"completed": 0, "incompleted": 0, "total": 0})

    def test_counting_notempty(self):
        self.assertEqual(tasks_counter(tasks_n_empty),{"completed": 0, "incompleted": 1, "total": 1})
        self.assertEqual(tasks_counter(tasks_n_empty_True), {"completed": 1, "incompleted": 0, "total": 1})
