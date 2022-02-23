%define srcname idna

Name:           python-%{srcname}
Version:	3.3
Release:	2
Summary:        Internationalized Domain Names in Applications (IDNA)
Group:		Development/Python
License:        BSD and Python and Unicode
URL:            https://github.com/kjd/idna
Source0:        https://github.com/kjd/idna/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python2)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2-pkg-resources
BuildRequires:  python-pkg-resources

%description
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891 <http://tools.ietf.org/html/rfc5891>.  This
version of the protocol is often referred to as "IDNA2008" and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement for the
"encodings.idna" module that comes with the Python standard library but
currently only supports the older 2003 specification.

%prep
%autosetup -n %{srcname}-%{version} -p1
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%__python setup.py build

%install
%__python setup.py install --skip-build --root %{buildroot}

%check
%__python setup.py test

%files
%doc README.rst HISTORY.rst
%{py_puresitedir}/%{srcname}
%{py_puresitedir}/%{srcname}-%{version}-py%{py_ver}.egg-info
