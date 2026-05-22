%define module idna

Name:		python-idna
Version:	3.16
Release:	1
Summary:	Internationalized Domain Names in Applications (IDNA)
Group:		Development/Python
License:	BSD-3-Clause
URL:		https://github.com/kjd/idna
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(wheel)


%description
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891 <http://tools.ietf.org/html/rfc5891>.  This
version of the protocol is often referred to as "IDNA2008" and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement for the
"encodings.idna" module that comes with the Python standard library but
currently only supports the older 2003 specification.

%files
%doc README.md HISTORY.md
%{_bindir}/%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
