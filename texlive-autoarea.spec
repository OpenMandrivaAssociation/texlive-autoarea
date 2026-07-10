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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package makes PiCTeX recognize lines and arcs in determining the
"bounding box" of a picture. (PiCTeX so far accounted for put commands
only). The "bounding box" is essential for proper placement of a picture
between running text and margins and for keeping the running text away.

