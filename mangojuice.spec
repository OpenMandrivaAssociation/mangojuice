Name:           mangojuice
Version:        0.6.1
Release:        1
Summary:        Graphical UI to manage Mangohud settings
Group:          Graphics/Utilities
License:        GPLv3
URL:            https://github.com/radiolamp/mangojuice/
Source0:        https://github.com/radiolamp/mangojuice/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  cmake
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
%meson
%meson_build

%install
%meson_install

%files
