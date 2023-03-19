Name:		way-displays
Version:	1.7.1
Release:	1
Summary:	Auto Manage Your Wayland Displays
License:	MIT
URL:		https://github.com/alex-courtis/way-displays
Source0:	%{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	git
BuildRequires:	make

BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots)
BuildRequires:	pkgconfig(yaml-cpp)

%description
Auto Manage Your Wayland Displays

%prep
%autosetup

%build
make
make man

%install
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 755 %{name}.1 %{buildroot}%{_datadir}/man/man1/%{name}.1
install -D -m 644 cfg.yaml %{buildroot}/etc/%{name}/cfg.yaml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/man/man1/%{name}.1.gz
/etc/%{name}/cfg.yaml

%changelog
* Sun May 19 2023 Aaron Wiedemer <hello@wiedemer.xyz> 1.7.1
- Initial package
