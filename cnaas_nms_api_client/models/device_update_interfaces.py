from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceUpdateInterfaces")


@_attrs_define
class DeviceUpdateInterfaces:
    """
    Attributes:
        hostname (str):
        replace (Union[Unset, bool]):
        delete_all (Union[Unset, bool]):
    """

    hostname: str
    replace: Unset | bool = UNSET
    delete_all: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        replace = self.replace

        delete_all = self.delete_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
            }
        )
        if replace is not UNSET:
            field_dict["replace"] = replace
        if delete_all is not UNSET:
            field_dict["delete_all"] = delete_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hostname = d.pop("hostname")

        replace = d.pop("replace", UNSET)

        delete_all = d.pop("delete_all", UNSET)

        device_update_interfaces = cls(
            hostname=hostname,
            replace=replace,
            delete_all=delete_all,
        )

        device_update_interfaces.additional_properties = d
        return device_update_interfaces

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
