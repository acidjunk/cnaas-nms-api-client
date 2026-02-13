""" Contains all the data models used in inputs/outputs """

from .delete_devcie import DeleteDevcie
from .device import Device
from .device_apply_config import DeviceApplyConfig
from .device_cert import DeviceCert
from .device_discover import DeviceDiscover
from .device_init import DeviceInit
from .device_initcheck import DeviceInitcheck
from .device_restore import DeviceRestore
from .device_sync import DeviceSync
from .device_update_facts import DeviceUpdateFacts
from .device_update_interfaces import DeviceUpdateInterfaces
from .firmware_download import FirmwareDownload
from .firmware_upgrade import FirmwareUpgrade
from .generate_config import GenerateConfig
from .generate_config_available_variables import GenerateConfigAvailableVariables
from .jobs import Jobs
from .linknet import Linknet
from .linknets import Linknets
from .mgmtdomain import Mgmtdomain
from .plugin import Plugin
from .repository import Repository
from .stackmember import Stackmember
from .stackmembers import Stackmembers

__all__ = (
    "DeleteDevcie",
    "Device",
    "DeviceApplyConfig",
    "DeviceCert",
    "DeviceDiscover",
    "DeviceInit",
    "DeviceInitcheck",
    "DeviceRestore",
    "DeviceSync",
    "DeviceUpdateFacts",
    "DeviceUpdateInterfaces",
    "FirmwareDownload",
    "FirmwareUpgrade",
    "GenerateConfig",
    "GenerateConfigAvailableVariables",
    "Jobs",
    "Linknet",
    "Linknets",
    "Mgmtdomain",
    "Plugin",
    "Repository",
    "Stackmember",
    "Stackmembers",
)
