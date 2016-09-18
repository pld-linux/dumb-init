#
# Conditional build:
%bcond_without	static		# don't build static version

Summary:	A minimal init system for Linux containers
Name:		dumb-init
Version:	1.0.1
Release:	4
License:	MIT
Group:		Base
Source0:	https://github.com/Yelp/dumb-init/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8eb97a95d886a26dfc939adbce0d028c
URL:		https://github.com/Yelp/dumb-init
%if %{with static}
BuildRequires:	musl-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
dumb-init is a simple process supervisor and init system designed to
run as PID 1 inside minimal container environments (such as Docker).
It is a deployed as a small, statically-linked binary written in C.

%package static
Summary:	A minimal init system for Linux containers (static)
Group:		Base

%description static
dumb-init is a simple process supervisor and init system designed to
run as PID 1 inside minimal container environments (such as Docker).
It is a deployed as a small, statically-linked binary written in C.

This package contains statically linked version of dumb-init.

%prep
%setup -q

%build
%if %{with static}
%{__make} \
	CC="musl-gcc" \
	CFLAGS="%{rpmcflags} -std=gnu99 -Wall -Werror -static"
mv dumb-init dumb-init-static
%{__make} clean
%endif

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -std=gnu99 -Wall -Werror"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p dumb-init $RPM_BUILD_ROOT%{_sbindir}
%if %{with static}
install -p dumb-init-static $RPM_BUILD_ROOT%{_sbindir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_sbindir}/dumb-init

%if %{with static}
%files static
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_sbindir}/dumb-init-static
%endif
