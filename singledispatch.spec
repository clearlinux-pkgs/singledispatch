#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : singledispatch
Version  : 3.4.0.3
Release  : 13
URL      : https://pypi.python.org/packages/source/s/singledispatch/singledispatch-3.4.0.3.tar.gz
Source0  : https://pypi.python.org/packages/source/s/singledispatch/singledispatch-3.4.0.3.tar.gz
Summary  : This library brings functools.singledispatch from Python 3.4 to Python 2.6-3.3.
Group    : Development/Tools
License  : MIT
Requires: singledispatch-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==============
singledispatch
==============
`PEP 443 <http://www.python.org/dev/peps/pep-0443/>`_ proposed to expose
a mechanism in the ``functools`` standard library module in Python 3.4
that provides a simple form of generic programming known as
single-dispatch generic functions.

%package python
Summary: python components for the singledispatch package.
Group: Default

%description python
python components for the singledispatch package.


%prep
%setup -q -n singledispatch-3.4.0.3

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
