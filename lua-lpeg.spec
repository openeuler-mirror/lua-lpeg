%define  mod_name lpeg

Name:    lua-%{mod_name}
Version: 1.0.2
Release: 3
Summary: Parsing Expression Grammars For Lua
License: MIT
URL:     http://www.inf.puc-rio.br/~roberto/lpeg/
Source0: http://www.inf.puc-rio.br/~roberto/lpeg/lpeg-%{version}.tar.gz
Patch0:  lua-lpeg-fix-cc.patch

BuildRequires: gcc, lua-devel
Requires: lua, lua(abi)

%description
LPeg is a new pattern-matching library for Lua, based on Parsing Expression
Grammars (PEGs).Following the Snobol tradition, LPeg defines patterns as
first-class objects. That is, patterns are regular Lua values (represented by
userdata). The library offers several functions to create and compose patterns.
With the use of metamethods, several of these functions are provided as infix
or prefix operators. On the one hand, the result is usually much more verbose
than the typical encoding of patterns using the so called regular expressions
(which typically are not regular expressions in the formal sense). On the other
hand, first-class patterns allow much better documentation (as it is easy to
comment the code, to break complex definitions in smaller parts, etc.) and are
extensible, as we can define new functions to create and compose patterns.

%prep
%autosetup -n %{mod_name}-%{version} -p1

%build
%make_build COPT="%{optflags}"

%install
%{__mkdir_p} %{buildroot}%{lua_libdir}
%{__mkdir_p} %{buildroot}%{lua_pkgdir}
%{__install} -p lpeg.so %{buildroot}%{lua_libdir}/lpeg.so.%{version}
%{__ln_s} lpeg.so.%{version} %{buildroot}%{lua_libdir}/lpeg.so
%{__install} -p -m 0644 re.lua %{buildroot}%{lua_pkgdir}

%check
make test

%pre


%preun


%post


%postun


%files
%doc HISTORY lpeg-128.gif lpeg.html re.html test.lua
%{lua_libdir}/lpeg.*
%{lua_pkgdir}/*

%changelog
* Wed Apr 19 2023 Xiaoya Huang <huangxiaoya@iscas.ac.cn> - 1.0.2-3
- Fix CC compiler support

* Sat Sep 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0.2-2
- Modify spec error information

* Sat Aug 31 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0.2-1
- Package init

