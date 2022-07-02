# Created by pyp2rpm-3.3.8
%global pypi_name yandex-music
%global pypi_version 2.0.1

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Неофициальная Python библиотека для работы с API сервиса Яндекс

License:        LGPLv3
URL:            https://github.com/MarshalX/yandex-music-api/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiofiles)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)

%description
 Yandex Music API Делаю то, что по определённым причинам не сделала компания
Yandex.⚠️ Это неофициальная библиотека.Сообщество разработчиков общаются и
помогают друг другу в Telegram чате < присоединяйтесь! .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(aiofiles)
Requires:       python3dist(aiohttp)
Requires:       python3dist(requests)
%description -n python3-%{pypi_name}
 Yandex Music API Делаю то, что по определённым причинам не сделала компания
Yandex.⚠️ Это неофициальная библиотека.Сообщество разработчиков общаются и
помогают друг другу в Telegram чате < присоединяйтесь! .. image::


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%exclude %{python3_sitelib}/tests
%{python3_sitelib}/yandex_music
%{python3_sitelib}/yandex_music-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Sun Jul 03 2022 Artem Vorotnikov <artem@vorotnikov.me> - 2.0.1-1
- Initial package.
