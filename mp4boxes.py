#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/11/16 3:41 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from boxes.avc1 import Avc1
from boxes.avc2 import Avc2
from boxes.avcc import AvcC
from boxes.btrt import Btrt
from boxes.co64 import Co64
from boxes.ctts import Ctts
from boxes.dinf import Dinf
from boxes.dref import Dref
from boxes.dref import Url
from boxes.dref import Urn
from boxes.edts import Edts
from boxes.elst import Elst
from boxes.esds import Esds
from boxes.free import Free
from boxes.ftyp import Ftyp
from boxes.hdlr import Hdlr
from boxes.mdat import Mdat
from boxes.mdhd import Mdhd
from boxes.mdia import Mdia
from boxes.minf import Minf
from boxes.moov import Moov
from boxes.mp4a import Mp4a
from boxes.mp4s import Mp4s
from boxes.mp4v import Mp4v
from boxes.mvhd import Mvhd
from boxes.skip import Skip
from boxes.smhd import Smhd
from boxes.stbl import Stbl
from boxes.stco import Stco
from boxes.stsc import Stsc
from boxes.stsd import Stsd
from boxes.stss import Stss
from boxes.stsz import Stsz
from boxes.stts import Stts
from boxes.tkhd import Tkhd
from boxes.trak import Trak
from boxes.udta import Udta
from boxes.vmhd import Vmhd
from mp4boxdesc import *

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
    FourCCMp4Mp4a: Mp4a,
    FourCCMp4Mp4v: Mp4v,
    FourCCMp4Mp4s: Mp4s,
    FourCCMp4Esds: Esds,
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
