from PyObjCTools.TestSupport import *

import Metal

class TestMTLSampler (TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLSamplerMinMagFilterNearest, 0)
        self.assertEqual(Metal.MTLSamplerMinMagFilterLinear, 1)
        self.assertEqual(Metal.MTLSamplerMipFilterNotMipmapped, 0)
        self.assertEqual(Metal.MTLSamplerMipFilterNearest, 1)
        self.assertEqual(Metal.MTLSamplerMipFilterLinear, 2)
        self.assertEqual(Metal.MTLSamplerAddressModeClampToEdge, 0)
        self.assertEqual(Metal.MTLSamplerAddressModeMirrorClampToEdge, 1)
        self.assertEqual(Metal.MTLSamplerAddressModeRepeat, 2)
        self.assertEqual(Metal.MTLSamplerAddressModeMirrorRepeat, 3)
        self.assertEqual(Metal.MTLSamplerAddressModeClampToZero, 4)
        self.assertEqual(Metal.MTLSamplerAddressModeClampToBorderColor, 5)
        self.assertEqual(Metal.MTLSamplerBorderColorTransparentBlack, 0)
        self.assertEqual(Metal.MTLSamplerBorderColorOpaqueBlack, 1)
        self.assertEqual(Metal.MTLSamplerBorderColorOpaqueWhite, 2)

    @min_sdk_level('10.11')
    def test_protocols(self):
        objc.protocolNamed('MTLSamplerState')


    @min_os_level('10.11')
    def test_methods10_11(self):
        self.assertResultIsBOOL(Metal.MTLSamplerDescriptor.normalizedCoordinates)
        self.assertArgIsBOOL(Metal.MTLSamplerDescriptor.setNormalizedCoordinates_, 0)

    @min_os_level('10.13')
    def test_methods10_13(self):
        self.assertResultIsBOOL(Metal.MTLSamplerDescriptor.supportArgumentBuffers)
        self.assertArgIsBOOL(Metal.MTLSamplerDescriptor.setSupportArgumentBuffers_, 0)
