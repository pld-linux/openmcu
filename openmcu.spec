Summary:	H.323 conferencing server
Summary(pl):	Serwer konferencji H.323
Name:		openmcu
Version:	1.0.12
Release:	1
License:	MPL
Group:		Applications/Communications
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openh323-devel
BuildRequires:	openssl-devel
BuildRequires:	pwlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
A free H.323 conferencing server. Part of OpenH323 project.

%description -l pl
Darmowy serwer konferencji H.323. Czê¶æ projektu OpenH323.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
PWLIBDIR=%{_prefix}; export PWLIBDIR
OPENH323DIR=%{_prefix}; export OPENH323DIR

%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	OPTCCFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install obj_*/%{name}	$RPM_BUILD_ROOT%{_bindir}
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf *.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
