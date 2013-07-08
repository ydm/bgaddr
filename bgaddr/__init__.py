# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import string

# Street prefix – ул(ица)
street_pref_re = re.compile(r'(?u)ул(?:ица|\.?)')

# Street number – № х А
num_re = re.compile(r'(?u)(?:№|но(?:мер|\.)?)?\s?(\d+ ?\w?)\b')

# Apartament building – бл(ок)
ab_re = re.compile(r'(?u)бл(?:ок|\.?)?\s*(\d* ?\w?)\b')

# Entrance – вх(од)
en_re = re.compile(r'(?u)вх(?:од|\.?)?\s*(\d* ?\w?)\b')

# Floor – ет(аж)
fl_re = re.compile(r'(?u)ет(?:аж|\.?)?\s*(\d+)\b')

# Apartament number – ап(артамент)
ap_re = re.compile(r'(?u)ап(?:артамент|\.?)?\s*(\d+)\b')


def parse_address(s):
    """Parse the given address string and return a dictionary of values
    with following keys:

    'street' -> street name
    'num'    -> number on street*
    'ab'     -> number of apartment building**
    'en'     -> entrance number**
    'fl'     -> floor number
    'ap'     -> apartament number

    * Can contain a letter optionally at the end
    ** Can contain letters

    """
    strip = lambda s: s.strip(
        string.punctuation + string.whitespace + '"' + "'")
    ret = {}
    for key, regexp in [('ap', ap_re),
                        ('fl', fl_re),
                        ('en', en_re),
                        ('ab', ab_re),
                        ('num', num_re)]:
        try:
            last = list(regexp.finditer(s))[-1]
        except (IndexError, TypeError):
            ret[key] = ''
        else:
            ret[key] = strip(last.group(1))
            s = s[:last.start()] + s[last.end():]

    # remove the str prefix
    s = street_pref_re.sub('', s)
    ret['street'] = strip(s)
    return ret
