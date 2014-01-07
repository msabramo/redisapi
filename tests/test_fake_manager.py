# Copyright 2014 redis-api authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import unittest
import os


class FakeManagerTest(unittest.TestCase):

    def remove_env(self, env):
        if env in os.environ:
            del os.environ[env]

    def setUp(self):
        os.environ["REDIS_SERVER_HOST"] = "localhost"
        self.addCleanup(self.remove_env, "REDIS_SERVER_HOST")
        from redisapi import FakeManager
        self.manager = FakeManager()

    def test_add_instance(self):
        self.assertFalse(self.manager.instance_added)
        self.manager.add_instance()
        self.assertTrue(self.manager.instance_added)

    def test_bind(self):
        self.assertFalse(self.manager.binded)
        self.manager.bind()
        self.assertTrue(self.manager.binded)

    def test_unbind(self):
        self.assertFalse(self.manager.unbinded)
        self.manager.unbind()
        self.assertTrue(self.manager.unbinded)

    def test_remove_instance(self):
        self.assertFalse(self.manager.removed)
        self.manager.remove()
        self.assertTrue(self.manager.removed)

    def test_is_ok(self):
        self.assertFalse(self.manager.is_ok())
        self.manager.ok = True
        self.assertTrue(self.manager.is_ok())