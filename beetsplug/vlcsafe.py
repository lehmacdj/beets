# -*- coding: utf-8 -*-
# This file is part of beets.
# Copyright 2016, Blemjhoo Tezoulbr <baobab@heresiarch.info>.
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

"""Makes paths safe for use in VLC m3u playlists"""

from __future__ import division, absolute_import, print_function

from beets.plugins import BeetsPlugin

__author__ = 'lehmacdj@gmail.com'
__version__ = '1.0'

def vlc_safe_template_func(text):
    if not(text):
        return u''
    text_out = ''
    for c in text:
        if c == '#':
            continue
        elif c == '[':
            text_out += '('
        elif c == ']':
            text_out += ')'
        else:
            text_out += c
    return text_out

class VlcSafePlugin(BeetsPlugin):
    def __init__(self):
        super(VlcSafePlugin, self).__init__()

        self.template_funcs['vlc_safe'] = vlc_safe_template_func
