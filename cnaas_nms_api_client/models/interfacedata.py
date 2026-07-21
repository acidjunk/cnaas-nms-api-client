from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interfacedata_tagged_vlan_list_item import InterfacedataTaggedVlanListItem
    from ..models.interfacedata_untagged_vlan import InterfacedataUntaggedVlan


T = TypeVar("T", bound="Interfacedata")


@_attrs_define
class Interfacedata:
    """
    Attributes:
        untagged_vlan (Union[Unset, InterfacedataUntaggedVlan]): VLAN ID or name Example: STUDENTS.
        tagged_vlan_list (Union[Unset, list['InterfacedataTaggedVlanListItem']]): List of VLAN IDs or names Example:
            ['STUDENTS', 'EMPLOYEES'].
        description (Union[Unset, str]): Interface description Example: Access point.
        enabled (Union[Unset, bool]):  Example: True.
        aggregate_id (Union[Unset, int]): LACP ID Example: -1.
        bpdu_filter (Union[Unset, bool]):  Example: True.
        redundant_link (Union[Unset, bool]):  Example: True.
        tags (Union[Unset, list[str]]): List of tags Example: ['tag1', 'tag2'].
        cli_append_str (Union[Unset, str]):
    """

    untagged_vlan: Union[Unset, "InterfacedataUntaggedVlan"] = UNSET
    tagged_vlan_list: Unset | list["InterfacedataTaggedVlanListItem"] = UNSET
    description: Unset | str = UNSET
    enabled: Unset | bool = UNSET
    aggregate_id: Unset | int = UNSET
    bpdu_filter: Unset | bool = UNSET
    redundant_link: Unset | bool = UNSET
    tags: Unset | list[str] = UNSET
    cli_append_str: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        untagged_vlan: Unset | dict[str, Any] = UNSET
        if not isinstance(self.untagged_vlan, Unset):
            untagged_vlan = self.untagged_vlan.to_dict()

        tagged_vlan_list: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.tagged_vlan_list, Unset):
            tagged_vlan_list = []
            for tagged_vlan_list_item_data in self.tagged_vlan_list:
                tagged_vlan_list_item = tagged_vlan_list_item_data.to_dict()
                tagged_vlan_list.append(tagged_vlan_list_item)

        description = self.description

        enabled = self.enabled

        aggregate_id = self.aggregate_id

        bpdu_filter = self.bpdu_filter

        redundant_link = self.redundant_link

        tags: Unset | list[str] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        cli_append_str = self.cli_append_str

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if untagged_vlan is not UNSET:
            field_dict["untagged_vlan"] = untagged_vlan
        if tagged_vlan_list is not UNSET:
            field_dict["tagged_vlan_list"] = tagged_vlan_list
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if aggregate_id is not UNSET:
            field_dict["aggregate_id"] = aggregate_id
        if bpdu_filter is not UNSET:
            field_dict["bpdu_filter"] = bpdu_filter
        if redundant_link is not UNSET:
            field_dict["redundant_link"] = redundant_link
        if tags is not UNSET:
            field_dict["tags"] = tags
        if cli_append_str is not UNSET:
            field_dict["cli_append_str"] = cli_append_str

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interfacedata_tagged_vlan_list_item import InterfacedataTaggedVlanListItem
        from ..models.interfacedata_untagged_vlan import InterfacedataUntaggedVlan

        d = dict(src_dict)
        _untagged_vlan = d.pop("untagged_vlan", UNSET)
        untagged_vlan: Unset | InterfacedataUntaggedVlan
        if isinstance(_untagged_vlan, Unset):
            untagged_vlan = UNSET
        else:
            untagged_vlan = InterfacedataUntaggedVlan.from_dict(_untagged_vlan)

        tagged_vlan_list = []
        _tagged_vlan_list = d.pop("tagged_vlan_list", UNSET)
        for tagged_vlan_list_item_data in _tagged_vlan_list or []:
            tagged_vlan_list_item = InterfacedataTaggedVlanListItem.from_dict(tagged_vlan_list_item_data)

            tagged_vlan_list.append(tagged_vlan_list_item)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        aggregate_id = d.pop("aggregate_id", UNSET)

        bpdu_filter = d.pop("bpdu_filter", UNSET)

        redundant_link = d.pop("redundant_link", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        cli_append_str = d.pop("cli_append_str", UNSET)

        interfacedata = cls(
            untagged_vlan=untagged_vlan,
            tagged_vlan_list=tagged_vlan_list,
            description=description,
            enabled=enabled,
            aggregate_id=aggregate_id,
            bpdu_filter=bpdu_filter,
            redundant_link=redundant_link,
            tags=tags,
            cli_append_str=cli_append_str,
        )

        interfacedata.additional_properties = d
        return interfacedata

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
