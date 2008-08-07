# TODO
# - make it generic for gecko based browsers (browser-plugins should first support this) and rename accordingly
Summary:	Konquefox extension for Firefox
Name:		konquefox
Version:	1.6.1
Release:	0.1
License:	BSD License
Group:		Development/Languages/PHP
URL:		https://addons.mozilla.org/en-US/firefox/addon/2671
Source0:	https://addons.mozilla.org/en-US/firefox/downloads/file/31174/%{name}-%{version}-fx.xpi
# Source0-md5:	9576fe6d09adf98fe4fc7bcee6551158
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# extension id from install.rdf
%define		extensionid		konquefox@free.fr
%define		extensiondir	%{_datadir}/mozilla-firefox/extensions/%{extensionid}

%description
Konquefox is an extension for Mozilla Firefox that adds some usefull
buttons: Clear URL, Go Up and Zoom, for a better integration in Linux
or KDE.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensiondir}
cp -a chrome.manifest install.rdf $RPM_BUILD_ROOT%{extensiondir}
cp -a konquefox.jar $RPM_BUILD_ROOT%{extensiondir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{extensiondir}
%{extensiondir}/chrome.manifest
%{extensiondir}/install.rdf
%{extensiondir}/konquefox.jar
