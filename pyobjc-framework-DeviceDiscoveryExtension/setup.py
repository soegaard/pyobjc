"""
Wrappers for the "DeviceDiscoveryExtension" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup

VERSION = "9.0a1"

setup(
    name="pyobjc-framework-DeviceDiscoveryExtension",
    description="Wrappers for the framework DeviceDiscoveryExtension on macOS",
    min_os_level="13.0",
    packages=["DeviceDiscoveryExtension"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
    ],
    long_description=__doc__,
)
