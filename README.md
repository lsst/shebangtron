shebangtron
===

Update the python interpreter path of EUPS installed products.


Usage
===

  curl -sSL https://raw.githubusercontent.com/lsst/shebangtron/master/shebangtron | python


Overview
===

Recent releases of OSX include a feature called "[System Integrity
Proection](https://support.apple.com/en-us/HT204899)" or "SIP".

See [DMTN-001: Porting the stack to OS X El Capitan](http://dmtn-001.lsst.io/en/master/)

TL;DR - SIP breaks the common idiom of using `/usr/bin/env` in the shebang line
of python scripts.

A solution is to use the fully qualified path to the desired python interpreter
in the shebang line.  This can be automatically done as part of a build/install
process but the build time path is unlikely to work when exporting software
(Eg., moving it to another system) from the build environment.  This requires
that either a package manager (such as
[`conda-build`](https://github.com/conda/conda-build)) handles this as part of a
post-install hook or manual action on the part of the end-user.  As EUPS does
not support post-install hooks/scripts, a manual step is required.


Prerequisites
===

A working EUPS environment is needed to supply the `eups` utility and define
the env var `EUPS_PATH` must be defined.  For an `newinstall.sh` based env,
sourcing one of the generated setup scripts is sufficient. Eg.,

    source loadLSST.bash
    curl -sSL https://raw.githubusercontent.com/lsst/shebangtron/master/shebangtron | python


Nitty-gritty
===

`shebangtron` will attempt to fixup the shebang line of all files that have
write permissions under the path `${EUPS_PATH}/$(eups flavor)`.  This is not
presently configurable beyond setting the value of `EUPS_PATH`.

The intent to keep this script easily usable as a single file that can be
`curl`'d and piped to `python` rather than installed as a pypi or conda
package.

The script is composed of (modified) snippets extracted from
[`conda-build`](https://github.com/conda/conda-build) and merged into a single
script.  This was necessary to avoid requiring the end-user to both install
`conda-build` to use as a library and a separate "fixup" script.  In addition,
changes to the permission handling logic were needed.
