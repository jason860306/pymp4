#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-12 15:06:52'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class IPMPTool(object, BaseDescriptor):
    """
    7.2.6.14.3.2.1 Syntax
    class IPMP_Tool extends BaseDescriptor
        : bit(8) tag= IPMP_ToolTag
    {
        bit(128) IPMP_ToolID;
        bit(1) isAltGroup;
        bit(1) isParametric;
        const bit(6) reserved=0b0000.00;
        if(isAltGroup){
            bit(8) numAlternates;
            bit(128) specificToolID[numAlternates];
        }
        if(isParametric)
            IPMP_ParamtericDescription toolParamDesc;
        ByteArray ToolURL[];
    }
    7.2.6.14.3.2.2 Semantics

    Each instance of Class IPMP_Tool identifies one IPMP Tool that is required
    by the Terminal to Consume the Content. This Tool shall be specified either
    as a unique implementation, as one of a list of alternatives, or through a
    parametric description.

    A unique implementation is indicated by the isAltGroup and isParametric
    fields both set to zero. In this case, the IPMP_ToolID shall be from the
    range reserved for specific implementations of an IPMP Tool and shall
    directly indicate the required Tool.

    In all other cases, the IPMP_ToolID serves as a Content-specific abstraction
    for an IPMP Tool ID since the actual IPMP Tool ID of the Tool is not known at
    the time of authoring the Content, and will depend on the Terminal implementation
    at a given time for a given piece of Content.

    A parametric description is indicated by setting the isParametric field to one.
    In this case, the Terminal shall select an IPMP Tool that meets the criteria
    specified in the following parametric description. In this case, the IPMP_ToolID
    shall be from the range reserved for Parametric Tools or Alternative Tools. The
    actual IPMP Tool ID of the Tool that the terminal implementation selects to
    fulfill this parametric description is known only to the Terminal. All the Content,
    and other tools, will refer to this Tool, for this Content, via the IPMP_ToolID
    specified. Note, this is not for message addressing.

    A list of alternative Tools is indicated by setting the isAltGroup flag to ”1”.
    The subsequent specific Tool IDs indicate the Tools that are equivalent
    alternatives to each other. If the isParametric field is also set to one, any
    Tool that is selected under the conditions for parametric tools (as discussed
    in the paragraph above) shall be considered by the Terminal to be another
    equivalent alternative to those specified via specific Tool IDs. The Terminal shall
    choose one from these equivalent alternatives at its discretion. The actual IPMP
    Tool ID of this Tool is known only to the Terminal.

    IPMP_ToolID – the identifier of the IPMP Tool, as discussed above.

    isAltGroup – if set to one, this IPMP_Tool contains a list of alternate IPMP Tools.

    numAlternates – the number of alternative IPMP Tools specified in IPMP_Tool.

    specificToolID – an array of the IDs of specific alternative IPMP Tools that can
    allow consumption of the content.

    isParametric – IPMP_Tool contains a parametric description of an IPMP Tool. In this
    case, IPMP_ToolID is an identifier for the parametrically described IPMP Tool, and
    the Terminal shall route information specified in the bitstream for IPMP_ToolID to
    the specific IPMP Tool instantiated by the terminal.

    ToolURL – An array of informative URLs from which one or more tools specified in
    IPMP_Tool may be obtained in a manner defined outside the scope of these specifications.
    """

    def __init__(self, descr_tag=DescrTag_IPMP_ToolTag):
        super(IPMPTool, self).__init__(descr_tag)
        self.ipmpToolID = 0
        self.isAltGroup = 0
        self.isParametric = 0
        self.reserved = 0
        self.numAlternates = 0
        self.specificToolID = []  # for i in self.numAlternates
        self.toolParamDesc = None
        self.toolUrl = []
