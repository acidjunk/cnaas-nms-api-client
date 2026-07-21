from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interfacedata import Interfacedata


T = TypeVar("T", bound="Interface")


@_attrs_define
class Interface:
    """
    Attributes:
        configtype (str): Type of interface, can be: ACCESS_AUTO, ACCESS_UNTAGGED, ACCESS_TAGGED, ACCESS_UPLINK,
            ACCESS_DOWNLINK, MLAG_PEER Example: ACCESS_AUTO.
        data (Union[Unset, Interfacedata]):
    """

    configtype: str
    data: Union[Unset, "Interfacedata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configtype = self.configtype

        data: Unset | dict[str, Any] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configtype": configtype,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interfacedata import Interfacedata

        d = dict(src_dict)
        configtype = d.pop("configtype")

        _data = d.pop("data", UNSET)
        data: Unset | Interfacedata
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = Interfacedata.from_dict(_data)

        interface = cls(
            configtype=configtype,
            data=data,
        )

        interface.additional_properties = d
        return interface

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
