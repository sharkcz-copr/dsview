%global srcname DSView

Name:           dsview
Version:        1.3.2
Release:        1%{?dist}
Summary:        GUI for DreamSourceLab USB-based instruments

License:        GPL-3.0-or-later AND GPL-2.0-or-later AND MIT
URL:            https://github.com/DreamSourceLab/DSView
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/DreamSourceLab/DSView/commit/2018baf0e1add4f9971dd02271ee8e6773cebfac
Patch0:         2018baf0e1add4f9971dd02271ee8e6773cebfac.patch
# use distro compiler/linker flags
Patch1:         dsview-cmake-flags.patch

BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  cmake(zlib)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  boost-devel
BuildRequires:  systemd-devel
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

%description
DSView is a GUI program for supporting various instruments from DreamSourceLab,
including logic analyzers, oscilloscopes, etc. DSView is based on the sigrok
project.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%cmake
%cmake_build


%install
%cmake_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

pushd %{buildroot}/%{_datadir}/%{srcname}
for f in NEWS* ug*.pdf; do
    rm -f $f
    ln -sf ../doc/%{name}/$f $f
done
popd


%files
%license COPYING
%doc README.md NEWS25 NEWS31 ug25.pdf ug31.pdf
%{_bindir}/%{srcname}
%{_datadir}/%{srcname}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/*/%{name}.svg
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/libsigrokdecode4DSL/
%{_udevrulesdir}/60-dreamsourcelab.rules


%changelog
* Mon Aug 18 2025 Dan Horák <dan@danny.cz> - 1.3.2-1
- initial Fedora version
