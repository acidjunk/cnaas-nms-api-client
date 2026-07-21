from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceHostnameSync")


@_attrs_define
class DeviceHostnameSync:
    """
    Attributes:
        dry_run (Union[Unset, bool]):
        force (Union[Unset, bool]):
        auto_push (Union[Unset, bool]):
        resync (Union[Unset, bool]):
        confirm_mode (Union[Unset, int]):
    """

    dry_run: Unset | bool = UNSET
    force: Unset | bool = UNSET
    auto_push: Unset | bool = UNSET
    resync: Unset | bool = UNSET
    confirm_mode: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run

        force = self.force

        auto_push = self.auto_push

        resync = self.resync

        confirm_mode = self.confirm_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if force is not UNSET:
            field_dict["force"] = force
        if auto_push is not UNSET:
            field_dict["auto_push"] = auto_push
        if resync is not UNSET:
            field_dict["resync"] = resync
        if confirm_mode is not UNSET:
            field_dict["confirm_mode"] = confirm_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dry_run = d.pop("dry_run", UNSET)

        force = d.pop("force", UNSET)

        auto_push = d.pop("auto_push", UNSET)

        resync = d.pop("resync", UNSET)

        confirm_mode = d.pop("confirm_mode", UNSET)

        device_hostname_sync = cls(
            dry_run=dry_run,
            force=force,
            auto_push=auto_push,
            resync=resync,
            confirm_mode=confirm_mode,
        )

        device_hostname_sync.additional_properties = d
        return device_hostname_sync

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
