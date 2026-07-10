%global tl_name autoarea
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3a
Release:	%{tl_revision}.1
Summary:	Automatic computation of bounding boxes with PiCTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pictex-addons/autoarea
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autoarea.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autoarea.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package makes PiCTeX recognize lines and arcs in determining the
"bounding box" of a picture. (PiCTeX so far accounted for put commands
only). The "bounding box" is essential for proper placement of a picture
between running text and margins and for keeping the running text away.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/autoarea
%dir %{_datadir}/texmf-dist/tex/latex/autoarea
%dir %{_datadir}/texmf-dist/doc/latex/autoarea/autodemo
%doc %{_datadir}/texmf-dist/doc/latex/autoarea/ANNOUNCE.txt
%doc %{_datadir}/texmf-dist/doc/latex/autoarea/README
%doc %{_datadir}/texmf-dist/doc/latex/autoarea/autodemo/README.autodemo
%doc %{_datadir}/texmf-dist/doc/latex/autoarea/autodemo/autodemo+.pdf
%doc %{_datadir}/texmf-dist/doc/latex/autoarea/autodemo/autodemo+.tex
%doc %{_datadir}/texmf-dist/doc/latex/autoarea/autodemo/autodemo-.pdf
%doc %{_datadir}/texmf-dist/doc/latex/autoarea/autodemo/autodemo-.tex
%doc %{_datadir}/texmf-dist/doc/latex/autoarea/autodemo/autodemo.tex
%{_datadir}/texmf-dist/tex/latex/autoarea/autoarea.sty
