from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphResizeOps(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphResizeMode)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphResizeNearest, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphResizeBilinear, 1)

    def test_methods(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeTensor_size_mode_centerResult_alignCorners_layout_name_,
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeTensor_size_mode_centerResult_alignCorners_layout_name_,
            4,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeWithGradientTensor_input_mode_centerResult_alignCorners_layout_name_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeWithGradientTensor_input_mode_centerResult_alignCorners_layout_name_,  # noqa: B950
            4,
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeTensor_sizeTensor_mode_centerResult_alignCorners_layout_name_,
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeTensor_sizeTensor_mode_centerResult_alignCorners_layout_name_,
            4,
        )
