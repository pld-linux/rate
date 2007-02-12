Summary:	Commandline traffic analysis tool
Summary(pl.UTF-8):	Narzędzie linii poleceń do analizy ruchu w sieci
Name:		rate
Version:	0.9
Release:	2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://s-tech.elsat.net.pl/bmtools/%{name}-%{version}.tar.gz
# Source0-md5:	5689ff8b6e0bb8f78dec9184623c5800
BuildRequires:	libpcap-devel >= 0.8
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rate is a swiss-army-knife commandline traffic analysis tool, designed
to help a network administrator to see what is happening at a router
at the moment. Unlike tcpdump(1), rate uses statistical and
stream-oriented methods, and will never produce an output stream at a
speed beyond human perception. The output is less accurate, however.
rate features four different operating modes, designed to perform the
following tasks: estimating overall traffic rates, determining nodes
generating the highest traffic, determining connections and flows
generating the highest traffic and extracting strings from packets.

%description -l pl.UTF-8
rate jest bogatym w możliwości narzędziem linii poleceń do analizy
ruchu w sieci, stworzonym aby pomóc administratorom sieci w ocenie
tego, co się w danej chwili dzieje na routerach. W odróżnieniu od
tcpdump(1), rate korzysta z metod statystycznych i potokowych, nigdy
nie generując strumienia danych wyjściowych z szybkością
przekraczającą możliwości ludzkiej percepcji. Natomiast otrzymywane
wyniki są mniej precyzyjne. rate posiada cztery różne tryby pracy
zaprojektowane aby realizować następujące zadania: szacowanie ogólnych
parametrów pracy sieci, identyfikacja węzłów generujących największy
ruch, identyfikacja połączeń i przepływów generujących największy
ruch oraz wydobywanie łańcuchów tekstowych z pakietów.

%prep
%setup -q

sed -i -e 's,net/bpf.h,pcap-bpf.h,' lib.c

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
