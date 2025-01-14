# This file is generated by objective.metadata
#
# Last update: Fri Jun 24 17:50:38 2022
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
constants = """$ASAuthorizationAppleIDProviderCredentialRevokedNotification$ASAuthorizationCustomMethodOther$ASAuthorizationCustomMethodRestorePurchase$ASAuthorizationCustomMethodVideoSubscriberAccount$ASAuthorizationErrorDomain$ASAuthorizationOperationImplicit$ASAuthorizationOperationLogin$ASAuthorizationOperationLogout$ASAuthorizationOperationRefresh$ASAuthorizationProviderAuthorizationOperationConfigurationRemoved$ASAuthorizationPublicKeyCredentialAttestationKindDirect$ASAuthorizationPublicKeyCredentialAttestationKindEnterprise$ASAuthorizationPublicKeyCredentialAttestationKindIndirect$ASAuthorizationPublicKeyCredentialAttestationKindNone$ASAuthorizationPublicKeyCredentialResidentKeyPreferenceDiscouraged$ASAuthorizationPublicKeyCredentialResidentKeyPreferencePreferred$ASAuthorizationPublicKeyCredentialResidentKeyPreferenceRequired$ASAuthorizationPublicKeyCredentialUserVerificationPreferenceDiscouraged$ASAuthorizationPublicKeyCredentialUserVerificationPreferencePreferred$ASAuthorizationPublicKeyCredentialUserVerificationPreferenceRequired$ASAuthorizationScopeEmail$ASAuthorizationScopeFullName$ASAuthorizationSecurityKeyPublicKeyCredentialDescriptorTransportBluetooth$ASAuthorizationSecurityKeyPublicKeyCredentialDescriptorTransportNFC$ASAuthorizationSecurityKeyPublicKeyCredentialDescriptorTransportUSB$ASCredentialIdentityStoreErrorDomain$ASExtensionErrorDomain$ASExtensionLocalizedFailureReasonErrorKey$ASWebAuthenticationSessionErrorDomain$"""
enums = """$ASAuthorizationAppleIDButtonStyleBlack@2$ASAuthorizationAppleIDButtonStyleWhite@0$ASAuthorizationAppleIDButtonStyleWhiteOutline@1$ASAuthorizationAppleIDButtonTypeContinue@1$ASAuthorizationAppleIDButtonTypeDefault@0$ASAuthorizationAppleIDButtonTypeSignIn@0$ASAuthorizationAppleIDButtonTypeSignUp@2$ASAuthorizationAppleIDProviderCredentialAuthorized@1$ASAuthorizationAppleIDProviderCredentialNotFound@2$ASAuthorizationAppleIDProviderCredentialRevoked@0$ASAuthorizationAppleIDProviderCredentialTransferred@3$ASAuthorizationControllerRequestOptionPreferImmediatelyAvailableCredentials@1$ASAuthorizationErrorCanceled@1001$ASAuthorizationErrorFailed@1004$ASAuthorizationErrorInvalidResponse@1002$ASAuthorizationErrorNotHandled@1003$ASAuthorizationErrorNotInteractive@1005$ASAuthorizationErrorUnknown@1000$ASAuthorizationProviderExtensionAuthenticationMethodPassword@1$ASAuthorizationProviderExtensionAuthenticationMethodUserSecureEnclaveKey@2$ASAuthorizationProviderExtensionKeyTypeUserDeviceEncryption@2$ASAuthorizationProviderExtensionKeyTypeUserDeviceSigning@1$ASAuthorizationProviderExtensionKeyTypeUserSecureEnclaveKey@3$ASAuthorizationProviderExtensionRegistrationResultFailed@1$ASAuthorizationProviderExtensionRegistrationResultFailedNoRetry@3$ASAuthorizationProviderExtensionRegistrationResultSuccess@0$ASAuthorizationProviderExtensionRegistrationResultUserInterfaceRequired@2$ASAuthorizationProviderExtensionRequestOptionsNone@0$ASAuthorizationProviderExtensionRequestOptionsRegistrationRepair@2$ASAuthorizationProviderExtensionRequestOptionsUserInteractionEnabled@1$ASCOSEAlgorithmIdentifierES256@-7$ASCOSEEllipticCurveIdentifierP256@1$ASCredentialIdentityStoreErrorCodeInternalError@0$ASCredentialIdentityStoreErrorCodeStoreBusy@2$ASCredentialIdentityStoreErrorCodeStoreDisabled@1$ASCredentialServiceIdentifierTypeDomain@0$ASCredentialServiceIdentifierTypeURL@1$ASExtensionErrorCodeCredentialIdentityNotFound@101$ASExtensionErrorCodeFailed@0$ASExtensionErrorCodeUserCanceled@1$ASExtensionErrorCodeUserInteractionRequired@100$ASUserDetectionStatusLikelyReal@2$ASUserDetectionStatusUnknown@1$ASUserDetectionStatusUnsupported@0$ASWebAuthenticationSessionErrorCodeCanceledLogin@1$ASWebAuthenticationSessionErrorCodePresentationContextInvalid@3$ASWebAuthenticationSessionErrorCodePresentationContextNotProvided@2$"""
misc.update(
    {
        "ASAuthorizationProviderExtensionAuthenticationMethod": NewType(
            "ASAuthorizationProviderExtensionAuthenticationMethod", int
        ),
        "ASAuthorizationAppleIDButtonType": NewType(
            "ASAuthorizationAppleIDButtonType", int
        ),
        "ASAuthorizationError": NewType("ASAuthorizationError", int),
        "ASCredentialIdentityStoreErrorCode": NewType(
            "ASCredentialIdentityStoreErrorCode", int
        ),
        "ASUserDetectionStatus": NewType("ASUserDetectionStatus", int),
        "ASAuthorizationAppleIDProviderCredentialState": NewType(
            "ASAuthorizationAppleIDProviderCredentialState", int
        ),
        "ASAuthorizationProviderExtensionRegistrationResult": NewType(
            "ASAuthorizationProviderExtensionRegistrationResult", int
        ),
        "ASAuthorizationProviderExtensionRequestOptions": NewType(
            "ASAuthorizationProviderExtensionRequestOptions", int
        ),
        "ASAuthorizationProviderExtensionKeyType": NewType(
            "ASAuthorizationProviderExtensionKeyType", int
        ),
        "ASExtensionErrorCode": NewType("ASExtensionErrorCode", int),
        "ASCredentialServiceIdentifierType": NewType(
            "ASCredentialServiceIdentifierType", int
        ),
        "ASAuthorizationAppleIDButtonStyle": NewType(
            "ASAuthorizationAppleIDButtonStyle", int
        ),
        "ASAuthorizationControllerRequestOptions": NewType(
            "ASAuthorizationControllerRequestOptions", int
        ),
        "ASWebAuthenticationSessionErrorCode": NewType(
            "ASWebAuthenticationSessionErrorCode", int
        ),
    }
)
misc.update(
    {
        "ASAuthorizationPublicKeyCredentialUserVerificationPreference": NewType(
            "ASAuthorizationPublicKeyCredentialUserVerificationPreference", str
        ),
        "ASAuthorizationProviderAuthorizationOperation": NewType(
            "ASAuthorizationProviderAuthorizationOperation", str
        ),
        "ASAuthorizationSecurityKeyPublicKeyCredentialDescriptorTransport": NewType(
            "ASAuthorizationSecurityKeyPublicKeyCredentialDescriptorTransport", str
        ),
        "ASAuthorizationScope": NewType("ASAuthorizationScope", str),
        "ASAuthorizationPublicKeyCredentialResidentKeyPreference": NewType(
            "ASAuthorizationPublicKeyCredentialResidentKeyPreference", str
        ),
        "ASCOSEEllipticCurveIdentifier": NewType("ASCOSEEllipticCurveIdentifier", int),
        "ASAuthorizationPublicKeyCredentialAttestationKind": NewType(
            "ASAuthorizationPublicKeyCredentialAttestationKind", str
        ),
        "ASAuthorizationOpenIDOperation": NewType(
            "ASAuthorizationOpenIDOperation", str
        ),
        "ASAuthorizationCustomMethod": NewType("ASAuthorizationCustomMethod", str),
        "ASCOSEAlgorithmIdentifier": NewType("ASCOSEAlgorithmIdentifier", int),
    }
)
misc.update({})
functions = {
    "ASAuthorizationAllSupportedPublicKeyCredentialDescriptorTransports": (b"@",)
}
aliases = {
    "ASAuthorizationAppleIDButtonTypeDefault": "ASAuthorizationAppleIDButtonTypeSignIn"
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"ASAccountAuthenticationModificationExtensionContext",
        b"getSignInWithAppleUpgradeAuthorizationWithState:nonce:completionHandler:",
        {
            "arguments": {
                4: {
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
    r(
        b"ASAuthorizationAppleIDProvider",
        b"getCredentialStateForUserID:completion:",
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
        b"ASAuthorizationProviderExtensionAuthorizationRequest",
        b"isCallerManaged",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"ASAuthorizationProviderExtensionAuthorizationRequest",
        b"isUserInterfaceEnabled",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"ASAuthorizationProviderExtensionAuthorizationRequest",
        b"presentAuthorizationViewControllerWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"ASAuthorizationProviderExtensionLoginConfiguration",
        b"configurationWithOpenIDConfigurationURL:clientID:issuer:completion:",
        {
            "arguments": {
                5: {
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
    r(
        b"ASAuthorizationProviderExtensionLoginConfiguration",
        b"includePreviousRefreshTokenInLoginRequest",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"ASAuthorizationProviderExtensionLoginConfiguration",
        b"setCustomAssertionRequestBodyClaims:returningError:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ASAuthorizationProviderExtensionLoginConfiguration",
        b"setCustomAssertionRequestHeaderClaims:returningError:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ASAuthorizationProviderExtensionLoginConfiguration",
        b"setCustomLoginRequestBodyClaims:returningError:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ASAuthorizationProviderExtensionLoginConfiguration",
        b"setCustomLoginRequestHeaderClaims:returningError:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ASAuthorizationProviderExtensionLoginConfiguration",
        b"setIncludePreviousRefreshTokenInLoginRequest:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"ASAuthorizationProviderExtensionLoginManager",
        b"copyIdentityForKeyType:",
        {"retval": {"already_cfretained": True}},
    )
    r(
        b"ASAuthorizationProviderExtensionLoginManager",
        b"copyKeyForKeyType:",
        {"retval": {"already_cfretained": True}},
    )
    r(
        b"ASAuthorizationProviderExtensionLoginManager",
        b"isDeviceRegistered",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"ASAuthorizationProviderExtensionLoginManager",
        b"isUserRegistered",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"ASAuthorizationProviderExtensionLoginManager",
        b"presentRegistrationViewControllerWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"ASAuthorizationProviderExtensionLoginManager",
        b"saveLoginConfiguration:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ASAuthorizationProviderExtensionLoginManager",
        b"userNeedsReauthenticationWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"ASAuthorizationSingleSignOnProvider",
        b"canPerformAuthorization",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"ASAuthorizationSingleSignOnRequest",
        b"isUserInterfaceEnabled",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"ASAuthorizationSingleSignOnRequest",
        b"setUserInterfaceEnabled:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"ASCredentialIdentityStore",
        b"getCredentialIdentityStoreStateWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"ASCredentialIdentityStore",
        b"removeAllCredentialIdentitiesWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"ASCredentialIdentityStore",
        b"removeCredentialIdentities:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"ASCredentialIdentityStore",
        b"replaceCredentialIdentitiesWithIdentities:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"ASCredentialIdentityStore",
        b"saveCredentialIdentities:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"ASCredentialIdentityStoreState", b"isEnabled", {"retval": {"type": b"Z"}})
    r(
        b"ASCredentialIdentityStoreState",
        b"supportsIncrementalUpdates",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"ASCredentialProviderExtensionContext",
        b"completeRequestReturningItems:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    }
                }
            }
        },
    )
    r(
        b"ASCredentialProviderExtensionContext",
        b"completeRequestWithSelectedCredential:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    }
                }
            }
        },
    )
    r(b"ASWebAuthenticationSession", b"canStart", {"retval": {"type": "Z"}})
    r(
        b"ASWebAuthenticationSession",
        b"initWithURL:callbackURLScheme:completionHandler:",
        {
            "arguments": {
                4: {
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
    r(
        b"ASWebAuthenticationSession",
        b"prefersEphemeralWebBrowserSession",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"ASWebAuthenticationSession",
        b"setPrefersEphemeralWebBrowserSession:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"ASWebAuthenticationSession", b"start", {"retval": {"type": b"Z"}})
    r(
        b"ASWebAuthenticationSessionRequest",
        b"shouldUseEphemeralSession",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"ASWebAuthenticationSessionWebBrowserSessionManager",
        b"wasLaunchedByAuthenticationServices",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"NSObject",
        b"accountAuthenticationModificationController:didFailRequest:withError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"accountAuthenticationModificationController:didSuccessfullyCompleteRequest:withUserInfo:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(b"NSObject", b"allowedCredentials", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"attestationPreference",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"authenticationSessionRequest:didCancelWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"authenticationSessionRequest:didCompleteWithCallbackURL:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"authorizationController:didCompleteWithAuthorization:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"authorizationController:didCompleteWithCustomMethod:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"authorizationController:didCompleteWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"beginAuthorizationWithRequest:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"beginDeviceRegistrationUsingLoginManager:options:completion:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"Q"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"q"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"beginHandlingWebAuthenticationSessionRequest:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"beginUserRegistrationUsingLoginManager:userName:authenticationMethod:options:completion:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"q"},
                5: {"type": b"Q"},
                6: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"q"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"cancelAuthorizationWithRequest:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"cancelWebAuthenticationSessionRequest:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"challenge", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"credentialID", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"displayName", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"name", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"presentationAnchorForAccountAuthenticationModificationController:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"presentationAnchorForAuthorizationController:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"presentationAnchorForWebAuthenticationSession:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"rawAttestationObject",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"rawAuthenticatorData",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(b"NSObject", b"rawClientDataJSON", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"registrationDidComplete",
        {"required": False, "retval": {"type": b"v"}},
    )
    r(
        b"NSObject",
        b"relyingPartyIdentifier",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"setAllowedCredentials:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setAttestationPreference:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setChallenge:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setCredentialID:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setDisplayName:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setName:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setRelyingPartyIdentifier:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setUserID:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setUserVerificationPreference:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"signature", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"userID", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"userVerificationPreference",
        {"required": True, "retval": {"type": b"@"}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
