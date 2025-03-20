#
# spec file for package tweeny
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

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
BuildRequires:  (ninja or ninja-build)

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
sed -i 's@lib/@%{_libdir}/@g' cmake/SetupExports.cmake

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
