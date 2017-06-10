%define srcname idna

Name:           python-%{srcname}
Version:        2.5
Release:        1
Summary:        Internationalized Domain Names in Applications (IDNA)
Group:		Development/Python
License:        BSD and Python and Unicode
URL:            https://github.com/kjd/idna
Source0:        https://github.com/kjd/idna/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python2)
BuildRequires:  pythonegg(setuptools)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3egg(setuptools)

%description
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891 <http://tools.ietf.org/html/rfc5891>.  This
version of the protocol is often referred to as "IDNA2008" and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement for the
"encodings.idna" module that comes with the Python standard library but
currently only supports the older 2003 specification.

%package -n python2-%{srcname}
Summary:        Internationalized Domain Names in Applications (IDNA)
Group:		Development/Python

%description -n python2-%{srcname}
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891 <http://tools.ietf.org/html/rfc5891>.  This
version of the protocol is often referred to as "IDNA2008" and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement for the
"encodings.idna" module that comes with the Python standard library but
currently only supports the older 2003 specification.

%prep
%setup -q -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

cp -a . %{py2dir}


%build
%__python setup.py build

pushd %{py2dir}
%{__python2} setup.py build
popd

%install
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

%__python setup.py install --skip-build --root %{buildroot}

%check
%__python setup.py test

pushd %{py2dir}
%__python2 setup.py test
popd


%files
%doc README.rst HISTORY.rst LICENSE.rst
%{py_puresitedir}/%{srcname}
%{py_puresitedir}/%{srcname}-%{version}-py%{py_ver}.egg-info

%files -n python2-%{srcname}
%doc README.rst HISTORY.rst LICENSE.rst
%{py2_puresitedir}/%{srcname}
%{py2_puresitedir}/%{srcname}-%{version}-py%{py2_ver}.egg-info
