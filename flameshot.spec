#
# spec file for package flameshot
#
Summary:	Powerful, yet simple to use open-source screenshot software
Summary(pl.UTF-8):	Potężne, ale proste w użyciu otwartoźródłowe oprogramowanie do zrzutów ekranu
Name:		flameshot
Version:	12.1.0
Release:	1
License:	GPLv3+ and ASL 2.0 and GPLv2 and LGPLv3 and Free Art
Group:		Applications/Graphics
URL:		https://github.com/flameshot-org/flameshot
Source0:	https://github.com/flameshot-org/flameshot/archive/v%{version}.tar.gz
# Source0-md5:	8c24308d01e3c073f9e876785b623211
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5DBus-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Network-devel >= 5
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	hicolor-icon-theme
BuildRequires:	kf5-kguiaddons-devel >= 5.89.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-linguist
Suggests:	bash-completion-%{name}
Suggests:	fish-completion-%{name}
Suggests:	zsh-completion-%{name}

%description
A program to capture screenshots.

Features:
 - Customizable appearance
 - Annotation and drawing tools
 - DBus interface
 - Export to file, web

%description -l pl.UTF-8
Program do robienia zrzutów ekranu.

Cechy:
  - Konfigurowalny wygląd
  - Narzędzia do adnotacji i rysowania
  - Interfejs DBus
  - Eksport do pliku, sieci

%package -n bash-completion-flameshot
Summary:	Bash Completion for %{name}
Summary(pl.UTF-8):	Uzupełnianie parametrów polecenia flameshot dla powłoki BASH
Group:		Applications/Shells
Requires:	%{name} = %{version}
Requires:	bash-completion
BuildArch:	noarch

%description -n bash-completion-flameshot
Bash completion script for flameshot's CLI.

%description -n bash-completion-flameshot -l pl.UTF-8
Uzupełnianie parametrów polecenia flameshot dla powłoki BASH.

%package -n zsh-completion-flameshot
Summary:	ZSH completion for %{name}
Summary(pl.UTF-8):	Uzupełnianie parametrów polecenia flameshot dla powłoki ZSH
Group:		Applications/Shells
Requires:	%{name} = %{version}
BuildArch:	noarch

%description -n zsh-completion-flameshot
zsh shell completions for %{name}.

%description -n zsh-completion-flameshot -l pl.UTF-8
Uzupełnianie parametrów polecenia flameshot dla powłoki ZSH.

%package -n fish-completion-flameshot
Summary:	Fish completion for %{name}
Summary(pl.UTF-8):	Uzupełnianie parametrów polecenia flameshot dla powłoki FISH
Group:		Applications/Shells
Requires:	%{name} = %{version}
BuildArch:	noarch

%description -n fish-completion-flameshot
Fish command line completion support for %{name}.

%description -n fish-completion-flameshot -l pl.UTF-8
Uzupełnianie parametrów polecenia flameshot dla powłoki FISH.

%prep
%setup -q

%build
mkdir -p build
cd build
%cmake .. \
	-DUSE_WAYLAND_CLIPBOARD:BOOL=ON \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd build
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

cd ..
%find_lang Internationalization --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f Internationalization.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_desktopdir}/org.flameshot.Flameshot.desktop
%{_datadir}/dbus-1/interfaces/org.flameshot.Flameshot.xml
%{_datadir}/dbus-1/services/org.flameshot.Flameshot.service
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/org.flameshot.Flameshot.metainfo.xml
%{_mandir}/man1/%{name}.1*

%files -n bash-completion-flameshot
%defattr(644,root,root,755)
%{bash_compdir}/%{name}

%files -n zsh-completion-flameshot
%defattr(644,root,root,755)
%dir %{_datadir}/zsh
%dir %{zsh_compdir}
%{zsh_compdir}/_flameshot

%files -n fish-completion-flameshot
%defattr(644,root,root,755)
%dir %{_datadir}/fish
%dir %{fish_compdir}
%{fish_compdir}/flameshot.fish
