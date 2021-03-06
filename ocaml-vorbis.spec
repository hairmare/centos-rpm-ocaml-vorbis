Name:     ocaml-vorbis

Version:  0.6.2
Release:  1
Summary:  OCaml bindings for libvorbis
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-vorbis
Source0:  https://github.com/savonet/ocaml-vorbis/releases/download/%{version}/ocaml-vorbis-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-ogg
BuildRequires: libvorbis-devel
Requires:      libvorbis

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/vorbis/META
/usr/lib64/ocaml/vorbis/vorbis.a
/usr/lib64/ocaml/vorbis/vorbis.cma
/usr/lib64/ocaml/vorbis/vorbis.cmi
/usr/lib64/ocaml/vorbis/vorbis.cmx
/usr/lib64/ocaml/vorbis/vorbis.cmxa
/usr/lib64/ocaml/vorbis/vorbis.mli
/usr/lib64/ocaml/vorbis/ogg_demuxer_vorbis_decoder.cmi
/usr/lib64/ocaml/vorbis/ogg_demuxer_vorbis_decoder.cmx
/usr/lib64/ocaml/vorbis/ogg_demuxer_vorbis_decoder.mli
/usr/lib64/ocaml/vorbis/libvorbis_stubs.a
/usr/lib64/ocaml/stublibs/dllvorbis_stubs.so
/usr/lib64/ocaml/stublibs/dllvorbis_stubs.so.owner

%description
OCAML bindings for libvorbis


%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-vorbis.spec
