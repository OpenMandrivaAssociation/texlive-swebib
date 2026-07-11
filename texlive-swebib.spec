%global tl_name swebib
%global tl_revision 76924

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Swedish bibliography styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/swebib
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/swebib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/swebib.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle contains Swedish versions of the standard bibliography
styles, and of the style plainnat. The styles should be functionally
equivalent to the corresponding original styles, apart from the Swedish
translations. The styles do not implement Swedish collation.

