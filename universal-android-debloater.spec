Name:		universal-android-debloater
Version:	1.2.0
Release:	1
Summary:	A GUI tool to debloat non-rooted Android devices using ADB
License:	GPL-3.0-or-later
Group:		Utility
URL:		https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation
Source0:	https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz
Source2:	uad-ng.desktop

BuildRequires:	cargo
BuildRequires:	cmake
BuildRequires:	clang
BuildRequires:	desktop-file-utils
BuildRequires:	rust-packaging
Requires:	android-tools

%description
A GUI tool to debloat non-rooted Android devices using ADB.

%prep
%autosetup -n %{name}-next-generation-%{version} -p1
# Extract vendored crates
tar xf %{S:1}
# Prep vendored crates dir
%cargo_prep -v vendor/

%build
export CARGO_HOME=$PWD/.cargo
%cargo_build
# sort out crate licenses
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%install
%cargo_install
# install icon and desktop file
install -Dm644 resources/assets/logo-dark.png "%{buildroot}%{_datadir}/pixmaps/uad-ng.png"
install -Dm644 %{S:2} -t "%{buildroot}%{_datadir}/applications/"

%check
%cargo_test
desktop-file-validate %{buildroot}%{_datadir}/applications/uad-ng.desktop

%files
%license LICENSE LICENSES.dependencies
%{_bindir}/uad-ng
%{_datadir}/applications/uad-ng.desktop
%{_datadir}/pixmaps/uad-ng.png
