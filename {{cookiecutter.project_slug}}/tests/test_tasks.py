#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_tasks.py
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

This is the test module for the project's tasks module.
"""

import unittest
import luigi.mock
import luigi.worker
from mock import patch
from {{cookiecutter.project_slug}}.tasks import {{cookiecutter.task_name}}

# To learn more about mocking Luigi objects, visit the link below.
# http://luigi.readthedocs.io/en/stable/api/luigi.mock.html


class TestSuite(unittest.TestCase):

    @patch('luigi.LocalTarget', side_effect=luigi.mock.MockFile)
    def test_arrange_act_assert(self, _):
        worker = luigi.worker.Worker()
        worker.add({{cookiecutter.task_name}}())
        worker.run()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
