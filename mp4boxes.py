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


from avc1 import Avc1
from avc2 import Avc2
from avcc import AvcC
from btrt import Btrt
from co64 import Co64
from ctts import Ctts
from dinf import Dinf
from dref import Dref
from dref import Url
from dref import Urn
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
from mp4boxdesc import *
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
from udta import Udta
from vmhd import Vmhd

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
    FourCCMp4Avc1: Avc1,
    FourCCMp4Avc2: Avc2,
    FourCCMp4AvcC: AvcC,
    FourCCMp4Btrt: Btrt,
    # FourCCMp4M4ds: 'm4ds',
    # FourCCMp4Srat: 'srat',
    FourCCMp4Stsz: Stsz,
    FourCCMp4Stsc: Stsc,
    FourCCMp4Stco: Stco,
    FourCCMp4Co64: Co64,
    FourCCMp4Mdat: Mdat,
    FourCCMp4Udta: Udta,
    FourCCMp4Ftyp: Ftyp,
    FourCCMp4Free: Free,
    FourCCMp4Skip: Skip,
    FourCCMp4Url: Url,
    FourCCMp4Urn: Urn
}
