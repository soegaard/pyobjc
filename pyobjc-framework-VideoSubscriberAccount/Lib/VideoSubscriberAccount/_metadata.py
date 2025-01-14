# This file is generated by objective.metadata
#
# Last update: Tue Jun  7 20:24:23 2022
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
constants = """$VSAccountProviderAuthenticationSchemeAPI$VSAccountProviderAuthenticationSchemeSAML$VSCheckAccessOptionPrompt$VSErrorDomain$VSErrorInfoKeyAccountProviderResponse$VSErrorInfoKeySAMLResponse$VSErrorInfoKeySAMLResponseStatus$VSErrorInfoKeyUnsupportedProviderIdentifier$VSOpenTVProviderSettingsURLString$"""
enums = """$VSAccountAccessStatusDenied@2$VSAccountAccessStatusGranted@3$VSAccountAccessStatusNotDetermined@0$VSAccountAccessStatusRestricted@1$VSErrorCodeAccessNotGranted@0$VSErrorCodeInvalidVerificationToken@5$VSErrorCodeProviderRejected@4$VSErrorCodeRejected@6$VSErrorCodeServiceTemporarilyUnavailable@3$VSErrorCodeUnsupported@7$VSErrorCodeUnsupportedProvider@1$VSErrorCodeUserCancelled@2$VSSubscriptionAccessLevelFreeWithAccount@1$VSSubscriptionAccessLevelPaid@2$VSSubscriptionAccessLevelUnknown@0$VSUserAccountQueryOptionAllDevices@1$VSUserAccountQueryOptionNone@0$"""
misc.update(
    {
        "VSSubscriptionAccessLevel": NewType("VSSubscriptionAccessLevel", int),
        "VSAccountAccessStatus": NewType("VSAccountAccessStatus", int),
        "VSErrorCode": NewType("VSErrorCode", int),
        "VSUserAccountQueryOptions": NewType("VSUserAccountQueryOptions", int),
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"accountManager:dismissViewController:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"accountManager:presentViewController:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"accountManager:shouldAuthenticateAccountProviderWithIdentifier:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"VSAccountManager",
        b"checkAccessStatusWithOptions:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"VSAccountManager",
        b"enqueueAccountMetadataRequest:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"VSAccountMetadataRequest", b"forceAuthentication", {"retval": {"type": b"Z"}})
    r(
        b"VSAccountMetadataRequest",
        b"includeAccountProviderIdentifier",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"VSAccountMetadataRequest",
        b"includeAuthenticationExpirationDate",
        {"retval": {"type": b"Z"}},
    )
    r(b"VSAccountMetadataRequest", b"isInterruptionAllowed", {"retval": {"type": b"Z"}})
    r(
        b"VSAccountMetadataRequest",
        b"setForceAuthentication:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"VSAccountMetadataRequest",
        b"setIncludeAccountProviderIdentifier:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"VSAccountMetadataRequest",
        b"setIncludeAuthenticationExpirationDate:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"VSAccountMetadataRequest",
        b"setInterruptionAllowed:",
        {"arguments": {2: {"type": b"Z"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
