%global tl_name classics
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1a
Release:	%{tl_revision}.1
Summary:	Cite classic works
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/classics
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/classics.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/classics.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a basic framework to cite classic works (specially
from authors such as Homer, Plato, Aristotle, Descartes, Hume, and Kant)
in accordance with traditional pagination systems. It may be used in
conjunction with other citation packages.

