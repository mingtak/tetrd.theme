# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import tetrd.theme


class TetrdThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=tetrd.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tetrd.theme:default')


TETRD_THEME_FIXTURE = TetrdThemeLayer()


TETRD_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TETRD_THEME_FIXTURE,),
    name='TetrdThemeLayer:IntegrationTesting'
)


TETRD_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TETRD_THEME_FIXTURE,),
    name='TetrdThemeLayer:FunctionalTesting'
)


TETRD_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TETRD_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TetrdThemeLayer:AcceptanceTesting'
)
