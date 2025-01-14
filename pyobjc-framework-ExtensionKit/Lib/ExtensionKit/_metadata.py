# This file is generated by objective.metadata
#
# Last update: Tue Jun 21 11:38:17 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$$"""
enums = """$$"""
misc.update({})
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"EXHostViewController",
        b"makeXPCConnectionWithError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"NSObject",
        b"hostViewControllerDidActivate:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"hostViewControllerWillDeactivate:error:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"shouldAcceptXPCConnection:",
        {"required": False, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
