# Copyright 2015 Alex Woroschilow (alex.woroschilow@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5 import QtGui


class SettingsTitle(QtWidgets.QLabel):

    def __init__(self, text):
        super(SettingsTitle, self).__init__(text)


class SettingsDescription(QtWidgets.QLabel):

    def __init__(self, text):
        super(SettingsDescription, self).__init__(text)
        self.setWordWrap(True)
