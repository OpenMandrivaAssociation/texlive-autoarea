# revision 15878
# category Package
# catalog-ctan /graphics/pictex/addon/autoarea
# catalog-date 2008-08-17 11:40:59 +0200
# catalog-license lppl
# catalog-version 0.3a
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
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
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
