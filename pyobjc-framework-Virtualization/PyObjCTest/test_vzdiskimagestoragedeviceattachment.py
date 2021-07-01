from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZDiskImageStorageDeviceAttachment(TestCase):
    def test_constants(self):
        self.assertEqual(Virtualization.VZDiskImageSynchronizationModeFull, 1)
        self.assertEqual(Virtualization.VZDiskImageSynchronizationModeFsync, 2)
        self.assertEqual(Virtualization.VZDiskImageSynchronizationModeNone, 3)

    def test_methods(self):
        self.assertArgIsBOOL(
            Virtualization.VZDiskImageStorageDeviceAttachment.initWithURL_readOnly_error_,
            1,
        )
        self.assertArgIsOut(
            Virtualization.VZDiskImageStorageDeviceAttachment.initWithURL_readOnly_error_,
            2,
        )
        self.assertResultIsBOOL(
            Virtualization.VZDiskImageStorageDeviceAttachment.isReadOnly
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBOOL(
            Virtualization.VZDiskImageStorageDeviceAttachment.initWithURL_readOnly_synchronizationMode_error_,
            1,
        )
        self.assertArgIsOut(
            Virtualization.VZDiskImageStorageDeviceAttachment.initWithURL_readOnly_synchronizationMode_error_,
            3,
        )
