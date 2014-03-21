'''
Wrappers for the "CoreWLAN" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup

setup(
    name='pyobjc-framework-CoreWLAN',
    version="3.0",
    description = "Wrappers for the framework CoreWLAN on Mac OS X",
    packages = [ "CoreWLAN" ],
    setup_requires = [
        'pyobjc-core>=3.0',
    ],
    install_requires = [
        'pyobjc-core>=3.0',
        'pyobjc-framework-Cocoa>=3.0',
    ],
    min_os_level="10.6",
)