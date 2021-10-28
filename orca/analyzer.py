from collections import defaultdict
from typing import NewType

from .parser import Document

Routes = NewType('Routes', dict[str, list[str]])


def analyze(doc: Document) -> Routes:
    tag2vms = defaultdict(list)
    for vm in doc['vms']:
        for tag in vm['tags']:
            tag2vms[tag].append(vm['vm_id'])

    paths = defaultdict(list)
    for r in doc['fw_rules']:
        if (sources := tag2vms.get(r['source_tag'])) is None:
            continue

        for target in tag2vms.get(r['dest_tag'], []):
            paths[target].extend(set(sources) - {target})

    return Routes(paths)
