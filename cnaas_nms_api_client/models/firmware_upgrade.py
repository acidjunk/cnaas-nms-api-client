from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FirmwareUpgrade")


@_attrs_define
class FirmwareUpgrade:
    """
    Attributes:
        url (str):
        start_at (Union[Unset, str]):
        download (Union[Unset, bool]):
        activate (Union[Unset, bool]):
        filename (Union[Unset, str]):
        group (Union[Unset, str]):
        hostname (Union[Unset, str]):
        pre_flight (Union[Unset, bool]):
        post_flight (Union[Unset, bool]):  Default: False.
        post_waittime (Union[Unset, int]):  Default: 600.
        reboot (Union[Unset, bool]):  Default: False.
        staggered_upgrade (Union[Unset, bool]):  Default: False.
    """

    url: str
    start_at: Unset | str = UNSET
    download: Unset | bool = UNSET
    activate: Unset | bool = UNSET
    filename: Unset | str = UNSET
    group: Unset | str = UNSET
    hostname: Unset | str = UNSET
    pre_flight: Unset | bool = UNSET
    post_flight: Unset | bool = False
    post_waittime: Unset | int = 600
    reboot: Unset | bool = False
    staggered_upgrade: Unset | bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        start_at = self.start_at

        download = self.download

        activate = self.activate

        filename = self.filename

        group = self.group

        hostname = self.hostname

        pre_flight = self.pre_flight

        post_flight = self.post_flight

        post_waittime = self.post_waittime

        reboot = self.reboot

        staggered_upgrade = self.staggered_upgrade

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if download is not UNSET:
            field_dict["download"] = download
        if activate is not UNSET:
            field_dict["activate"] = activate
        if filename is not UNSET:
            field_dict["filename"] = filename
        if group is not UNSET:
            field_dict["group"] = group
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if pre_flight is not UNSET:
            field_dict["pre_flight"] = pre_flight
        if post_flight is not UNSET:
            field_dict["post_flight"] = post_flight
        if post_waittime is not UNSET:
            field_dict["post_waittime"] = post_waittime
        if reboot is not UNSET:
            field_dict["reboot"] = reboot
        if staggered_upgrade is not UNSET:
            field_dict["staggered_upgrade"] = staggered_upgrade

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        start_at = d.pop("start_at", UNSET)

        download = d.pop("download", UNSET)

        activate = d.pop("activate", UNSET)

        filename = d.pop("filename", UNSET)

        group = d.pop("group", UNSET)

        hostname = d.pop("hostname", UNSET)

        pre_flight = d.pop("pre_flight", UNSET)

        post_flight = d.pop("post_flight", UNSET)

        post_waittime = d.pop("post_waittime", UNSET)

        reboot = d.pop("reboot", UNSET)

        staggered_upgrade = d.pop("staggered_upgrade", UNSET)

        firmware_upgrade = cls(
            url=url,
            start_at=start_at,
            download=download,
            activate=activate,
            filename=filename,
            group=group,
            hostname=hostname,
            pre_flight=pre_flight,
            post_flight=post_flight,
            post_waittime=post_waittime,
            reboot=reboot,
            staggered_upgrade=staggered_upgrade,
        )

        firmware_upgrade.additional_properties = d
        return firmware_upgrade

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
