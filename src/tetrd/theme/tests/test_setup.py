# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from tetrd.theme.testing import TETRD_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that tetrd.theme is properly installed."""

    layer = TETRD_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if tetrd.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'tetrd.theme'))

    def test_browserlayer(self):
        """Test that ITetrdThemeLayer is registered."""
        from tetrd.theme.interfaces import (
            ITetrdThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(ITetrdThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TETRD_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['tetrd.theme'])

    def test_product_uninstalled(self):
        """Test if tetrd.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'tetrd.theme'))

    def test_browserlayer_removed(self):
        """Test that ITetrdThemeLayer is removed."""
        from tetrd.theme.interfaces import ITetrdThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ITetrdThemeLayer, utils.registered_layers())
