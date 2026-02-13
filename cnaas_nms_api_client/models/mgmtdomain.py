from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Mgmtdomain")


@_attrs_define
class Mgmtdomain:
    """
    Attributes:
        device_a (str):
        device_b (str):
        vlan (int):
        ipv4_gw (str):
        ipv6_gw (str):
        description (Union[Unset, str]):
    """

    device_a: str
    device_b: str
    vlan: int
    ipv4_gw: str
    ipv6_gw: str
    description: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_a = self.device_a

        device_b = self.device_b

        vlan = self.vlan

        ipv4_gw = self.ipv4_gw

        ipv6_gw = self.ipv6_gw

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "device_a": device_a,
                "device_b": device_b,
                "vlan": vlan,
                "ipv4_gw": ipv4_gw,
                "ipv6_gw": ipv6_gw,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_a = d.pop("device_a")

        device_b = d.pop("device_b")

        vlan = d.pop("vlan")

        ipv4_gw = d.pop("ipv4_gw")

        ipv6_gw = d.pop("ipv6_gw")

        description = d.pop("description", UNSET)

        mgmtdomain = cls(
            device_a=device_a,
            device_b=device_b,
            vlan=vlan,
            ipv4_gw=ipv4_gw,
            ipv6_gw=ipv6_gw,
            description=description,
        )

        mgmtdomain.additional_properties = d
        return mgmtdomain

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
