Name:		texlive-ptptex
Version:	19440
Release:	2
Summary:	Macros for 'Progress of Theoretical Physics'
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ptptex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptptex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptptex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The distribution contains the class (which offers an option
file for preprints), and a template. The class requires the
cite, overcite and wrapfig packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
