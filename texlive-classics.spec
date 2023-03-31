Name:		texlive-classics
Version:	53671
Release:	2
Summary:	Cite classic works
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/classics
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classics.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classics.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a basic framework to cite classic works
(specially from authors such as Homer, Plato, Aristotle,
Descartes, Hume, and Kant) in accordance with traditional
pagination systems. It may be used in conjunction with other
citation packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/classics/classics.sty
%doc %{_texmfdistdir}/doc/latex/classics/README
%doc %{_texmfdistdir}/doc/latex/classics/classics.pdf
%doc %{_texmfdistdir}/doc/latex/classics/classics.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
