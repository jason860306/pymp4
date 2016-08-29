#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '4/20/2016 16:01:30'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


# four cc for boxes
FourCCMp4Root = 'root'
FourCCMp4Uuid = 'uuid'

FourCCMp4Url = 'url '
FourCCMp4Urn = 'urn '

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
FourCCMp4Avc1 = 'avc1'
FourCCMp4Avc2 = 'avc2'
FourCCMp4AvcC = 'avcC'
FourCCMp4Btrt = 'btrt'
FourCCMp4M4ds = 'm4ds'
FourCCMp4Mp4a = 'mp4a'
FourCCMp4Mp4v = 'mp4v'
FourCCMp4Mp4s = 'mp4s'
FourCCMp4Esds = 'esds'
FourCCMp4Srat = 'srat'
FourCCMp4Stsz = 'stsz'
FourCCMp4Stsc = 'stsc'
FourCCMp4Stco = 'stco'
FourCCMp4Co64 = 'co64'
FourCCMp4Mdat = 'mdat'
FourCCMp4Udta = 'udta'
FourCCMp4Ftyp = 'ftyp'
FourCCMp4Free = 'free'
FourCCMp4Skip = 'skip'

# fullname for boxes
Mp4UrlFullName = 'Data Entry Url Box'
Mp4UrnFullName = 'Data Entry Urn Box '

Mp4MoovFullName = 'Movie Box'
Mp4MvhdFullName = 'Movie Header Box'
Mp4TrakFullName = 'Track Box'
Mp4TkhdFullName = 'Track Header Box'
Mp4EdtsFullName = 'Edit Box'
Mp4ElstFullName = 'Edit List Box'
Mp4MdiaFullName = 'Media Box'
Mp4MdhdFullName = 'Media Header Box'
Mp4HdlrFullName = 'Handler Reference Box'
Mp4MinfFullName = 'Media Information Box'
Mp4VmhdFullName = 'Video media header'
Mp4SmhdFullName = 'Sound media header'
Mp4DinfFullName = 'Data Information Box'
Mp4DrefFullName = 'Data Reference Box'
Mp4StblFullName = 'Sample Table Box'
Mp4SttsFullName = 'Decoding Time to Sample Box'
Mp4CttsFullName = 'Composition Time to Sample Box'
Mp4StssFullName = 'Sync Sample Box'
Mp4StsdFullName = 'Sample Description Box'
Mp4Avc1FullName = 'AVC SampleEntry'
Mp4Avc2FullName = 'AVC2 SampleEntry'
Mp4AvcCFullName = 'AVC Configuration Box'
Mp4BtrtFullName = 'MPEG4 BitRate Box'
Mp4M4dsFullName = 'MPEG4 Extension Descriptors Box'
Mp4Mp4aFullName = 'MPEG4 Audio Sample Entry'
Mp4Mp4vFullName = 'MPEG4 Visual Sample Entry'
Mp4Mp4sFullName = 'Mpeg Sample Entry'
Mp4EsdsFullName = 'Elementary Stream Descriptors'
Mp4SratFullName = 'Sampling Rate Box'
Mp4StszFullName = 'Sample Size Boxes'
Mp4StscFullName = 'Sample To Chunk Box'
Mp4StcoFullName = 'Chunk Offset Box in 32 bit'
Mp4Co64FullName = 'Chunk Offset Box in 64 bit'
Mp4MdatFullName = 'Media Data Box'
Mp4UdtaFullName = 'User Data Box'
Mp4FtypFullName = 'File Type Box'
Mp4FreeFullName = 'Free Space Box'
Mp4SkipFullName = 'Free Space Box'

# description for boxes
Mp4UrlDesc = 'a URL entry, where it gives a location to find the resource with the given URL.'
Mp4UrnDesc = 'a URN entry, where it gives a location to find the resource with the given name.'

