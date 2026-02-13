from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Stackmember")



@_attrs_define
class Stackmember:
    """ 
        Attributes:
            hardware_id (str):
            member_no (Union[Unset, int]):
            priority_id (Union[Unset, int]):
     """

    hardware_id: str
    member_no: Union[Unset, int] = UNSET
    priority_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hardware_id = self.hardware_id

        member_no = self.member_no

        priority_id = self.priority_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "hardware_id": hardware_id,
        })
        if member_no is not UNSET:
            field_dict["member_no"] = member_no
        if priority_id is not UNSET:
            field_dict["priority_id"] = priority_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hardware_id = d.pop("hardware_id")

        member_no = d.pop("member_no", UNSET)

        priority_id = d.pop("priority_id", UNSET)

        stackmember = cls(
            hardware_id=hardware_id,
            member_no=member_no,
            priority_id=priority_id,
        )


        stackmember.additional_properties = d
        return stackmember

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
