#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : singledispatch
Version  : 3.4.0.3
Release  : 23
URL      : https://files.pythonhosted.org/packages/d9/e9/513ad8dc17210db12cb14f2d4d190d618fb87dd38814203ea71c87ba5b68/singledispatch-3.4.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/d9/e9/513ad8dc17210db12cb14f2d4d190d618fb87dd38814203ea71c87ba5b68/singledispatch-3.4.0.3.tar.gz
Summary  : This library brings functools.singledispatch from Python 3.4 to Python 2.6-3.3.
Group    : Development/Tools
License  : MIT
Requires: singledispatch-python = %{version}-%{release}
Requires: singledispatch-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
singledispatch
        ==============

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

%description python3
python3 components for the singledispatch package.


%prep
%setup -q -n singledispatch-3.4.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542759106
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
