import libdispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestWorkloop(TestCase):
    @min_os_level("10.14")
    def test_functions(self):
        self.assertResultHasType(libdispatch.dispatch_workloop_create, objc._C_ID)
        self.assertResultIsRetained(libdispatch.dispatch_workloop_create)
        self.assertArgHasType(
            libdispatch.dispatch_workloop_create, 0, b"n^" + objc._C_CHAR_AS_TEXT
        )
        self.assertArgIsNullTerminated(libdispatch.dispatch_workloop_create, 0)

        self.assertResultHasType(
            libdispatch.dispatch_workloop_create_inactive, objc._C_ID
        )
        self.assertResultIsRetained(libdispatch.dispatch_workloop_create_inactive)
        self.assertArgHasType(
            libdispatch.dispatch_workloop_create_inactive,
            0,
            b"n^" + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(libdispatch.dispatch_workloop_create_inactive, 0)

        self.assertResultHasType(
            libdispatch.dispatch_workloop_set_autorelease_frequency, objc._C_VOID
        )
        self.assertArgHasType(
            libdispatch.dispatch_workloop_set_autorelease_frequency, 0, objc._C_ID
        )
        self.assertArgHasType(
            libdispatch.dispatch_workloop_set_autorelease_frequency, 1, objc._C_ULNG
        )

    @min_os_level("11.0")
    def test_functions11_0(self):
        self.assertResultHasType(
            libdispatch.dispatch_workloop_set_os_workgroup, objc._C_VOID
        )
        self.assertArgHasType(
            libdispatch.dispatch_workloop_set_os_workgroup, 0, objc._C_ID
        )
        self.assertArgHasType(
            libdispatch.dispatch_workloop_set_os_workgroup, 1, objc._C_ID
        )
