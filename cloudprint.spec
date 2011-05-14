# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%define alphatag git620e490f1a

Name:           cloudprint
Version:        0.5
Release:        0.1.%{alphatag}%{?dist}
Summary:        Share your CUPS printers with Google's Cloud Print


Group:          System Environment/Daemons
License:        GPLv3
URL:            https://github.com/armooo/cloudprint/
# git clone git://github.com/armooo/cloudprint.git
# git archive --prefix=cloudprint-0.4/ HEAD | bzip2 -9 -c > cloudprint-0.4.tar.bz2
Source0:        %{name}-%{version}-%{alphatag}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python >= 2.6
BuildRequires:  system-config-printer-libs, python-daemon, python-lockfile
Requires:       system-config-printer-libs, python-daemon, python-lockfile

%description
Cloudprint lets you print from any Google Cloud Print-enabled device
(http://google.com/landing/cloudprint) to your local CUPS printers.

%prep
%setup -q


%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="%{optflags}" %{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING
# For noarch packages: sitelib
%{python_sitelib}/*
%{_bindir}/cloudprint


%changelog
* Fri May 13 2011 Matt Domsch <matt@domsch.com> - 0.5-0.1.git620e490f1a
- Initial package
