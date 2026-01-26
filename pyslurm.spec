%global slurm_version 25.11
%global slurm_patch 2
%global commit 9a7885376717c5aeb8a37436dc0f11f81a14f039
%global snapshot 1.git9a7885

Name:           python-pyslurm
Version:        %{slurm_version}.0^%{snapshot}
Release:        1.bx%{?dist}
Summary:        Python Interface to Slurm

License:        GPLv2+
URL:            https://pyslurm.github.io/
Source:         https://github.com/vub-hpc/pyslurm/archive/%{commit}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-Cython
BuildRequires:  python3-packaging
BuildRequires:  slurm-devel == %{slurm_version}.%{slurm_patch}
Requires: slurm == %{slurm_version}.%{slurm_patch}

%global _description %{expand:
PySlurm is the Python client library for the Slurm Workload Manager.}

%description %_description

%package -n python3-pyslurm
Summary:        %{summary}

%description -n python3-pyslurm %_description

%prep
%autosetup -p0 -n pyslurm-%{commit}

# Dynamically generates BuildRequires, including:
# - Build backend dependencies (PEP 518)
# - Runtime dependencies for tests
# - Dependencies from a dependency group (PEP 735)
%generate_buildrequires
%pyproject_buildrequires

# Build the wheel package using the upstream-specified build backend (PEP 517)
%build
%pyproject_wheel

# Install the wheel package and save the file list
%install
%pyproject_install

# Explicitly list the installed importable module to avoid accidental installations.
# Use -l to assert a %%license file is found (PEP 639).
%pyproject_save_files -l pyslurm

# Testing disabled
# PySlurm needs a working Slurm environment

%files -n python3-pyslurm
%license COPYING.txt
%doc README.md
%{python3_sitearch}/pyslurm-*.egg-info/
%{python3_sitearch}/pyslurm/

%changelog
* Mon Jan 26 2026 Alex Domingo <alex.domingo.toro@vub.be>
- Update for Slurm 25.11
* Wed Sep 4 2024 Alex Domingo <alex.domingo.toro@vub.be>
- Initial version of the spec file for Slurm 24.05
