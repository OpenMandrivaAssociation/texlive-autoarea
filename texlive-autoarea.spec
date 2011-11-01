Name:		texlive-autoarea
Version:	0.3a
Release:	1
Summary:	Automatic computation of bounding boxes with PiCTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pictex/addon/autoarea
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autoarea.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autoarea.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package makes PiCTeX recognize lines and arcs in
determining the "bounding box" of a picture. (PiCTeX so far
accounted for put commands only). The "bounding box" is
essential for proper placement of a picture between running
text and margins and for keeping the running text away.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/autoarea/autoarea.sty
%doc %{_texmfdistdir}/doc/latex/autoarea/ANNOUNCE.txt
%doc %{_texmfdistdir}/doc/latex/autoarea/README.aa
%doc %{_texmfdistdir}/doc/latex/autoarea/autodemo/README.autodemo
%doc %{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo+.log
%doc %{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo+.pdf
%doc %{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo+.tex
%doc %{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo-.log
%doc %{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo-.pdf
%doc %{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo-.tex
%doc %{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
