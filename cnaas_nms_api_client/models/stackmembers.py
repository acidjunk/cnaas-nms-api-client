from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stackmember import Stackmember


T = TypeVar("T", bound="Stackmembers")


@_attrs_define
class Stackmembers:
    """
    Attributes:
        stackmembers (Union[Unset, list['Stackmember']]):
    """

    stackmembers: Unset | list["Stackmember"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stackmembers: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.stackmembers, Unset):
            stackmembers = []
            for stackmembers_item_data in self.stackmembers:
                stackmembers_item = stackmembers_item_data.to_dict()
                stackmembers.append(stackmembers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stackmembers is not UNSET:
            field_dict["stackmembers"] = stackmembers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stackmember import Stackmember

        d = dict(src_dict)
        stackmembers = []
        _stackmembers = d.pop("stackmembers", UNSET)
        for stackmembers_item_data in _stackmembers or []:
            stackmembers_item = Stackmember.from_dict(stackmembers_item_data)

            stackmembers.append(stackmembers_item)

        stackmembers = cls(
            stackmembers=stackmembers,
        )

        stackmembers.additional_properties = d
        return stackmembers

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