Mp4MoovDesc = 'container for all the meta-data'
Mp4MvhdDesc = 'movie header, overall declarations'
Mp4TrakDesc = 'container for an individual track or stream'
Mp4TkhdDesc = 'track header, overall information about the track'
Mp4EdtsDesc = 'edit list container'
Mp4ElstDesc = 'an edit list'
Mp4MdiaDesc = 'container for the media information in a track'
Mp4MdhdDesc = 'media header, overall information about the media'
Mp4HdlrDesc = 'handler, at this level, the media (handler) type'
Mp4MinfDesc = 'media information container'
Mp4VmhdDesc = 'video media header, overall information (video track only)'
Mp4SmhdDesc = 'sound media header, overall information (sound track only)'
Mp4DinfDesc = 'data information atom, container'
Mp4DrefDesc = 'data reference atom, declares source(s) of media in track'
Mp4StblDesc = 'sample table atom, container for the time/space map'
Mp4SttsDesc = '(decoding) time-to-sample'
Mp4CttsDesc = 'composition time-to-sample table'
Mp4StssDesc = 'sync (key, I-frame) sample map'
Mp4StsdDesc = 'sample descriptions (codec types, initialization etc.)'
Mp4Avc1Desc = 'may only be used when the entire stream is a compliant and usable ' \
              'AVC stream as viewed by an AVC decoder operating under the ' \
              'configuration (including profile and level) given in the AVCConfigurationBox.'
Mp4Avc2Desc = 'may only be used when Extractors or Aggregators (Annex B) are required ' \
              'to be supported, and an appropriate Toolset is required (for example, ' \
              'as indicated by the file-type brands).'
Mp4AvcCDesc = 'the decoder configuration information for ISO/IEC 14496-10 video content.'
Mp4BtrtDesc = 'a bitrate box of mpeg4'
Mp4M4dsDesc = 'unknow'
Mp4Mp4aDesc = 'For audio streams, an AudioSampleEntry'
Mp4Mp4vDesc = 'For visual streams, a VisualSampleEntry is used'
Mp4Mp4sDesc = 'For all other MPEG-4 streams, a MpegSampleEntry is used'
Mp4EsdsDesc = 'Elementary Stream Descriptors'
Mp4SratDesc = 'the actual sampling rate of the audio media, expressed as a 32‐bit integer'
Mp4StszDesc = 'sample sizes (framing)'
Mp4StscDesc = 'sample-to-chunk, partial data-offset information'
Mp4StcoDesc = 'chunk offset, partial data-offset information'
Mp4Co64Desc = '64-bit chunk offset'
Mp4MdatDesc = 'Media data container'
Mp4UdtaDesc = 'user-data, copyright etc.'
Mp4FtypDesc = 'file type and compatibility'
Mp4FreeDesc = 'free space'
Mp4SkipDesc = 'free space'

