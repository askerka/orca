import io
import typing

import pytest

from orca.parser import parse


@pytest.fixture
def file() -> typing.IO:
    return io.StringIO("""{
    "vms": [
        {
            "vm_id": "vm-a211de",
            "name": "jira_server",
            "tags": [
                "ci",
                "dev"
            ]
        },
        {
            "vm_id": "vm-c7bac01a07",
            "name": "bastion",
            "tags": [
                "ssh",
                "dev"
            ]
        }
    ],
    "fw_rules": [
        {
            "fw_id": "fw-82af742",
            "source_tag": "ssh",
            "dest_tag": "dev"
        }
    ]
}""")


def test_parse(file: file) -> None:
    result = parse(file)

    assert "vms" in result
    assert "fw_rules" in result
