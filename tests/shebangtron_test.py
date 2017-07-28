import sys
from subprocess import check_output

def test_not_py_shebang(tmpdir, monkeypatch):
    flavor = "deadbeef"
    python = "snake"

    flavor_dir = tmpdir.mkdir(flavor)
    test_file = flavor_dir.join("mangleme")
    test_file.write("#!/bin/sh")

    monkeypatch.setenv("EUPS_PATH", tmpdir)
    monkeypatch.setenv("SHTRON_EUPS_FLAVOR", flavor)
    monkeypatch.setenv("SHTRON_PYTHON", python)

    print(check_output(["./shebangtron"]))

    assert test_file.read() == "#!/bin/sh"

def test_vanilla_py_shebang(tmpdir, monkeypatch):
    flavor = "deadbeef"
    python = "snake"

    flavor_dir = tmpdir.mkdir(flavor)
    test_file = flavor_dir.join("mangleme")
    test_file.write("#!python")

    monkeypatch.setenv("EUPS_PATH", tmpdir)
    monkeypatch.setenv("SHTRON_EUPS_FLAVOR", flavor)
    monkeypatch.setenv("SHTRON_PYTHON", python)

    print(check_output(["./shebangtron"]))

    assert test_file.read() == "#!" + python

def test_env_shebang(tmpdir, monkeypatch):
    flavor = "deadbeef"
    python = "snake"

    flavor_dir = tmpdir.mkdir(flavor)
    test_file = flavor_dir.join("mangleme")
    test_file.write("#!/usr/bin/env python")

    monkeypatch.setenv("EUPS_PATH", tmpdir)
    monkeypatch.setenv("SHTRON_EUPS_FLAVOR", flavor)
    monkeypatch.setenv("SHTRON_PYTHON", python)

    print(check_output(["./shebangtron"]))

    assert test_file.read() == "#!/usr/bin/env python"
