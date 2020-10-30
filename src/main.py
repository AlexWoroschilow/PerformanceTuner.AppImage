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
import logging
import optparse
import os
import sys

abspath = sys.argv[0] \
    if len(sys.argv) else \
    os.path.abspath(__file__)
os.chdir(os.path.dirname(abspath))

from modules.qt5_application import desktop

if __name__ == "__main__":
    parser = optparse.OptionParser()

    logfile = os.path.expanduser('~/.config/AOD-PowerTuner/default.log')
    parser.add_option("--logfile", default=logfile, dest="logfile", help="Logfile location")
    parser.add_option("--loglevel", default=logging.DEBUG, dest="loglevel", help="Logging level")
    configfile = os.path.expanduser('~/.config/AOD-PowerTuner/default.conf')
    parser.add_option("--config", default=configfile, dest="config", help="Config file location")
    (options, args) = parser.parse_args()

    log_format = '[%(relativeCreated)d][%(name)s] %(levelname)s - %(message)s'
    logging.basicConfig(level=options.loglevel, format=log_format)

    application = desktop.Application(options, args)
    sys.exit(application.exec_(options, args))
