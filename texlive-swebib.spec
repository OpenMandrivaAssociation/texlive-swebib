# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/swebib
# catalog-date 2007-01-15 14:17:51 +0100
# catalog-license lppl1.2
# catalog-version undef
Name:		texlive-swebib
Version:	20070115
Release:	1
Summary:	Swedish bibliography styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/swebib
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swebib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swebib.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The bundle contains Swedish versions of the standard
bibliography styles, and of the style plainnat. The styles
should be funtionally equivalent to the corresponding original
styles, apart from the Swedish translations. The styles do not
implement Swedish collation.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/swebib/sweabbrv.bst
%{_texmfdistdir}/bibtex/bst/swebib/swealpha.bst
%{_texmfdistdir}/bibtex/bst/swebib/sweplain.bst
%{_texmfdistdir}/bibtex/bst/swebib/sweplnat.bst
%{_texmfdistdir}/bibtex/bst/swebib/sweunsrt.bst
%doc %{_texmfdistdir}/doc/latex/swebib/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
