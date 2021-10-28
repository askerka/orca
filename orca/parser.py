import json
from typing import IO, TypedDict, cast

from pydantic_typeddict import as_typed_dict


class VM(TypedDict):
    vm_id: str
    name: str
    tags: list[str]


class FirewallRule(TypedDict):
    fw_id: str
    source_tag: str
    dest_tag: str


class Document(TypedDict):
    vms: list[VM]
    fw_rules: list[FirewallRule]


def parse(file: IO) -> Document:
    return cast(
        Document,
        as_typed_dict(json.load(file), Document),
    )
