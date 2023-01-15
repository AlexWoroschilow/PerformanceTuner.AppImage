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

from .slider import DashboardSlider


class SettingsWidget(QtWidgets.QWidget):
    default_performance = None
    default_performance_power_level = None
    default_performance_power_control = None
    default_performance_autosuspend_delay = None
    default_performance_autosuspend = None

    default_powersave = None
    default_powersave_power_level = None
    default_powersave_power_control = None
    default_powersave_autosuspend_delay = None
    default_powersave_autosuspend = None

    @hexdi.inject('config')
    def __init__(self, config):
        super(SettingsWidget, self).__init__()

        self.default_performance = config.get('default.performance.usb', 'on')
        self.default_performance_power_level = config.get('default.performance.usb.power_level', 'on')
        self.default_performance_power_control = config.get('default.performance.usb.power_control', 'on')
        self.default_performance_autosuspend_delay = int(config.get('default.performance.usb.autosuspend_delay', -1))
        self.default_performance_autosuspend = int(config.get('default.performance.usb.autosuspend', -1))

        self.default_powersave = config.get('default.powersave.usb', 'auto')
        self.default_powersave_power_level = config.get('default.powersave.usb.power_level', 'auto')
        self.default_powersave_power_control = config.get('default.powersave.usb.power_control', 'auto')
        self.default_powersave_autosuspend_delay = int(config.get('default.powersave.usb.autosuspend_delay', 500))
        self.default_powersave_autosuspend = int(config.get('default.powersave.usb.autosuspend', 500))


class SettingsPerformanceWidget(SettingsWidget):

    @hexdi.inject('config')
    def __init__(self, config):
        super(SettingsPerformanceWidget, self).__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.setContentsMargins(0, 0, 0, 0)

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setAlignment(Qt.AlignCenter)

        value = config.get('usb.performance', self.default_performance)
        slider = DashboardSlider('USB', int(value == self.default_performance))
        slider.slideAction.connect(self.action_slide)

        self.layout().addWidget(slider)

    @hexdi.inject('config')
    def action_slide(self, slider_state, config):
        value = self.default_powersave \
            if slider_state == 0 else self.default_performance
        config.set('usb.performance', value)

        value_power_level = self.default_powersave_power_level \
            if slider_state == 0 else self.default_performance_power_level
        config.set('usb.performance.power_level', value_power_level)

        value_power_control = self.default_powersave_power_control \
            if slider_state == 0 else self.default_performance_power_control
        config.set('usb.performance.power_control', value_power_control)

        value_autosuspend_delay = self.default_powersave_autosuspend_delay \
            if slider_state == 0 else self.default_performance_autosuspend_delay
        config.set('usb.performance.autosuspend_delay', value_autosuspend_delay)

        value_autosuspend = self.default_powersave_autosuspend \
            if slider_state == 0 else self.default_performance_autosuspend
        config.set('usb.performance.autosuspend', value_autosuspend)


class SettingsPowersaveWidget(SettingsWidget):

    @hexdi.inject('config')
    def __init__(self, config):
        super(SettingsPowersaveWidget, self).__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.setContentsMargins(0, 0, 0, 0)

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setAlignment(Qt.AlignCenter)

        value = config.get('usb.powersave', self.default_powersave)
        slider = DashboardSlider('USB', int(value == self.default_performance))
        slider.slideAction.connect(self.action_slide)

        self.layout().addWidget(slider)

    @hexdi.inject('config')
    def action_slide(self, slider_state, config):
        value = self.default_powersave \
            if slider_state == 0 else self.default_performance
        config.set('usb.powersave', value)

        value_power_level = self.default_powersave_power_level \
            if slider_state == 0 else self.default_performance_power_level
        config.set('usb.powersave.power_level', value_power_level)

        value_power_control = self.default_powersave_power_control \
            if slider_state == 0 else self.default_performance_power_control
        config.set('usb.powersave.power_control', value_power_control)

        value_autosuspend_delay = self.default_powersave_autosuspend_delay \
            if slider_state == 0 else self.default_performance_autosuspend_delay
        config.set('usb.powersave.autosuspend_delay', value_autosuspend_delay)

        value_autosuspend = self.default_powersave_autosuspend \
            if slider_state == 0 else self.default_performance_autosuspend
        config.set('usb.powersave.autosuspend', value_autosuspend)
