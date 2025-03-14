#!/bin/bash

if [[ -z "$1" || -d "$1" ]]; then
    echo "You didn't specify anything to build";
    if [ -d "$1" ]
    then
        cd "$1" || exit
    fi
    spec=$(ls ./*.spec | head -1)
    if [ -z "$spec" ]
    then
        echo "No spec file found. Exiting."
        exit 1;
    else
        reg='Name: '
        name=$(grep "$reg" "$spec" | sed -e "s/$reg//" -e "s/ //g")
        reg='Version: '
        echo "Found spec $spec: name $name"
    fi
else
    spec=$1.spec
    name="$1"
fi

if grep -qE 'Fedora|release [6-9]' /etc/redhat-release >& /dev/null
then
  myrpmbasedir=$HOME/rpmbuild
else
  myrpmbasedir=/usr/src/redhat
fi

rpmbasedir=${BDISTRPMBASEDIR:-$myrpmbasedir}

echo "----> Building rpm for $name"
src_dir=$PWD
echo "----> Using $src_dir"

# delete older versions of the rpm since there's no point having old
# versions in there when we still have the src.rpms in the SRPMS dir
echo "----> Cleaning up older packages"
find "$rpmbasedir/RPMS" -type f -name "${name}-[0-9]\*" -delete

echo "----> Installing specfile requires"
sudo dnf -y builddep "$spec" 

echo "----> Building the package"

# -ba: source and binary
# no debuginfo
# download sources from remote
rpmbuild \
    --define "_sourcedir $src_dir" \
    --define "_topdir $rpmbasedir" \
    --undefine=_disable_source_fetch \
    --without debuginfo \
    -ba "$spec"
ec=$?

exit $ec
