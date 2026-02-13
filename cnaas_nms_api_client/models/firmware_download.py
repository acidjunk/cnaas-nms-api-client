from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FirmwareDownload")


@_attrs_define
class FirmwareDownload:
    """
    Attributes:
        url (str):
        sha1 (str):
        filename (str):
        verify_tls (Union[Unset, bool]):
    """

    url: str
    sha1: str
    filename: str
    verify_tls: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        sha1 = self.sha1

        filename = self.filename

        verify_tls = self.verify_tls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "sha1": sha1,
                "filename": filename,
            }
        )
        if verify_tls is not UNSET:
            field_dict["verify_tls"] = verify_tls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        sha1 = d.pop("sha1")

        filename = d.pop("filename")

        verify_tls = d.pop("verify_tls", UNSET)

        firmware_download = cls(
            url=url,
            sha1=sha1,
            filename=filename,
            verify_tls=verify_tls,
        )

        firmware_download.additional_properties = d
        return firmware_download

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
