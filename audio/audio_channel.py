#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '2016-09-20 上午11:59'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


# ----------------------------------------------------------------------------------------------------------
# Table 1.19 – Channel Configuration
# ----------------------------------------------------------------------------------------------------------
# value | number of channels | audio syntactic elements, | channel to speaker mapping
#       |                    | listed in order received  |
# ----------------------------------------------------------------------------------------------------------
#   0   |         -          |             -             | defined in AOT related SpecificConfig
# ----------------------------------------------------------------------------------------------------------
#   1   |         1          | single_channel_element()  | center front speaker
# ----------------------------------------------------------------------------------------------------------
#   2   |         2          | channel_pair_element()    | left, right front speakers
# ----------------------------------------------------------------------------------------------------------
#   3   |         3          | single_channel_element(), | center front speaker,
#       |                    | channel_pair_element()    | left, right front speakers
# ----------------------------------------------------------------------------------------------------------
#   4   |         4          | single_channel_element(), | center front speaker,
#       |                    | channel_pair_element(),   | left, right center front speakers,
#       |                    | single_channel_element()  | rear surround speakers
# ----------------------------------------------------------------------------------------------------------
#   5   |         5          | single_channel_element(), | center front speaker,
#       |                    | channel_pair_element(),   | left, right front speakers,
#       |                    | channel_pair_element()    | left surround, right surround rear speakers
# ----------------------------------------------------------------------------------------------------------
#   6   |        5+1         | single_channel_element(), | center front speaker,
#       |                    | channel_pair_element(),   | left, right front speakers,
#       |                    | channel_pair_element(),   | left surround, right surround rear speakers,
#       |                    | lfe _element()            | front low frequency effects speaker
# ----------------------------------------------------------------------------------------------------------
#   7   |        7+1         | single_channel_element(), | center front speaker
#       |                    | channel_pair_element(),   | left, right center front speakers,
#       |                    | channel_pair_element(),   | left, right outside front speakers,
#       |                    | channel_pair_element(),   | left surround, right surround rear speakers,
#       |                    | lfe_element()             | front low frequency effects speaker
# ----------------------------------------------------------------------------------------------------------
#  8-15 |         -          |            -              | reserved
# ----------------------------------------------------------------------------------------------------------

AudioChannel = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 8
}
