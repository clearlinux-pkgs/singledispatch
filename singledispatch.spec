#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : singledispatch
Version  : 3.6.2
Release  : 41
URL      : https://files.pythonhosted.org/packages/9d/22/e55f573ff772600858e4cb91b05f6e17edb8d4636a8af0039ceb668b51ee/singledispatch-3.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9d/22/e55f573ff772600858e4cb91b05f6e17edb8d4636a8af0039ceb668b51ee/singledispatch-3.6.2.tar.gz
Summary  : Backport functools.singledispatch from Python 3.4 to Python 2.6-3.3.
Group    : Development/Tools
License  : MIT
Requires: singledispatch-license = %{version}-%{release}
Requires: singledispatch-python = %{version}-%{release}
Requires: singledispatch-python3 = %{version}-%{release}
Requires: ordereddict
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : ordereddict
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/singledispatch.svg
:target: `PyPI link`_

%package license
Summary: license components for the singledispatch package.
Group: Default

%description license
license components for the singledispatch package.


%package python
Summary: python components for the singledispatch package.
Group: Default
Requires: singledispatch-python3 = %{version}-%{release}

%description python
python components for the singledispatch package.


%package python3
Summary: python3 components for the singledispatch package.
Group: Default
Requires: python3-core
Provides: pypi(singledispatch)
Requires: pypi(six)

%description python3
python3 components for the singledispatch package.


%prep
%setup -q -n singledispatch-3.6.2
cd %{_builddir}/singledispatch-3.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622128290
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/singledispatch
cp %{_builddir}/singledispatch-3.6.2/LICENSE %{buildroot}/usr/share/package-licenses/singledispatch/8e6689d37f82d5617b7f7f7232c94024d41066d1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/singledispatch/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
