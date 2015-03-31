#!/usr/bin/python
# -*- coding: utf-8 -*-


import mock
import unittest
import undelete as D

class HDXConnectionTest(unittest.TestCase):
  '''Unit tests for checking the connection with HDX.'''

  def test_connection_with_hdx(self):
    a = "xxx"
    b = "yyy"
    assert D.collectDatasetDataFromHDX(dataset_id = a, apikey = b) == False
