# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'tetrd.theme:uninstall',
        ]


def post_install(context):
    """Post install script"""
    if context.readDataFile('tetrdtheme_default.txt') is None:
        return
    # Do something during the installation of this package


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('tetrdtheme_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
