%define	pre	pre
Summary:	commandline traffic analysis tool
Name:		rate
Version:	0.9
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://s-tech.elsat.net.pl/bmtools/%{name}-%{version}%{pre}.tar.gz
# Source0-md5:	6238c7cd1099e48e141b1b2cc6f00e23
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'rate' is a swiss-army-knife commandline traffic analysis tool,
designed to help a network administrator to see what is happening at a
router at the moment. Unlike tcpdump(1), rate uses statistical and
stream-oriented methods, and will never produce an output stream at a
speed beyond human perception. The output is less accurate, however.
Rate features four different operating modes, designed to perform the
following tasks: estimating overall traffic rates, determining nodes
generating the highest traffic, determining connections and flows
generating the highest traffic and extracting strings from packets.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc} %{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install doc/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
