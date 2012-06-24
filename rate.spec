Summary:	Commandline traffic analysis tool
Summary(pl):	Narz�dzie linii polece� do analizy ruchu w sieci
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

%description -l pl
rate jest bogatym w mo�liwo�ci narz�dziem linii polece� do analizy
ruchu w sieci, stworzonym aby pom�c administratorom sieci w ocenie
tego, co si� w danej chwili dzieje na routerach. W odr�nieniu od
tcpdump(1), rate korzysta z metod statystycznych i potokowych, nigdy
nie generuj�c strumienia danych wyj�ciowych z szybko�ci�
przekraczaj�c� mo�liwo�ci ludzkiej percepcji. Natomiast otrzymywane
wyniki s� mniej precyzyjne. rate posiada cztery r�ne tryby pracy
zaprojektowane aby realizowa� nast�puj�ce zadania: szacowanie og�lnych
parametr�w pracy sieci, identyfikacja w�z��w generuj�cych najwi�kszy
ruch, identyfikacja po��cze� i przep�yw�w generuj�cych najwi�kszy
ruch oraz wydobywanie �a�cuch�w tekstowych z pakiet�w.

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