# FourCC => FullName
MP4BoxesFullName = {
    FourCCMp4Moov: Mp4MoovFullName,
    FourCCMp4Mvhd: Mp4MvhdFullName,
    FourCCMp4Trak: Mp4TrakFullName,
    FourCCMp4Tkhd: Mp4TkhdFullName,
    FourCCMp4Edts: Mp4EdtsFullName,
    FourCCMp4Elst: Mp4ElstFullName,
    FourCCMp4Mdia: Mp4MdiaFullName,
    FourCCMp4Mdhd: Mp4MdhdFullName,
    FourCCMp4Hdlr: Mp4HdlrFullName,
    FourCCMp4Minf: Mp4MinfFullName,
    FourCCMp4Vmhd: Mp4VmhdFullName,
    FourCCMp4Smhd: Mp4SmhdFullName,
    FourCCMp4Dinf: Mp4DinfFullName,
    FourCCMp4Dref: Mp4DrefFullName,
    FourCCMp4Stbl: Mp4StblFullName,
    FourCCMp4Stts: Mp4SttsFullName,
    FourCCMp4Ctts: Mp4CttsFullName,
    FourCCMp4Stss: Mp4StssFullName,
    FourCCMp4Stsd: Mp4StsdFullName,
    FourCCMp4Avc1: Mp4Avc1FullName,
    FourCCMp4Avc2: Mp4Avc2FullName,
    FourCCMp4AvcC: Mp4AvcCFullName,
    FourCCMp4Btrt: Mp4BtrtFullName,
    FourCCMp4M4ds: Mp4M4dsFullName,
    FourCCMp4Mp4a: Mp4Mp4aFullName,
    FourCCMp4Mp4v: Mp4Mp4vFullName,
    FourCCMp4Mp4s: Mp4Mp4sFullName,
    FourCCMp4Esds: Mp4EsdsFullName,
    FourCCMp4Srat: Mp4SratFullName,
    FourCCMp4Stsz: Mp4StszFullName,
    FourCCMp4Stsc: Mp4StscFullName,
    FourCCMp4Stco: Mp4StcoFullName,
    FourCCMp4Co64: Mp4Co64FullName,
    FourCCMp4Mdat: Mp4MdatFullName,
    FourCCMp4Udta: Mp4UdtaFullName,
    FourCCMp4Ftyp: Mp4FtypFullName,
    FourCCMp4Free: Mp4FreeFullName,
    FourCCMp4Skip: Mp4SkipFullName,
    FourCCMp4Url: Mp4UrlFullName,
    FourCCMp4Urn: Mp4UrnFullName
}

# FourCC => Desc
MP4BoxesDesc = {
    FourCCMp4Moov: Mp4MoovDesc,
    FourCCMp4Mvhd: Mp4MvhdDesc,
    FourCCMp4Trak: Mp4TrakDesc,
    FourCCMp4Tkhd: Mp4TkhdDesc,
    FourCCMp4Edts: Mp4EdtsDesc,
    FourCCMp4Elst: Mp4ElstDesc,
    FourCCMp4Mdia: Mp4MdiaDesc,
    FourCCMp4Mdhd: Mp4MdhdDesc,
    FourCCMp4Hdlr: Mp4HdlrDesc,
    FourCCMp4Minf: Mp4MinfDesc,
    FourCCMp4Vmhd: Mp4VmhdDesc,
    FourCCMp4Smhd: Mp4SmhdDesc,
    FourCCMp4Dinf: Mp4DinfDesc,
    FourCCMp4Dref: Mp4DrefDesc,
    FourCCMp4Stbl: Mp4StblDesc,
    FourCCMp4Stts: Mp4SttsDesc,
    FourCCMp4Ctts: Mp4CttsDesc,
    FourCCMp4Stss: Mp4StssDesc,
    FourCCMp4Stsd: Mp4StsdDesc,
    FourCCMp4Avc1: Mp4Avc1Desc,
    FourCCMp4Avc2: Mp4Avc2Desc,
    FourCCMp4AvcC: Mp4AvcCDesc,
    FourCCMp4Btrt: Mp4BtrtDesc,
    FourCCMp4M4ds: Mp4M4dsDesc,
    FourCCMp4Mp4a: Mp4Mp4aDesc,
    FourCCMp4Mp4v: Mp4Mp4vDesc,
    FourCCMp4Mp4s: Mp4Mp4sDesc,
    FourCCMp4Esds: Mp4EsdsDesc,
    FourCCMp4Srat: Mp4SratDesc,
    FourCCMp4Stsz: Mp4StszDesc,
    FourCCMp4Stsc: Mp4StscDesc,
    FourCCMp4Stco: Mp4StcoDesc,
    FourCCMp4Co64: Mp4Co64Desc,
    FourCCMp4Mdat: Mp4MdatDesc,
    FourCCMp4Udta: Mp4UdtaDesc,
    FourCCMp4Ftyp: Mp4FtypDesc,
    FourCCMp4Free: Mp4FreeDesc,
    FourCCMp4Skip: Mp4SkipDesc,
    FourCCMp4Url: Mp4UrlDesc,
    FourCCMp4Urn: Mp4UrnDesc
}
