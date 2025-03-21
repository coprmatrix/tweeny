%define __builder ninja
Name:           tweeny
Version:        3.2.0
Release:        0
Summary:        Modern C++ tweening library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/mobius3/tweeny
Source0:        %{url}/archive/v%{version}.tar.gz#/tweeny-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  (ninja ninja-build)
BuildArch:      noarch

%description
Header-only %{summary}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}

%description devel
Header-only %{summary}.

%prep
%autosetup
sed -i 's~lib/~%{_libdir}/~g' cmake/SetupExports.cmake

%build
%cmake \
 -DCMAKE_BUILD_TYPE=Release \
 -DTWEENY_BUILD_EXAMPLES=OFF \
 -DTWEENY_BUILD_DOCUMENTATION=OFF \
 ..
%cmake_build

%install
%cmake_install

%files devel
%doc README.md CHANGELOG.md
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/cmake/Tweeny

%changelog
