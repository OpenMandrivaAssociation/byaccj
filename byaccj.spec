Summary:	Parser Generator with Java Extension
Name:		byaccj
Version:	1.15
Release:	9
License:	Public Domain
URL:		http://byaccj.sourceforge.net/

Source0:	http://sourceforge.net/projects/byaccj/files/byaccj/1.15/byaccj1.15_src.tar.gz
Patch0:		byaccj-1.15-fix-warnings.patch

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
%autosetup -p1 -n %{name}%{version}
chmod -c -x src/* docs/*
sed -i -e 's|-arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -mmacosx-version-min=10.4||g' src/Makefile

%build
pushd src
%make_build linux CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" CC=%{__cc}
popd

sed -i 's/\r//g' docs/tf.y

%install
install -d -m 755 %{buildroot}%{_mandir}/man1
mv docs/yacc.cat %{buildroot}%{_mandir}/man1

mkdir -p %{buildroot}%{_bindir}
cp -p src/yacc.linux \
  %{buildroot}%{_bindir}/%{name}

%files
%doc docs/* src/README
%{_mandir}/man1/yacc.cat*
%attr(755, root, root) %{_bindir}/%{name}
