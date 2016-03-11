#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/11/16 3:41 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from co64 import Co64
from ctts import Ctts
from dinf import Dinf
from dref import Dref
from edts import Edts
from elst import Elst
from free import Free
from ftyp import Ftyp
from hdlr import Hdlr
from mdat import Mdat
from mdhd import Mdhd
from mdia import Mdia
from minf import Minf
from moov import Moov
from mvhd import Mvhd
from skip import Skip
from smhd import Smhd
from stbl import Stbl
from stco import Stco
from stsc import Stsc
from stsd import Stsd
from stss import Stss
from stsz import Stsz
from stts import Stts
from tkhd import Tkhd
from trak import Trak
from udat import Udat
from vmhd import Vmhd

FourCCMp4Root = 'root'

FourCCMp4Moov = 'moov'
FourCCMp4Mvhd = 'mvhd'
FourCCMp4Trak = 'trak'
FourCCMp4Tkhd = 'tkhd'
FourCCMp4Edts = 'edts'
FourCCMp4Elst = 'elst'
FourCCMp4Mdia = 'mdia'
FourCCMp4Mdhd = 'mdhd'
FourCCMp4Hdlr = 'hdlr'
FourCCMp4Minf = 'minf'
FourCCMp4Vmhd = 'vmhd'
FourCCMp4Smhd = 'smhd'
FourCCMp4Dinf = 'dinf'
FourCCMp4Dref = 'dref'
FourCCMp4Stbl = 'stbl'
FourCCMp4Stts = 'stts'
FourCCMp4Ctts = 'ctts'
FourCCMp4Stss = 'stss'
FourCCMp4Stsd = 'stsd'
FourCCMp4Stsz = 'stsz'
FourCCMp4Stsc = 'stsc'
FourCCMp4Stco = 'stco'
FourCCMp4Co64 = 'co64'
FourCCMp4Mdat = 'mdat'
FourCCMp4Udat = 'udat'
FourCCMp4Ftyp = 'ftyp'
FourCCMp4Free = 'free'
FourCCMp4Skip = 'skip'

FourCCMp4Uuid = 'uuid'

# FourCC => BoxType
MP4Boxes = {
    FourCCMp4Moov: Moov,
    FourCCMp4Mvhd: Mvhd,
    FourCCMp4Trak: Trak,
    FourCCMp4Tkhd: Tkhd,
    FourCCMp4Edts: Edts,
    FourCCMp4Elst: Elst,
    FourCCMp4Mdia: Mdia,
    FourCCMp4Mdhd: Mdhd,
    FourCCMp4Hdlr: Hdlr,
    FourCCMp4Minf: Minf,
    FourCCMp4Vmhd: Vmhd,
    FourCCMp4Smhd: Smhd,
    FourCCMp4Dinf: Dinf,
    FourCCMp4Dref: Dref,
    FourCCMp4Stbl: Stbl,
    FourCCMp4Stts: Stts,
    FourCCMp4Ctts: Ctts,
    FourCCMp4Stss: Stss,
    FourCCMp4Stsd: Stsd,
    FourCCMp4Stsz: Stsz,
    FourCCMp4Stsc: Stsc,
    FourCCMp4Stco: Stco,
    FourCCMp4Co64: Co64,
    FourCCMp4Mdat: Mdat,
    FourCCMp4Udat: Udat,
    FourCCMp4Ftyp: Ftyp,
    FourCCMp4Free: Free,
    FourCCMp4Skip: Skip
}


def ParseFourCC(four_cc_num):
    num1 = four_cc_num & 0xFF000000 >> 24
    num2 = four_cc_num & 0x00FF0000 >> 16
    num3 = four_cc_num & 0x0000FF00 >> 8
    num4 = four_cc_num & 0x000000FF
    return "%d%d%d%d" % (num1, num2, num3, num4)
