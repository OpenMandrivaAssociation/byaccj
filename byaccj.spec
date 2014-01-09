%{?_javapackages_macros:%_javapackages_macros}
# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Summary:	Parser Generator with Java Extension
Name:		byaccj
Version:	1.15
Release:	7.0%{?dist}
Epoch:		0
License:	Public Domain
URL:		http://byaccj.sourceforge.net/

Source0:	http://sourceforge.net/projects/byaccj/files/byaccj/1.15/byaccj1.15_src.tar.gz
Requires:	man-pages

%description
BYACC/J is an extension of the Berkeley v 1.8 YACC-compatible 
parser generator. Standard YACC takes a YACC source file, and 
generates one or more C files from it, which if compiled properly, 
will produce a LALR-grammar parser. This is useful for expression 
parsing, interactive command parsing, and file reading. Many 
megabytes of YACC code have been written over the years.
This is the standard YACC tool that is in use every day to produce 
C/C++ parsers. I have added a "-J" flag which will cause BYACC to 
generate Java source code, instead. So there finally is a YACC for 
Java now! 

%prep
%setup -q -n %{name}%{version}
chmod -c -x src/* docs/*
sed -i -e 's|-arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -mmacosx-version-min=10.4||g' src/Makefile

%build
pushd src
make linux CFLAGS="%{optflags}" LDFLAGS=""
popd

sed -i 's/\r//g' docs/tf.y

%install
# manual
install -d -m 755 %{buildroot}%{_mandir}/man1
mv docs/yacc.cat %{buildroot}%{_mandir}/man1

# jars
mkdir -p %{buildroot}%{_bindir}
cp -p src/yacc.linux \
  %{buildroot}%{_bindir}/%{name}

%files
%doc docs/* src/README
%{_mandir}/man1/yacc.cat*
%attr(755, root, root) %{_bindir}/%{name}

%changelog
* Fri Jul 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 0:1.15-7
- Simplify installation of docs.
- Drop executable bits from sources and docs.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 26 2012 Alexander Kurtakov <akurtako@redhat.com> - 0:1.15-4
- Fix build.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 06 2011 Luis Bazan <bazanluis20@gmail.com> 0:1.15-2
- New Release

* Thu Aug 25 2011 Luis Bazan <bazanluis20@gmail.com> 0:1.15-1
- Update to 1.15

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0:1.14-4
- Build with %%{optflags} (#500022).

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.14-2
- drop repotag

* Sat Feb 9 2008 Devrim GUNDUZ <devrim@commandprompt.com> - 0:1.14-1jpp.1
- Update to 1.14
- Cosmetic cleanup in spec

* Tue Mar 06 2007 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.11-2jpp.2.fc7
- First build in fedora after passing review

* Thu Feb 15 2007 Tania Bento <tbento@redhat.com> - 0:1.11-2jpp.1
- Fixed the %%Release tag.
- Changed the %%License tag.
- Fixed the %%BuildRoot tag.
- Removed the %%Vendor tag.
- Removed the %%Distribution tag.
- Removed the %%BuildRequires: gcc and make tags as these d not need to be
listed.
- Removed "%%define section free".
- Added "sed -i 's/\r//g docs/tf.y' to fix a warning generated by
rpmlint.
- Fixed the %%Source0 tag.
- Changed the %%Group tag.
- Installed man pages in proper directory. 

* Wed Jan 04 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.11-2jpp
- First JPP 1.7 build

* Wed Nov 16 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.11-1jpp
- First JPackage release

