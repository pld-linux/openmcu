Summary:	H.323 conferencing server
Summary(pl):	Serwer konferencji H.323
Name:		openmcu
Version:	1.1.7
Release:	1
License:	MPL 1.0
Group:		Applications/Communications
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
# Source0-md5:	041c468256f426e9e5a8cec0cdc769f6
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.11.7
BuildRequires:	pwlib-devel >= 1.4.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%requires_eq	openh323

%description
A free H.323 conferencing server. Part of OpenH323 project.

%description -l pl
Darmowy serwer konferencji H.323. Cz�� projektu OpenH323.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
