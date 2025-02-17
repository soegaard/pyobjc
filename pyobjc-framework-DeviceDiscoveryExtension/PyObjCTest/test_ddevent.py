from PyObjCTools.TestSupport import TestCase
import DeviceDiscoveryExtension


class TestDDEvent(TestCase):
    def test_constants(self):
        self.assertIsEnumType(DeviceDiscoveryExtension.DDEventType)
        self.assertEqual(DeviceDiscoveryExtension.DDEventTypeUnknown, 0)
        self.assertEqual(DeviceDiscoveryExtension.DDEventTypeDeviceFound, 40)
        self.assertEqual(DeviceDiscoveryExtension.DDEventTypeDeviceLost, 41)
        self.assertEqual(DeviceDiscoveryExtension.DDEventTypeDeviceChanged, 42)
        self.assertEqual(DeviceDiscoveryExtension.DDEventTypeDevicesPresentChanged, 50)

    def test_functions(self):
        DeviceDiscoveryExtension.DDEventTypeToString

    def test_methods(self):
        self.assertResultIsBOOL(
            DeviceDiscoveryExtension.DDEventDevicesPresent.devicesPresent
        )
