%global tl_name ptptex
%global tl_revision 19440

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.91
Release:	%{tl_revision}.1
Summary:	Macros for Progress of Theoretical Physics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ptptex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptptex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptptex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The distribution contains the class (which offers an option file for
preprints), and a template. The class requires the cite, overcite and
wrapfig packages.

