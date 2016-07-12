#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 14:32:47'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class ESDescriptor(object, BaseDescriptor):
    """
    7.2.6.5.1 Syntax
    class ES_Descriptor extends BaseDescriptor
        : bit(8) tag=ES_DescrTag {
        bit(16) ES_ID;
        bit(1) streamDependenceFlag;
        bit(1) URL_Flag;
        bit(1) OCRstreamFlag;
        bit(5) streamPriority;
        if (streamDependenceFlag)
            bit(16) dependsOn_ES_ID;
        if (URL_Flag) {
            bit(8) URLlength;
            bit(8) URLstring[URLlength];
        }
        if (OCRstreamFlag)
            bit(16) OCR_ES_Id;
        DecoderConfigDescriptor decConfigDescr;
        if (ODProfileLevelIndication==0x01) //no SL extension.
        {
            SLConfigDescriptor slConfigDescr;
        }
        else // SL extension is possible.
        {
            SLConfigDescriptor slConfigDescr;
        }
        IPI_DescrPointer ipiPtr[0 .. 1];
        IP_IdentificationDataSet ipIDS[0 .. 255];
        IPMP_DescriptorPointer ipmpDescrPtr[0 .. 255];
        LanguageDescriptor langDescr[0 .. 255];
        QoS_Descriptor qosDescr[0 .. 1];
        RegistrationDescriptor regDescr[0 .. 1];
        ExtensionDescriptor extDescr[0 .. 255];
    }

    7.2.6.5.2 Semantics
    The ES_Descriptor conveys all information related to a particular elementary
    stream and has three major parts.

    The first part consists of the ES_ID which is a unique reference to the
    elementary stream within its name scope (see 7.2.7.2.4), a mechanism to
    describe dependencies of elementary streams within the scope of the parent
    object descriptor and an optional URL string. Dependencies and usage of URLs
    are specified in 7.2.7.

    The second part consists of the component descriptors which convey the
    parameters and requirements of the elementary stream.

    The third part is a set of optional extension descriptors that support the
    inclusion of future extensions as well as the transport of private data in
    a backward compatible way.

    ES_ID – This syntax element provides a unique label for each elementary
    stream within its name scope. The values 0 and 0xFFFF are reserved.
    streamDependenceFlag – If set to one indicates that a dependsOn_ES_ID will follow.
    URL_Flag – if set to 1 indicates that a URLstring will follow.
    OCRstreamFlag – indicates that an OCR_ES_ID syntax element will follow.
                    streamPriority – indicates a relative measure for the priority
                    of this elementary stream. An elementary stream with a higher
                    streamPriority is more important than one with a lower
                    streamPriority. The absolute values of streamPriority are not
                    normatively defined.
    dependsOn_ES_ID – is the ES_ID of another elementary stream on which this
                      elementary stream depends. The stream with dependsOn_ES_ID
                      shall also be associated to the same object descriptor as the
                      current ES_Descriptor.
    URLlength – the length of the subsequent URLstring in bytes.
    URLstring[] – contains a UTF-8 (ISO/IEC 10646-1) encoded URL that shall point to
                  the location of an SLpacketized stream by name. The parameters of
                  the SL-packetized stream that is retrieved from the URL are
                  fully specified in this ES_Descriptor.
                  See also 7.2.7.3.3. Permissible URLs may be constrained by profile
                  and levels as well as by specific delivery layers.
    OCR_ES_ID – indicates the ES_ID of the elementary stream within the name scope
                (see 7.2.7.2.4) from which the time base for this elementary stream
                is derived. Circular references between elementary streams are not
                permitted.
    decConfigDescr – is a DecoderConfigDescriptor as specified in 7.2.6.6.
    slConfigDescr – is an SLConfigDescriptor as specified in 7.2.6.8. If
                    ODProfileLevelIndication is different from 0x01, it may be an
                    extension of SLConfigDescriptor (i.e. and extended class) as
                    defined in 7.2.6.8.
    ipiPtr[] – an array of zero or one IPI_DescrPointer as specified in 7.2.6.12.
    ipIDS[] – an array of zero or more IP_IdentificationDataSet as specified in 7.2.6.9.
              Each ES_Descriptor shall have either one IPI_DescrPointer or zero up to 255
              IP_IdentificationDataSet elements. This allows to unambiguously associate
              an IP Identification to each elementary stream.
    ipmpDescrPtr[] – an array of IPMP_DescriptorPointer, as defined in 7.2.6.13, that
                     points to the IPMP_Descriptors related to the elementary stream
                     described by this ES_Descriptor. The array shall have any number
                     of zero up to 255 elements.
    langDescr[] – an array of zero or one LanguageDescriptor structures as specified
                  in 7.2.6.18.6. It indicates the language attributed to this elementary
                  stream.
    NOTE — Multichannel audio streams may be treated as one elementary stream with one
           ES_Descriptor by ISO/IEC 14496. In that case different languages present
           in different channels of the multichannel stream are not identifyable with
           a LanguageDescriptor.
    qosDescr[] – an array of zero or one QoS_Descriptor as specified in 7.2.6.15.
    extDescr[] – an array of ExtensionDescriptor structures as specified in 7.2.6.16.
    """

    def __init__(self, descr_tag=DescrTag_ES_DescrTag):
        BaseDescriptor.__init__(self, descr_tag)
        self.ES_ID = 0
        self.strmDependceFlag = 0
        self.urlFlag = 0
        self.OCRStrmFlag = 0
        self.strmPriority = 0
        self.dependsOn_ES_ID = 0  # if strmDependceFlag
        self.urlLen = 0  # if urlFlag
        self.url = ''  # if urlFlag
        self.OCR_ES_ID = 0  # if OCRStrmFlag
        self.decConfigDescr = None

        # DecoderConfigDescriptor decConfigDescr;
        # if (ODProfileLevelIndication==0x01) //no SL extension.
        # {
        #     SLConfigDescriptor slConfigDescr;
        # }
        # else // SL extension is possible.
        # {
        #     SLConfigDescriptor slConfigDescr;
        # }
        # IPI_DescrPointer ipiPtr[0 .. 1];
        # IP_IdentificationDataSet ipIDS[0 .. 255];
        # IPMP_DescriptorPointer ipmpDescrPtr[0 .. 255];
        # LanguageDescriptor langDescr[0 .. 255];
        # QoS_Descriptor qosDescr[0 .. 1];
        # RegistrationDescriptor regDescr[0 .. 1];
        # ExtensionDescriptor extDescr[0 .. 255];
        #
