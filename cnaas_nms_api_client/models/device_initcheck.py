from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceInitcheck")


@_attrs_define
class DeviceInitcheck:
    """
    Attributes:
        hostname (str):
        device_type (str):
        mlag_peer_id (Union[Unset, int]):
        mlag_peer_hostname (Union[Unset, str]):
    """

    hostname: str
    device_type: str
    mlag_peer_id: Unset | int = UNSET
    mlag_peer_hostname: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        device_type = self.device_type

        mlag_peer_id = self.mlag_peer_id

        mlag_peer_hostname = self.mlag_peer_hostname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
                "device_type": device_type,
            }
        )
        if mlag_peer_id is not UNSET:
            field_dict["mlag_peer_id"] = mlag_peer_id
        if mlag_peer_hostname is not UNSET:
            field_dict["mlag_peer_hostname"] = mlag_peer_hostname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hostname = d.pop("hostname")

        device_type = d.pop("device_type")

        mlag_peer_id = d.pop("mlag_peer_id", UNSET)

        mlag_peer_hostname = d.pop("mlag_peer_hostname", UNSET)

        device_initcheck = cls(
            hostname=hostname,
            device_type=device_type,
            mlag_peer_id=mlag_peer_id,
            mlag_peer_hostname=mlag_peer_hostname,
        )

        device_initcheck.additional_properties = d
        return device_initcheck

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
