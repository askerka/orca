import pytest

from orca.analyzer import Document, analyze


@pytest.fixture
def document() -> Document:
    return {
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
    }


def test_analyzer(document: Document) -> None:
    result = analyze(document)

    assert result == {
        'vm-a211de': ['vm-c7bac01a07'],
        'vm-c7bac01a07': [],
    }
