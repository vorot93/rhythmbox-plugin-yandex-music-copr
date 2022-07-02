%global reponame rhythmbox-plugin-yandex-music
%global commit 39c4d2e7d0465add36fda958a8ad51f7a942003a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20220701
%global debug_package %{nil}
%global plugindir /rhythmbox/plugins/yandex-music

Name:           rhythmbox-yandex-music
Version:        0
Release:        0.%{date}git%{shortcommit}%{?dist}
Summary:        Yandex.Music plugin for Rhythmbox
License:        GPLv3
URL:            https://github.com/dobroweb/%{reponame}
Source0:        https://github.com/dobroweb/%{reponame}/archive/%{commit}/%{reponame}-%{commit}.tar.gz
Requires:       rhythmbox%{?_isa}
Requires:       python3dist(yandex-music)

%description
Yandex.Music plugin for Rhythmbox.

%prep
%autosetup -n %{reponame}-%{commit}

%install

mkdir -p %{buildroot}/%{_libdir}%{plugindir}{,po}
mkdir -p %{buildroot}/%{_datadir}%{plugindir}

install -D po/* -t %{buildroot}%{_libdir}%{plugindir}/po
install -D *.py description.plugin -t %{buildroot}%{_libdir}%{plugindir}
install -D gschemas.compiled *.gschema.xml *.svg -t %{buildroot}%{_datadir}%{plugindir}

%files
%doc README.md
%license LICENSE
%{_libdir}%{plugindir}
%{_datadir}%{plugindir}
