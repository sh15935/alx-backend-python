#!/usr/bin/env python3
"""Parametize a unit test"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ tests the function for following inputs """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """ method to test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Tests that a key error is raised """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ Tests that the function utils.get_json returns expected result """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ tests utils.get_json returns the expected result """
        mock_get.return_value = test_payload
        res = get_json(test_url)
        self.assertEqual(res, test_payload)
