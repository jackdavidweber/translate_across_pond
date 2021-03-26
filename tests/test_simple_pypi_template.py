#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from ..translate_across_pond.translate_across_pond import americanize, britishize

def test_americanize():
    assert americanize("colour") == 'color'