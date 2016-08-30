#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # Administrator
__date__ = '2016/6/29 19:01'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from cmdtagdef import *


class BaseCommand(object):
    """
    7.2.2.3.2 Semantics

    This class is an abstract base class that is extended by the command
    classes specified in 7.2.5.5. Each command constitutes a self-describing
    class, identified by a unique class tag. This abstract base class
    establishes a common name space for the class tags of these commands.
    The values of the class tags are defined in Table 2. As an expandable
    class the size of each class instance in bytes is encoded and accessible
    through the instance variable sizeOfInstance (see 8.3.3).

    A class that allows the aggregation of classes of type BaseCommand may
    actually aggregate any of the classes that extend BaseCommand.

    NOTE — User private commands may have an internal structure, for example
    to identify the country or manufacturer that uses a specific command.
    The tags and semantics for such user private command may be managed by
    a registration authority if required.
    """

    def __init__(self, cmd_tag=CmdTag_Forbidden00):
        self.command_tag = cmd_tag
