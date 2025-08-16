#!/usr/bin/env python3

"""
The pagure_bz.json output order changes after each run, so make sure that it's
sorted.
"""

import json

PAGURE_BZ = "data/extras/pagure_bz.json"


def main() -> None:
    with open(PAGURE_BZ) as fp:
        data = json.load(fp)
    for namespace in data.values():
        for users in namespace.values():
            users.sort()
    with open(PAGURE_BZ, "w") as fp:
        json.dump(data, fp, sort_keys=True, indent=4)


if __name__ == "__main__":
    main()
