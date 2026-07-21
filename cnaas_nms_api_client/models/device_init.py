from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceInit")


@_attrs_define
class DeviceInit:
    """
    Attributes:
        hostname (Union[Unset, str]):
        device_type (Union[Unset, str]):
        replace_hostname (Union[Unset, bool]): This device id should replace old device with specified hostname Default:
            False.
    """

    hostname: Unset | str = UNSET
    device_type: Unset | str = UNSET
    replace_hostname: Unset | bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        device_type = self.device_type

        replace_hostname = self.replace_hostname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if replace_hostname is not UNSET:
            field_dict["replace_hostname"] = replace_hostname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hostname = d.pop("hostname", UNSET)

        device_type = d.pop("device_type", UNSET)

        replace_hostname = d.pop("replace_hostname", UNSET)

        device_init = cls(
            hostname=hostname,
            device_type=device_type,
            replace_hostname=replace_hostname,
        )

        device_init.additional_properties = d
        return device_init

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
