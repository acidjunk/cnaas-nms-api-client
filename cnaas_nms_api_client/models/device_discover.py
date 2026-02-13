from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeviceDiscover")


@_attrs_define
class DeviceDiscover:
    """
    Attributes:
        ztp_mac (str):
        dhcp_ip (str):
    """

    ztp_mac: str
    dhcp_ip: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ztp_mac = self.ztp_mac

        dhcp_ip = self.dhcp_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ztp_mac": ztp_mac,
                "dhcp_ip": dhcp_ip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ztp_mac = d.pop("ztp_mac")

        dhcp_ip = d.pop("dhcp_ip")

        device_discover = cls(
            ztp_mac=ztp_mac,
            dhcp_ip=dhcp_ip,
        )

        device_discover.additional_properties = d
        return device_discover

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
