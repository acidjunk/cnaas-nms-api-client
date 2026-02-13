from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Linknets")



@_attrs_define
class Linknets:
    """ 
        Attributes:
            device_a (str):
            device_b (str):
            device_a_port (str):
            device_b_port (str):
            ipv4_network (Union[Unset, str]):
     """

    device_a: str
    device_b: str
    device_a_port: str
    device_b_port: str
    ipv4_network: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        device_a = self.device_a

        device_b = self.device_b

        device_a_port = self.device_a_port

        device_b_port = self.device_b_port

        ipv4_network = self.ipv4_network


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "device_a": device_a,
            "device_b": device_b,
            "device_a_port": device_a_port,
            "device_b_port": device_b_port,
        })
        if ipv4_network is not UNSET:
            field_dict["ipv4_network"] = ipv4_network

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_a = d.pop("device_a")

        device_b = d.pop("device_b")

        device_a_port = d.pop("device_a_port")

        device_b_port = d.pop("device_b_port")

        ipv4_network = d.pop("ipv4_network", UNSET)

        linknets = cls(
            device_a=device_a,
            device_b=device_b,
            device_a_port=device_a_port,
            device_b_port=device_b_port,
            ipv4_network=ipv4_network,
        )


        linknets.additional_properties = d
        return linknets

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
