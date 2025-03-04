# <img src="logo.png" alt="PySlurm Logo">

pyslurm is the Python client library for the [Slurm Workload Manager](https://slurm.schedmd.com)

## Fork from VUB-HPC
This fork adds specific tooling and patches to PySlurm that are needed to build
and install this software in our HPC clusters.

Command to build the RPM of PySlurm from our build servers:
```
clusterbuildrpm -d -r pub -f vub-hpc -p pyslurm -b vub-hpc
```

## Requirements

* [Slurm](https://slurm.schedmd.com) - Slurm shared library and header files
* [Python](https://www.python.org) - >= 3.6
* [Cython](https://cython.org) - >= 0.29.37

This Version is for Slurm 24.05.x

## Versioning

In pyslurm, the versioning scheme follows the official Slurm versioning. The
first two numbers (`MAJOR.MINOR`) always correspond to Slurms Major-Release,
for example `24.05`.
The last number (`MICRO`) is however not tied in any way to Slurms `MICRO`
version, but is instead PySlurm's internal Patch-Level. For example, any
pyslurm 24.05.X version should work with any Slurm 24.05.X release.

## Installation

By default, it is searched inside `/usr/include` for the Header files and in
`/usr/lib64` for Slurms shared-library (`libslurm.so`) during Installation.
For Slurm installations in different locations, you will need to provide
the corresponding paths to the necessary files.

You can specify those with environment variables (recommended), for example:

```shell
export SLURM_INCLUDE_DIR=/opt/slurm/24.05/include
export SLURM_LIB_DIR=/opt/slurm/24.05/lib
```

Then you can proceed to install pyslurm, for example by cloning the Repository:

```shell
git clone https://github.com/PySlurm/pyslurm.git && cd pyslurm
scripts/build.sh

# Or simply with pip
pip install .
```

Also see `python setup.py --help`

## Contributors

pyslurm is made by [contributors like
you](https://github.com/PySlurm/pyslurm/graphs/contributors).

## Support

Feel free to ask questions in the [GitHub
Discussions](https://github.com/orgs/PySlurm/discussions)

Found a bug or you are missing a feature? Feel free to [open an Issue!](https://github.com/PySlurm/pyslurm/issues/new)
