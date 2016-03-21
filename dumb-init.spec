Summary:	A minimal init system for Linux containers
Name:		dumb-init
Version:	1.0.1
Release:	1
License:	MIT
Group:		Base
Source0:	https://github.com/Yelp/dumb-init/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8eb97a95d886a26dfc939adbce0d028c
URL:		https://github.com/Yelp/dumb-init
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sbindir	/sbin

%description
dumb-init is a simple process supervisor and init system designed to
run as PID 1 inside minimal container environments (such as Docker).
It is a deployed as a small, statically-linked binary written in C.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -std=gnu99 -Wall -Werror"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p dumb-init $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_sbindir}/dumb-init
