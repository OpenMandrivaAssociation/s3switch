Name:		s3switch
Summary:	Switch display output between CRT/LCD/TV on S3 boards
Version:	0.20020911
Release:	%mkrel 4
License:	MIT
Group:		System/X11
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	http://www.probo.com/timr/s3ssrc.zip
Exclusivearch:	%{ix86}

%description
s3switch is an utility that allows the switch of the display
output between the various output devices supported by
Savage boards (CRT, LCD, TV).

%prep
%setup -q -c

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}/
install -m755 s3switch %{buildroot}%{_bindir}/s3switch
mkdir -p %{buildroot}%{_mandir}/man1/
install -m644 s3switch.1x %{buildroot}%{_mandir}/man1/s3switch.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/s3switch
%{_mandir}/man1/s3switch.1*

