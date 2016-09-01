#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-19 16:15:13'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


import descr.deccfgdescr
import descr.decspecinfo
import descr.dependptr
import descr.descrtagdef
import descr.esdescr
import descr.extprofleveldescr
import descr.extslcfgdescr
import descr.initobjdescr
import descr.ipiddataset
import descr.ipidescr
import descr.ipmpdescr
import descr.ipmptool
import descr.ipmptoollstdescr
import descr.langdescr
import descr.markerdescr
import descr.objdescr
import descr.qosdescr
import descr.regdescr
import descr.slcfgdescr


def create_descr(offset=0, descr_tag=descr.descrtagdef.DescrTag_Forbidden00):
    """
    :brief source code from gpac (be famous as mp4box)
    :detail
        //
        //		CONSTRUCTORS
        //
        GF_Descriptor *gf_odf_create_descriptor(u8 tag)
        {
            GF_Descriptor *desc;

            switch (tag) {
            case GF_ODF_IOD_TAG:
                return gf_odf_new_iod();
            case GF_ODF_OD_TAG:
                return gf_odf_new_od();
            case GF_ODF_ESD_TAG:
                return gf_odf_new_esd();
            case GF_ODF_DCD_TAG:
                return gf_odf_new_dcd();
            case GF_ODF_SLC_TAG:
                //default : we create it without any predefinition...
                return gf_odf_new_slc(0);
            case GF_ODF_MUXINFO_TAG:
                return gf_odf_new_muxinfo();
            case GF_ODF_BIFS_CFG_TAG:
                return gf_odf_new_bifs_cfg();
            case GF_ODF_UI_CFG_TAG:
                return gf_odf_new_ui_cfg();
            case GF_ODF_TEXT_CFG_TAG:
                return gf_odf_new_text_cfg();
            case GF_ODF_TX3G_TAG:
                return gf_odf_new_tx3g();
            case GF_ODF_ELEM_MASK_TAG:
                return gf_odf_New_ElemMask();
            case GF_ODF_LASER_CFG_TAG:
                return gf_odf_new_laser_cfg();

            case GF_ODF_DSI_TAG:
                desc = gf_odf_new_default();
                if (!desc) return desc;
                desc->tag = GF_ODF_DSI_TAG;
                return desc;

            case GF_ODF_AUX_VIDEO_DATA:
                return gf_odf_new_auxvid();

            case GF_ODF_SEGMENT_TAG:
                return gf_odf_new_segment();
            case GF_ODF_MEDIATIME_TAG:
                return gf_odf_new_mediatime();

            //File Format Specific
            case GF_ODF_ISOM_IOD_TAG:
                return gf_odf_new_isom_iod();
            case GF_ODF_ISOM_OD_TAG:
                return gf_odf_new_isom_od();
            case GF_ODF_ESD_INC_TAG:
                return gf_odf_new_esd_inc();
            case GF_ODF_ESD_REF_TAG:
                return gf_odf_new_esd_ref();
            case GF_ODF_LANG_TAG:
                return gf_odf_new_lang();

        #ifndef GPAC_MINIMAL_ODF

            case GF_ODF_CI_TAG:
                return gf_odf_new_ci();
            case GF_ODF_SCI_TAG:
                return gf_odf_new_sup_cid();
            case GF_ODF_IPI_PTR_TAG:
                return gf_odf_new_ipi_ptr();
            //special case for the file format
            case GF_ODF_ISOM_IPI_PTR_TAG:
                desc = gf_odf_new_ipi_ptr();
                if (!desc) return desc;
                desc->tag = GF_ODF_ISOM_IPI_PTR_TAG;
                return desc;

            case GF_ODF_IPMP_PTR_TAG:
                return gf_odf_new_ipmp_ptr();
            case GF_ODF_IPMP_TAG:
                return gf_odf_new_ipmp();
            case GF_ODF_QOS_TAG:
                return gf_odf_new_qos();
            case GF_ODF_REG_TAG:
                return gf_odf_new_reg();
            case GF_ODF_CC_TAG:
                return gf_odf_new_cc();
            case GF_ODF_KW_TAG:
                return gf_odf_new_kw();
            case GF_ODF_RATING_TAG:
                return gf_odf_new_rating();
            case GF_ODF_SHORT_TEXT_TAG:
                return gf_odf_new_short_text();
            case GF_ODF_TEXT_TAG:
                return gf_odf_new_exp_text();
            case GF_ODF_CC_NAME_TAG:
                return gf_odf_new_cc_name();
            case GF_ODF_CC_DATE_TAG:
                return gf_odf_new_cc_date();
            case GF_ODF_OCI_NAME_TAG:
                return gf_odf_new_oci_name();
            case GF_ODF_OCI_DATE_TAG:
                return gf_odf_new_oci_date();
            case GF_ODF_SMPTE_TAG:
                return gf_odf_new_smpte_camera();
            case GF_ODF_EXT_PL_TAG:
                return gf_odf_new_pl_ext();
            case GF_ODF_PL_IDX_TAG:
                return gf_odf_new_pl_idx();

            case GF_ODF_IPMP_TL_TAG:
                return gf_odf_new_ipmp_tool_list();
            case GF_ODF_IPMP_TOOL_TAG:
                return gf_odf_new_ipmp_tool();

            case 0:
            case 0xFF:
                return NULL;
        #endif /*GPAC_MINIMAL_ODF*/
            default:
                //ISO Reserved
                if ( (tag >= GF_ODF_ISO_RES_BEGIN_TAG) &&
                        (tag <= GF_ODF_ISO_RES_END_TAG) ) {
                    return NULL;
                }
                desc = gf_odf_new_default();
                if (!desc) return desc;
                desc->tag = tag;
                return desc;
            }
        }
    :param descr_tag: tag for a descriptor
    :return: a descriptor instance
    """

    tmp_descr = None
    if descr_tag == descr.descrtagdef.DescrTag_Forbidden00:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ObjectDescrTag:
        tmp_descr = descr.objdescr.ObjectDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_InitialObjectDescrTag:
        tmp_descr = descr.initobjdescr.InitObjectDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_ES_DescrTag:
        tmp_descr = descr.esdescr.ESDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_DecoderConfigDescrTag:
        tmp_descr = descr.deccfgdescr.DecoderConfigDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_DecSpecificInfoTag:
        tmp_descr = descr.decspecinfo.DecoderSpecificInfo(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_SLConfigDescrTag:
        tmp_descr = descr.slcfgdescr.SLConfigDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_ContentIdentDescrTag:
        tmp_descr = descr.ipiddataset.IPIdentificationDataSet(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_SupplContentIdentDescrTag:
        tmp_descr = descr.ipiddataset.IPIdentificationDataSet(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_IPI_DescrPointerTag:
        tmp_descr = descr.ipidescr.IPIDescrPtr(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_IPMP_DescrPointerTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_IPMP_DescrTag:
        tmp_descr = descr.ipmpdescr.IPMPDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_QoS_DescrTag:
        tmp_descr = descr.qosdescr.QoSDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_RegistrationDescrTag:
        tmp_descr = descr.regdescr.RegistrationDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_ES_ID_IncTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ES_ID_RefTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_MP4_IOD_Tag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_MP4_OD_Tag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_IPL_DescrPointerRefTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ExtensionProfileLevelDescrTag:
        tmp_descr = descr.extprofleveldescr.ExtProfLevelDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_profileLevelIndicationIndexDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ISOReserved15:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ISOReserved3F:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ContentClassificationDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_KeyWordDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_RatingDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_LanguageDescrTag:
        tmp_descr = descr.langdescr.LanguageDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_ShortTextualDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ExpandedTextualDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ContentCreatorNameDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ContentCreationDateDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_OCICreatorNameDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_OCICreationDateDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_SmpteCameraPositionDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_SegmentDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_MediaTimeDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ISO_OCI_Reserved4D:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ISO_OCI_Reserved5F:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_IPMP_ToolsListDescrTag:
        tmp_descr = descr.ipmptoollstdescr.IPMPToolListDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_IPMP_ToolTag:
        tmp_descr = descr.ipmptool.IPMPTool(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_M4MuxTimingDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_M4MuxCodeTableDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ExtSLConfigDescrTag:
        tmp_descr = descr.extslcfgdescr.ExtendedSLConfigDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_M4MuxBufferSizeDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_M4MuxIdentDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_DependencyPointerTag:
        tmp_descr = descr.dependptr.DependencyPointer(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_DependencyMarkerTag:
        tmp_descr = descr.markerdescr.MarkerDescriptor(offset, descr_tag)
    elif descr_tag == descr.descrtagdef.DescrTag_M4MuxChannelDescrTag:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ISOReserved6A:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ISOReservedBF:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_UserPrivateC0:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_UserPrivateFE:
        pass
    elif descr_tag == descr.descrtagdef.DescrTag_ForbiddenFF:
        pass

    return tmp_descr
