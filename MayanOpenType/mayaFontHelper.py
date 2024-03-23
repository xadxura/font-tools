# egyptian opentype helper

import os
from os import listdir
from os.path import isfile, join
import re
import codecs
import math
from fontTools import ttx
from fontTools.ttLib import TTFont
from fontTools.ufoLib import UFOReader
from fontTools.ttLib.tables._g_l_y_f import Glyph

ver = 0.1

# TODO

class MayaFontHelper:
  def __init__(self):
    pass

  def loadUFOFont(self):
    print('Loading Maya UFO font')

    path = '../../fonts/Mayan/Classic/MayaClassic.ufo'

    ufo = UFOReader(path)
    glyphset = ufo.getGlyphSet()
    list = glyphset.getComponentReferences()
    for l in list:
      print (l)

    pass

  pass