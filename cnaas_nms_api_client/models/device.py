from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Device")



@_attrs_define
class Device:
    """ 
        Attributes:
            hostname (str):
            platform (str):
            state (str):
            device_type (str):
            site_id (Union[Unset, int]):
            description (Union[Unset, str]):
            management_ip (Union[Unset, str]):
            infra_ip (Union[Unset, str]):
            dhcp_ip (Union[Unset, str]):
            serial (Union[Unset, str]):
            ztp_mac (Union[Unset, str]):
            vendor (Union[Unset, str]):
            model (Union[Unset, str]):
            os_version (Union[Unset, str]):
            synchronized (Union[Unset, bool]):
            port (Union[Unset, int]):
     """

    hostname: str
    platform: str
    state: str
    device_type: str
    site_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    management_ip: Union[Unset, str] = UNSET
    infra_ip: Union[Unset, str] = UNSET
    dhcp_ip: Union[Unset, str] = UNSET
    serial: Union[Unset, str] = UNSET
    ztp_mac: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    os_version: Union[Unset, str] = UNSET
    synchronized: Union[Unset, bool] = UNSET
    port: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        platform = self.platform

        state = self.state

        device_type = self.device_type

        site_id = self.site_id

        description = self.description

        management_ip = self.management_ip

        infra_ip = self.infra_ip

        dhcp_ip = self.dhcp_ip

        serial = self.serial

        ztp_mac = self.ztp_mac

        vendor = self.vendor

        model = self.model

        os_version = self.os_version

        synchronized = self.synchronized

        port = self.port


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "hostname": hostname,
            "platform": platform,
            "state": state,
            "device_type": device_type,
        })
        if site_id is not UNSET:
            field_dict["site_id"] = site_id
        if description is not UNSET:
            field_dict["description"] = description
        if management_ip is not UNSET:
            field_dict["management_ip"] = management_ip
        if infra_ip is not UNSET:
            field_dict["infra_ip"] = infra_ip
        if dhcp_ip is not UNSET:
            field_dict["dhcp_ip"] = dhcp_ip
        if serial is not UNSET:
            field_dict["serial"] = serial
        if ztp_mac is not UNSET:
            field_dict["ztp_mac"] = ztp_mac
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if model is not UNSET:
            field_dict["model"] = model
        if os_version is not UNSET:
            field_dict["os_version"] = os_version
        if synchronized is not UNSET:
            field_dict["synchronized"] = synchronized
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hostname = d.pop("hostname")

        platform = d.pop("platform")

        state = d.pop("state")

        device_type = d.pop("device_type")

        site_id = d.pop("site_id", UNSET)

        description = d.pop("description", UNSET)

        management_ip = d.pop("management_ip", UNSET)

        infra_ip = d.pop("infra_ip", UNSET)

        dhcp_ip = d.pop("dhcp_ip", UNSET)

        serial = d.pop("serial", UNSET)

        ztp_mac = d.pop("ztp_mac", UNSET)

        vendor = d.pop("vendor", UNSET)

        model = d.pop("model", UNSET)

        os_version = d.pop("os_version", UNSET)

        synchronized = d.pop("synchronized", UNSET)

        port = d.pop("port", UNSET)

        device = cls(
            hostname=hostname,
            platform=platform,
            state=state,
            device_type=device_type,
            site_id=site_id,
            description=description,
            management_ip=management_ip,
            infra_ip=infra_ip,
            dhcp_ip=dhcp_ip,
            serial=serial,
            ztp_mac=ztp_mac,
            vendor=vendor,
            model=model,
            os_version=os_version,
            synchronized=synchronized,
            port=port,
        )


        device.additional_properties = d
        return device

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
