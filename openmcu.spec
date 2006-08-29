Summary:	H.323 conferencing server
Summary(pl):	Serwer konferencji H.323
Name:		openmcu
Version:	2.1.1
%define fver	%(echo %{version} | tr . _)
Release:	2
License:	MPL 1.0
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/openh323/%{name}-v%{fver}-src-tar.gz
# Source0-md5:	db561a73bc96557b105625f2107b03ef
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.15
BuildRequires:	pwlib-devel >= 1.10.0
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free H.323 conferencing server. Part of OpenH323 project.

%description -l pl
Darmowy serwer konferencji H.323. Czê¶æ projektu OpenH323.

%prep
%setup -q -n %{name}_v%{fver}
%patch0 -p1

%build
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	CXX="%{__cxx}" \
	OPTCCFLAGS="%{rpmcflags} -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install obj_*/%{name}	$RPM_BUILD_ROOT%{_bindir}
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
