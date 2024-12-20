#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_project.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
