# revision 15878
# category Package
# catalog-ctan /graphics/pictex/addon/autoarea
# catalog-date 2008-08-17 11:40:59 +0200
# catalog-license lppl
# catalog-version 0.3a
Name:		texlive-autoarea
Version:	0.3a
Release:	7
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

%description
This package makes PiCTeX recognize lines and arcs in
determining the "bounding box" of a picture. (PiCTeX so far
accounted for put commands only). The "bounding box" is
essential for proper placement of a picture between running
text and margins and for keeping the running text away.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3a-2
+ Revision: 749438
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3a-1
+ Revision: 717872
- texlive-autoarea
- texlive-autoarea
- texlive-autoarea
- texlive-autoarea
- texlive-autoarea

