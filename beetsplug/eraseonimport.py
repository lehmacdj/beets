# -*- coding: utf-8 -*-
# This file is part of beets.
# Copyright 2021, Devin Lehmacher
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

"""Clears tag fields in media files on import."""

from __future__ import division, absolute_import, print_function

from beets.plugins import BeetsPlugin
from beets.importer import action

__author__ = 'lehmacdj@gmail.com'

def summary(item):
    return u'{0} - {1}'.format(item.artist, item.title)

class EraseOnImportPlugin(BeetsPlugin):
    def __init__(self):
        super(EraseOnImportPlugin, self).__init__()

        self.register_listener('import_task_choice', self.import_task_choice)

    def import_task_choice(self, session, task):
        if task.choice_flag == action.APPLY or task.choice_flag == action.ASIS:
            for item in task.imported_items():
                self._log.debug(u'erasing fields genre and comments for {0}', summary(item))
                # TODO: generalize by using a config value
                item.original_genre = item.genre
                item.genre = ''
                item.comments = ''
