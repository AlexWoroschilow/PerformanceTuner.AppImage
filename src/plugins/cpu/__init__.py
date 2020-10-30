# -*- coding: utf-8 -*-
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
import os

import inject


class Loader(object):

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    @inject.params(config='config', service='plugin.service.cpu')
    def _ignores(self, status=1, config=None, service=None):
        ignored = []
        for device in service.cores():
            value_ignored = config.get('cpu.permanent.{}'.format(device.code), 0)
            if not int(value_ignored):
                continue
            if int(value_ignored) == status:
                ignored.append(device.code)
                continue
        return ignored


def configure(binder: inject.Binder, options: {} = None, args: {} = None):
    from .workspace.settings import SettingsWidget
    binder.bind_to_constructor('workspace.cpu', SettingsWidget)

    from .service import Finder
    binder.bind_to_constructor('plugin.service.cpu', Finder)


def bootstrap(options: {} = None, args: [] = None):
    from modules import qt5_window
    from modules import qt5_workspace_battery
    from modules import qt5_workspace_adapter

    @qt5_window.workspace(name='CPU', focus=False, position=2)
    @inject.params(workspace='workspace.cpu')
    def window_workspace(parent=None, workspace=None):
        return workspace

    @qt5_workspace_battery.element()
    def battery_element(parent=None):
        from .settings.panel import SettingsPowersaveWidget
        return SettingsPowersaveWidget()

    @qt5_workspace_adapter.element()
    def adapter_element(parent=None):
        from .settings.panel import SettingsPerformanceWidget
        return SettingsPerformanceWidget()

    from modules.qt5_workspace_udev import performance
    from modules.qt5_workspace_udev import powersave

    @performance.rule()
    @inject.params(config='config', service='plugin.service.cpu')
    def rule_performance(config, service):
        for device in service.devices():
            if not os.path.exists(device.path):
                continue

            yield 'echo {} > {}/cpufreq/scaling_governor'.format(
                config.get('cpu.performance', 'ondemand'), device.path
            )

    @powersave.rule()
    @inject.params(config='config', service='plugin.service.cpu')
    def rule_powersave(config, service):
        for device in service.devices():
            if not os.path.exists(device.path):
                continue

            yield 'echo {} > {}/cpufreq/scaling_governor'.format(
                config.get('cpu.powersave', 'powersave'), device.path
            )
