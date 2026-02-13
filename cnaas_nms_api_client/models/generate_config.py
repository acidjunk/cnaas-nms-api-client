from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.generate_config_available_variables import GenerateConfigAvailableVariables





T = TypeVar("T", bound="GenerateConfig")



@_attrs_define
class GenerateConfig:
    """ 
        Attributes:
            hostname (Union[Unset, str]):
            generated_config (Union[Unset, str]):
            available_variables (Union[Unset, GenerateConfigAvailableVariables]):
     """

    hostname: Union[Unset, str] = UNSET
    generated_config: Union[Unset, str] = UNSET
    available_variables: Union[Unset, 'GenerateConfigAvailableVariables'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_config_available_variables import GenerateConfigAvailableVariables
        hostname = self.hostname

        generated_config = self.generated_config

        available_variables: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.available_variables, Unset):
            available_variables = self.available_variables.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if generated_config is not UNSET:
            field_dict["generated_config"] = generated_config
        if available_variables is not UNSET:
            field_dict["available_variables"] = available_variables

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_config_available_variables import GenerateConfigAvailableVariables
        d = dict(src_dict)
        hostname = d.pop("hostname", UNSET)

        generated_config = d.pop("generated_config", UNSET)

        _available_variables = d.pop("available_variables", UNSET)
        available_variables: Union[Unset, GenerateConfigAvailableVariables]
        if isinstance(_available_variables,  Unset):
            available_variables = UNSET
        else:
            available_variables = GenerateConfigAvailableVariables.from_dict(_available_variables)




        generate_config = cls(
            hostname=hostname,
            generated_config=generated_config,
            available_variables=available_variables,
        )


        generate_config.additional_properties = d
        return generate_config

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
