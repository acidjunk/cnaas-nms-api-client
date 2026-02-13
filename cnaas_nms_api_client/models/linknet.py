from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Linknet")


@_attrs_define
class Linknet:
    """
    Attributes:
        device_a (Union[Unset, str]):
        device_b (Union[Unset, str]):
        device_a_port (Union[Unset, str]):
        device_b_port (Union[Unset, str]):
        ipv4_network (Union[Unset, str]):
        device_a_ip (Union[Unset, str]):
        device_b_ip (Union[Unset, str]):
    """

    device_a: Unset | str = UNSET
    device_b: Unset | str = UNSET
    device_a_port: Unset | str = UNSET
    device_b_port: Unset | str = UNSET
    ipv4_network: Unset | str = UNSET
    device_a_ip: Unset | str = UNSET
    device_b_ip: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_a = self.device_a

        device_b = self.device_b

        device_a_port = self.device_a_port

        device_b_port = self.device_b_port

        ipv4_network = self.ipv4_network

        device_a_ip = self.device_a_ip

        device_b_ip = self.device_b_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_a is not UNSET:
            field_dict["device_a"] = device_a
        if device_b is not UNSET:
            field_dict["device_b"] = device_b
        if device_a_port is not UNSET:
            field_dict["device_a_port"] = device_a_port
        if device_b_port is not UNSET:
            field_dict["device_b_port"] = device_b_port
        if ipv4_network is not UNSET:
            field_dict["ipv4_network"] = ipv4_network
        if device_a_ip is not UNSET:
            field_dict["device_a_ip"] = device_a_ip
        if device_b_ip is not UNSET:
            field_dict["device_b_ip"] = device_b_ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_a = d.pop("device_a", UNSET)

        device_b = d.pop("device_b", UNSET)

        device_a_port = d.pop("device_a_port", UNSET)

        device_b_port = d.pop("device_b_port", UNSET)

        ipv4_network = d.pop("ipv4_network", UNSET)

        device_a_ip = d.pop("device_a_ip", UNSET)

        device_b_ip = d.pop("device_b_ip", UNSET)

        linknet = cls(
            device_a=device_a,
            device_b=device_b,
            device_a_port=device_a_port,
            device_b_port=device_b_port,
            ipv4_network=ipv4_network,
            device_a_ip=device_a_ip,
            device_b_ip=device_b_ip,
        )

        linknet.additional_properties = d
        return linknet

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
