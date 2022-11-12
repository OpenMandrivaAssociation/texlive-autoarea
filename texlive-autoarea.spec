Name:		texlive-autoarea
Version:	59552
Release:	1
Summary:	Automatic computation of bounding boxes with PiCTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pictex/addon/autoarea
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autoarea.r59552.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autoarea.doc.r59552.tar.xz
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
%{_texmfdistdir}/tex/latex/autoarea
%doc %{_texmfdistdir}/doc/latex/autoarea

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
