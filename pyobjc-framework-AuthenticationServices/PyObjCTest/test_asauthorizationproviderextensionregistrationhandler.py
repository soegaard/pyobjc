import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestASAuthorizationProviderExtensionRegistrationHandlerHelper(
    AuthenticationServices.NSObject
):
    def beginDeviceRegistrationUsingLoginManager_options_completion_(self, a, b, c):
        pass

    def beginUserRegistrationUsingLoginManager_userName_authenticationMethod_options_completion_(
        self, a, b, c, d, e
    ):
        pass


class TestASAuthorizationProviderExtensionRegistrationHandler(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            AuthenticationServices.ASAuthorizationProviderExtensionAuthenticationMethod
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionAuthenticationMethodPassword,
            1,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionAuthenticationMethodUserSecureEnclaveKey,
            2,
        )

        self.assertIsEnumType(
            AuthenticationServices.ASAuthorizationProviderExtensionRequestOptions
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionRequestOptionsNone, 0
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionRequestOptionsUserInteractionEnabled,
            1 << 0,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionRequestOptionsRegistrationRepair,
            1 << 1,
        )

        self.assertIsEnumType(
            AuthenticationServices.ASAuthorizationProviderExtensionRegistrationResult
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionRegistrationResultSuccess,
            0,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionRegistrationResultFailed,
            1,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionRegistrationResultUserInterfaceRequired,
            2,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionRegistrationResultFailedNoRetry,
            3,
        )

    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("ASAuthorizationProviderExtensionRegistrationHandler")

    def test_methods(self):
        self.assertArgHasType(
            TestASAuthorizationProviderExtensionRegistrationHandlerHelper.beginDeviceRegistrationUsingLoginManager_options_completion_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestASAuthorizationProviderExtensionRegistrationHandlerHelper.beginDeviceRegistrationUsingLoginManager_options_completion_,
            2,
            b"v" + objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestASAuthorizationProviderExtensionRegistrationHandlerHelper.beginUserRegistrationUsingLoginManager_userName_authenticationMethod_options_completion_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestASAuthorizationProviderExtensionRegistrationHandlerHelper.beginUserRegistrationUsingLoginManager_userName_authenticationMethod_options_completion_,
            3,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestASAuthorizationProviderExtensionRegistrationHandlerHelper.beginUserRegistrationUsingLoginManager_userName_authenticationMethod_options_completion_,
            4,
            b"v" + objc._C_NSInteger,
        )
