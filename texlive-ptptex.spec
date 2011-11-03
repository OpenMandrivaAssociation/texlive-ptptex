# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/ptptex
# catalog-date 2008-11-22 15:14:22 +0100
# catalog-license lppl
# catalog-version 0.91
Name:		texlive-ptptex
Version:	0.91
Release:	1
Summary:	Macros for 'Progress of Theoretical Physics'
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ptptex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptptex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptptex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The distribution contains the class (which offers an option
file for preprints), and a template. The class requires the
cite, overcite and wrapfig packages.

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
%{_texmfdistdir}/tex/latex/ptptex/ptp-prep.clo
%{_texmfdistdir}/tex/latex/ptptex/ptptex.cls
%{_texmfdistdir}/tex/latex/ptptex/wrapft.sty
%doc %{_texmfdistdir}/doc/latex/ptptex/README
%doc %{_texmfdistdir}/doc/latex/ptptex/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/ptptex/manptp.pdf
%doc %{_texmfdistdir}/doc/latex/ptptex/manptp.tex
%doc %{_texmfdistdir}/doc/latex/ptptex/template.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
