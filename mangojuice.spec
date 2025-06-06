Name:           mangojuice
Version:        0.8.5
Release:        1
Summary:        Graphical UI to manage Mangohud settings
Group:          Graphics/Utilities
License:        GPLv3
URL:            https://github.com/radiolamp/mangojuice/
Source0:        https://github.com/radiolamp/mangojuice/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(vapigen)

Requires:  mangohud
Requires:  vulkan-tools
Requires:  mesa-demos
Requires:  libadwaita-common
Requires:  %{_lib}gio2.0_0
Requires:  %{_lib}gee0.8_2
Requires:  gtk4

%description
This program will be a convenient alternative to Goverlay for setting up Mangohud.

%prep
%autosetup -p1

%build
# Switch to GCC because as of Clang 19.1.3-1 and Mangojuice 0.7.7 app crashing at launch.
export CC=gcc
export CXX=g++
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/mangojuice
%{_datadir}/applications/io.github.radiolamp.mangojuice.desktop
%{_datadir}/metainfo/io.github.radiolamp.mangojuice.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/io.github.radiolamp.mangojuice*
%{_iconsdir}/hicolor/scalable/apps/list-drag-handle-symbolic.svg
