from enum import Enum
from struct import *

LAYOUT_LINE_LENGTH = 80
MAX_SECTIONS = 9


class FirmwareDescriptor:
    def __init__(self, data: bytes):
        self._data = data

    def regions(self):
        pass

class FirmwareRegion:
    pass


class FirmwareDescriptorVersion(Enum):
    VERSION_1 = 1
    VERSION_2 = 2


class FirmwareDescriptorPlatform(Enum):
    PLATFORM_APL = 0
    PLATFORM_CNL = 1
    PLATFORM_GLK = 2
    PLATFORM_SKLKBL = 3


class FirmwareDescriptorSpiFrequency(Enum):
    SPI_FREQUENCY_20MHZ = 0,
    SPI_FREQUENCY_33MHZ = 1,
    SPI_FREQUENCY_48MHZ = 2,
    SPI_FREQUENCY_50MHZ_30MHZ = 4,
    SPI_FREQUENCY_17MHZ = 6,


class FirmwareDescriptorComponentDensity(Enum):
    COMPONENT_DENSITY_512KB = 0,
    COMPONENT_DENSITY_1MB = 1,
    COMPONENT_DENSITY_2MB = 2,
    COMPONENT_DENSITY_4MB = 3,
    COMPONENT_DENSITY_8MB = 4,
    COMPONENT_DENSITY_16MB = 5,
    COMPONENT_DENSITY_32MB = 6,
    COMPONENT_DENSITY_64MB = 7,
    COMPONENT_DENSITY_UNUSED = 0xf
