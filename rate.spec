%define	pre	pre
Summary:	Commandline traffic analysis tool
Summary(pl):	Narzêdzie linii poleceñ do analizy ruchu w sieci
Name:		rate
Version:	0.9
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://s-tech.elsat.net.pl/bmtools/%{name}-%{version}%{pre}.tar.gz
# Source0-md5:	6238c7cd1099e48e141b1b2cc6f00e23
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
rate jest bogatym w mo¿liwo¶ci narzêdziem linii poleceñ do analizy
ruchu w sieci, stworzonym aby pomóc administratorom sieci w ocenie
tego, co siê w danej chwili dzieje na routerach. W odró¿nieniu od
tcpdump(1), rate korzysta z metod statystycznych i potokowych, nigdy
nie generuj±c strumienia danych wyj¶ciowych z szybko¶ci±
przekraczaj±c± mo¿liwo¶ci ludzkiej percepcji. Natomiast otrzymywane
wyniki s± mniej precyzyjne. rate posiada cztery ró¿ne tryby pracy
zaprojektowane aby realizowaæ nastêpuj±ce zadania: szacowanie ogólnych
parametrów pracy sieci, identyfikacja wêz³ów generuj±cych najwiêkszy
ruch, identyfikacja po³±czeñ i przep³ywów generuj±cych najwiêkszy
ruch oraz wydobywanie ³añcuchów tekstowych z pakietów.

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
