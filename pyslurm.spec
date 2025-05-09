%global slurm_version 24.05
%global slurm_patch 8
%global commit c8ce3a4b3be693bb70a3d5dfc06f6a06d2dece63
%global snapshot 1.git29994

Name:           python-pyslurm
Version:        %{slurm_version}.0^%{snapshot}
Release:        2.bx%{?dist}
Summary:        Python Interface to Slurm

License:        GPL-2.0
URL:            https://pyslurm.github.io/
Source:         https://github.com/vub-hpc/pyslurm/archive/%{commit}.tar.gz

%global _description %{expand:
PySlurm is the Python client library for the Slurm Workload Manager.}

%description %_description

%package -n python3-pyslurm
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  slurm-devel == %{slurm_version}.%{slurm_patch}

Requires: slurm == %{slurm_version}.%{slurm_patch}

%description -n python3-pyslurm %_description

%prep
%autosetup -p0 -n pyslurm-%{commit}

%build
%py3_build

%install
%py3_install

# Testing disabled
# PySlurm needs a working Slurm environment

%files -n python3-pyslurm
%license COPYING.txt
%doc README.md
%{python3_sitearch}/pyslurm-*.egg-info/
%{python3_sitearch}/pyslurm/

%changelog
* Wed Sep 4 2024 Alex Domingo <alex.domingo.toro@vub.be>
- Initial version of the spec file for Slurm 24.05
