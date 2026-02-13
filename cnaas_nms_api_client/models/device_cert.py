from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceCert")


@_attrs_define
class DeviceCert:
    """
    Attributes:
        action (str): Action to execute, one of: RENEW Example: RENEW.
        hostname (Union[Unset, str]): Device hostname Example: myhostname.
        group (Union[Unset, str]): Device group Example: mygroup.
    """

    action: str
    hostname: Unset | str = UNSET
    group: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        hostname = self.hostname

        group = self.group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        hostname = d.pop("hostname", UNSET)

        group = d.pop("group", UNSET)

        device_cert = cls(
            action=action,
            hostname=hostname,
            group=group,
        )

        device_cert.additional_properties = d
        return device_cert

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
