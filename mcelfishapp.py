import os
import subprocess
import mcelfish
from pathlib import Path


def assert_is_ints(lst):
    assert isinstance(lst, list)
    for e in lst:
        assert isinstance(e, int)


def _statusfname(data):
    h = str(hash(tuple(data)))
    statusfile = f"mcelfish{h}.status"
    return statusfile


def execute(data):
    assert_is_ints(data)
    if not data:
        return
    fname = _statusfname(data)
    rfname = _statusfname(data) + ".run"
    if not os.path.isfile(fname):
        exit(f"Status file doesn't exist for {data}")

    if os.path.isfile(rfname):
        exit(f"Already running")
    else:
        Path(rfname).touch()

    model, trace = mcelfish.run(data=data)
    smry, res = mcelfish.summary(model, trace)
    retval = smry.to_html()
    _, _, _, _, beta = mcelfish.beta(res)
    html = f"<div>{retval}</div><p>{beta}</p>"
    with open(fname, "a") as fout:
        fout.write(f"<html><body>")
        fout.write(f"<h1>Results</h1>")
        fout.write(f"\t<div>{data}</div>\n")
        fout.write(f"\t<div>{html}</div>\n")
        fout.write(f"</body></html>\n")


def get(data):
    assert_is_ints(data)
    if not data:
        return "No Data"
    statusfname = _statusfname(data)
    if os.path.isfile(statusfname):
        with open(statusfname, "r") as fh:
            return "".join(fh.read())
    else:
        args = [str(e) for e in data]
        Path(statusfname).touch()
        subprocess.Popen(["python", __file__, *args])
        return "Computing ..."


def main():
    from sys import argv

    if len(argv) < 2:
        exit("Usage: mcelfishapp 5 1 0 0 0")
    data = [int(e) for e in argv[1:]]
    execute(data)


if __name__ == "__main__":
    main()
