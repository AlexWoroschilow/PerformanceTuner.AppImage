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

import hexdi
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from .widget import ContainerWidget


class DashboardScrollArea(QtWidgets.QScrollArea):

    @hexdi.inject('themes')
    def __init__(self, themes=None):
        super(DashboardScrollArea, self).__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.setWidgetResizable(True)

        self.container = ContainerWidget()
        self.setWidget(self.container)

        self.setStyleSheet(themes.get_stylesheet())

    def addWidget(self, widget):
        self.container.addWidget(widget)

    def close(self):
        super(DashboardScrollArea, self).deleteLater()
        return super(DashboardScrollArea, self).close()
