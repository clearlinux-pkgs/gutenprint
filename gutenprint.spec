#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gutenprint
Version  : 5.3.1
Release  : 4
URL      : https://sourceforge.net/projects/gimp-print/files/gutenprint-5.3/5.3.1/gutenprint-5.3.1.tar.xz
Source0  : https://sourceforge.net/projects/gimp-print/files/gutenprint-5.3/5.3.1/gutenprint-5.3.1.tar.xz
Summary  : Gutenprint Top Quality Printer Drivers
Group    : Development/Tools
License  : GPL-2.0
Requires: gutenprint-bin = %{version}-%{release}
Requires: gutenprint-data = %{version}-%{release}
Requires: gutenprint-lib = %{version}-%{release}
Requires: gutenprint-license = %{version}-%{release}
Requires: gutenprint-locales = %{version}-%{release}
Requires: gutenprint-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : cups
BuildRequires : cups-dev
BuildRequires : cups-filters
BuildRequires : cups-filters-dev
BuildRequires : doxygen
BuildRequires : e2fsprogs-dev
BuildRequires : flex
BuildRequires : ghostscript
BuildRequires : ghostscript-dev
BuildRequires : gnutls-dev
BuildRequires : krb5-dev
BuildRequires : pkgconfig(gimpui-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : readline-dev

%description
Welcome to Gutenprint 5.3.1!  Please read these notes carefully.
that are of interest to distributors and packagers of Gutenprint.
It is not necessary for end users of Gutenprint to read this file.

%package bin
Summary: bin components for the gutenprint package.
Group: Binaries
Requires: gutenprint-data = %{version}-%{release}
Requires: gutenprint-license = %{version}-%{release}
Requires: gutenprint-man = %{version}-%{release}

%description bin
bin components for the gutenprint package.


%package data
Summary: data components for the gutenprint package.
Group: Data

%description data
data components for the gutenprint package.


%package dev
Summary: dev components for the gutenprint package.
Group: Development
Requires: gutenprint-lib = %{version}-%{release}
Requires: gutenprint-bin = %{version}-%{release}
Requires: gutenprint-data = %{version}-%{release}
Provides: gutenprint-devel = %{version}-%{release}

%description dev
dev components for the gutenprint package.


%package lib
Summary: lib components for the gutenprint package.
Group: Libraries
Requires: gutenprint-data = %{version}-%{release}
Requires: gutenprint-license = %{version}-%{release}

%description lib
lib components for the gutenprint package.


%package license
Summary: license components for the gutenprint package.
Group: Default

%description license
license components for the gutenprint package.


%package locales
Summary: locales components for the gutenprint package.
Group: Default

%description locales
locales components for the gutenprint package.


%package man
Summary: man components for the gutenprint package.
Group: Default

%description man
man components for the gutenprint package.


%prep
%setup -q -n gutenprint-5.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545277735
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1545277735
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gutenprint
cp COPYING %{buildroot}/usr/share/package-licenses/gutenprint/COPYING
cp src/cups/COPYING %{buildroot}/usr/share/package-licenses/gutenprint/src_cups_COPYING
%make_install
%find_lang gutenprint

%files
%defattr(-,root,root,-)
/usr/lib/cups/backend/gutenprint53+usb
/usr/lib/cups/driver/gutenprint.5.3
/usr/lib/cups/filter/commandtocanon
/usr/lib/cups/filter/commandtoepson
/usr/lib/cups/filter/rastertogutenprint.5.3
/usr/lib64/gimp/2.0/plug-ins/gutenprint

%files bin
%defattr(-,root,root,-)
/usr/bin/cups-calibrate
/usr/bin/cups-genppd.5.3
/usr/bin/cups-genppdupdate
/usr/bin/escputil
/usr/bin/testpattern

%files data
%defattr(-,root,root,-)
/usr/share/cups/calibrate.ppm
/usr/share/cups/usb/net.sf.gimp-print.usb-quirks
/usr/share/gutenprint/5.3/xml/dither/matrix-1x1.xml
/usr/share/gutenprint/5.3/xml/dither/matrix-2x1.xml
/usr/share/gutenprint/5.3/xml/dither/matrix-4x1.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/artisan.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/b500.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/c120.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/c64.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/c80.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/c82.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/claria.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/claria_xp.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/cmy.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/cmykrb.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/cmykro.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/cx3650.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/defaultblack.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/f360.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/f360_photo.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/f360_photo7_japan.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/f360_ultrachrome.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/f360_ultrachrome_k3.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/f360_ultrachrome_k3v.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/f360_ultrachrome_k3v_2.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/nx100.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/photo_gen0.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/photo_gen1.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/photo_gen2.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/photo_gen3.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/photo_gen3_4.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/photo_gen4.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/photo_pigment.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/picturemate_4.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/picturemate_6.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/pro_gen1.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/pro_gen2.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/pro_pigment.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/pro_ultrachrome.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/pro_ultrachrome_k3.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/pro_ultrachrome_k34.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/pro_ultrachrome_k3v.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/pro_ultrachrome_k3v10.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/pro_ultrachrome_k3v10a.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/pro_ultrachrome_k3v10b.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/pro_ultrachrome_k3v4.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/standard.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/standard_gen0.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/sx445.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/ultrachrome.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/wf40.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/wf500.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/x80.xml
/usr/share/gutenprint/5.3/xml/escp2/inks/xp100.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/artisan.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/b500.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/cd.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/cd_cutter_roll_feed.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/cd_roll_feed.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/cutter_roll_feed.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/default-duplex.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/default.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/pro3880.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/pro_cutter_roll_feed.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/pro_roll_feed.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/r1800.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/r2400.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/r2880.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/rx680.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/rx700.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/spro5000.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/standard_roll_feed.xml
/usr/share/gutenprint/5.3/xml/escp2/inputslots/wf7000.xml
/usr/share/gutenprint/5.3/xml/escp2/media/artisan.xml
/usr/share/gutenprint/5.3/xml/escp2/media/b500.xml
/usr/share/gutenprint/5.3/xml/escp2/media/c120.xml
/usr/share/gutenprint/5.3/xml/escp2/media/c64.xml
/usr/share/gutenprint/5.3/xml/escp2/media/c80.xml
/usr/share/gutenprint/5.3/xml/escp2/media/c82.xml
/usr/share/gutenprint/5.3/xml/escp2/media/claria.xml
/usr/share/gutenprint/5.3/xml/escp2/media/claria1400.xml
/usr/share/gutenprint/5.3/xml/escp2/media/claria_xp.xml
/usr/share/gutenprint/5.3/xml/escp2/media/cmy.xml
/usr/share/gutenprint/5.3/xml/escp2/media/cmykrb.xml
/usr/share/gutenprint/5.3/xml/escp2/media/cmykro.xml
/usr/share/gutenprint/5.3/xml/escp2/media/cx3650.xml
/usr/share/gutenprint/5.3/xml/escp2/media/f360.xml
/usr/share/gutenprint/5.3/xml/escp2/media/f360_photo.xml
/usr/share/gutenprint/5.3/xml/escp2/media/f360_photo7_japan.xml
/usr/share/gutenprint/5.3/xml/escp2/media/f360_ultrachrome.xml
/usr/share/gutenprint/5.3/xml/escp2/media/f360_ultrachrome_k3.xml
/usr/share/gutenprint/5.3/xml/escp2/media/f360_ultrachrome_k3v.xml
/usr/share/gutenprint/5.3/xml/escp2/media/nx100.xml
/usr/share/gutenprint/5.3/xml/escp2/media/photo_gen0.xml
/usr/share/gutenprint/5.3/xml/escp2/media/photo_gen1.xml
/usr/share/gutenprint/5.3/xml/escp2/media/photo_gen2.xml
/usr/share/gutenprint/5.3/xml/escp2/media/photo_gen3.xml
/usr/share/gutenprint/5.3/xml/escp2/media/photo_gen3_4.xml
/usr/share/gutenprint/5.3/xml/escp2/media/photo_gen4.xml
/usr/share/gutenprint/5.3/xml/escp2/media/photo_pigment.xml
/usr/share/gutenprint/5.3/xml/escp2/media/picturemate_4.xml
/usr/share/gutenprint/5.3/xml/escp2/media/picturemate_6.xml
/usr/share/gutenprint/5.3/xml/escp2/media/pro3880_ultrachrome_k3v.xml
/usr/share/gutenprint/5.3/xml/escp2/media/pro_gen1.xml
/usr/share/gutenprint/5.3/xml/escp2/media/pro_gen2.xml
/usr/share/gutenprint/5.3/xml/escp2/media/pro_pigment.xml
/usr/share/gutenprint/5.3/xml/escp2/media/pro_ultrachrome.xml
/usr/share/gutenprint/5.3/xml/escp2/media/pro_ultrachrome_k3.xml
/usr/share/gutenprint/5.3/xml/escp2/media/pro_ultrachrome_k3v.xml
/usr/share/gutenprint/5.3/xml/escp2/media/pro_ultrachrome_k3v10.xml
/usr/share/gutenprint/5.3/xml/escp2/media/pro_ultrachrome_k3v10a.xml
/usr/share/gutenprint/5.3/xml/escp2/media/pro_ultrachrome_k3v10b.xml
/usr/share/gutenprint/5.3/xml/escp2/media/r800.xml
/usr/share/gutenprint/5.3/xml/escp2/media/standard.xml
/usr/share/gutenprint/5.3/xml/escp2/media/standard_gen0.xml
/usr/share/gutenprint/5.3/xml/escp2/media/ultrachrome.xml
/usr/share/gutenprint/5.3/xml/escp2/media/wf500.xml
/usr/share/gutenprint/5.3/xml/escp2/media/x80.xml
/usr/share/gutenprint/5.3/xml/escp2/mediasizes/standard.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/baseline_300.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/baseline_360.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/bx.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/c1xx.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/c2x.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/c4x.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/c7xx.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/c8x.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/c8x_base.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/cpro.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/photo2.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/picmate.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_ultrachrome_k3.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_ultrachrome_k3_base.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_ultrachrome_k3_cutter.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_ultrachrome_k3v.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_ultrachrome_k3v10.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_ultrachrome_k3v10_base.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_ultrachrome_k3v10a.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_ultrachrome_k3v10b.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_x000.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_x500.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_x600.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_x700.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_x800.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/pro_x880.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/r200.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/r240.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/r800.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/sc800.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/sp700.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/sp750.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/sp950.xml
/usr/share/gutenprint/5.3/xml/escp2/model/base/wf7xxx.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_0.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_1.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_10.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_100.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_101.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_102.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_103.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_104.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_105.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_106.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_107.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_108.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_109.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_11.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_110.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_112.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_113.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_114.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_115.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_116.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_117.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_118.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_119.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_12.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_120.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_121.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_122.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_123.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_124.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_125.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_126.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_127.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_128.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_129.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_13.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_130.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_131.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_132.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_14.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_15.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_16.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_17.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_18.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_2.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_20.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_21.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_22.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_23.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_24.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_25.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_26.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_27.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_28.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_29.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_3.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_30.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_31.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_32.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_34.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_35.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_36.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_37.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_38.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_39.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_4.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_40.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_41.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_42.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_43.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_44.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_45.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_46.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_47.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_48.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_49.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_5.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_50.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_51.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_52.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_53.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_54.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_55.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_56.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_57.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_58.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_6.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_60.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_61.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_62.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_63.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_64.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_65.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_66.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_67.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_68.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_69.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_7.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_70.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_71.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_72.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_73.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_74.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_75.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_76.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_77.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_78.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_79.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_8.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_80.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_81.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_82.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_83.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_84.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_85.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_86.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_87.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_88.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_89.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_9.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_90.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_91.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_92.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_93.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_94.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_95.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_96.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_97.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_98.xml
/usr/share/gutenprint/5.3/xml/escp2/model/model_99.xml
/usr/share/gutenprint/5.3/xml/escp2/qualitypresets/p1_5.xml
/usr/share/gutenprint/5.3/xml/escp2/qualitypresets/picturemate.xml
/usr/share/gutenprint/5.3/xml/escp2/qualitypresets/prox900.xml
/usr/share/gutenprint/5.3/xml/escp2/qualitypresets/standard.xml
/usr/share/gutenprint/5.3/xml/escp2/qualitypresets/v2880.xml
/usr/share/gutenprint/5.3/xml/escp2/qualitypresets/wf40.xml
/usr/share/gutenprint/5.3/xml/escp2/resolutions/c8x.xml
/usr/share/gutenprint/5.3/xml/escp2/resolutions/escp2-i.xml
/usr/share/gutenprint/5.3/xml/escp2/resolutions/prox600.xml
/usr/share/gutenprint/5.3/xml/escp2/resolutions/sc480.xml
/usr/share/gutenprint/5.3/xml/escp2/resolutions/sc680.xml
/usr/share/gutenprint/5.3/xml/escp2/resolutions/sc740.xml
/usr/share/gutenprint/5.3/xml/escp2/resolutions/sc860.xml
/usr/share/gutenprint/5.3/xml/escp2/resolutions/sp700.xml
/usr/share/gutenprint/5.3/xml/escp2/resolutions/sp720.xml
/usr/share/gutenprint/5.3/xml/escp2/resolutions/wf6xx.xml
/usr/share/gutenprint/5.3/xml/escp2/weaves/pro7000.xml
/usr/share/gutenprint/5.3/xml/escp2/weaves/pro7500.xml
/usr/share/gutenprint/5.3/xml/escp2/weaves/pro7600.xml
/usr/share/gutenprint/5.3/xml/escp2/weaves/standard.xml
/usr/share/gutenprint/5.3/xml/papers/labels.xml
/usr/share/gutenprint/5.3/xml/papers/standard.xml
/usr/share/gutenprint/5.3/xml/printers/canon.xml
/usr/share/gutenprint/5.3/xml/printers/dpl.xml
/usr/share/gutenprint/5.3/xml/printers/dyesub.xml
/usr/share/gutenprint/5.3/xml/printers/escp2.xml
/usr/share/gutenprint/5.3/xml/printers/lexmark.xml
/usr/share/gutenprint/5.3/xml/printers/pcl.xml
/usr/share/gutenprint/5.3/xml/printers/ps.xml
/usr/share/gutenprint/5.3/xml/printers/raw.xml
/usr/share/gutenprint/doc/AUTHORS
/usr/share/gutenprint/doc/COPYING
/usr/share/gutenprint/doc/ChangeLog
/usr/share/gutenprint/doc/FAQ.html
/usr/share/gutenprint/doc/NEWS
/usr/share/gutenprint/doc/README
/usr/share/gutenprint/doc/gutenprint-users-manual.odt
/usr/share/gutenprint/doc/gutenprint-users-manual.pdf
/usr/share/gutenprint/doc/gutenprint.pdf
/usr/share/gutenprint/doc/reference-html/book1.html
/usr/share/gutenprint/doc/reference-html/c1714.html
/usr/share/gutenprint/doc/reference-html/c193.html
/usr/share/gutenprint/doc/reference-html/c1965.html
/usr/share/gutenprint/doc/reference-html/c199.html
/usr/share/gutenprint/doc/reference-html/c38.html
/usr/share/gutenprint/doc/reference-html/c463.html
/usr/share/gutenprint/doc/reference-html/c47.html
/usr/share/gutenprint/doc/reference-html/docbook.css
/usr/share/gutenprint/doc/reference-html/f14.html
/usr/share/gutenprint/doc/reference-html/gpl-terms.html
/usr/share/gutenprint/doc/reference-html/gpl.html
/usr/share/gutenprint/doc/reference-html/ln10.html
/usr/share/gutenprint/doc/reference-html/x1666.html
/usr/share/gutenprint/doc/reference-html/x1731.html
/usr/share/gutenprint/doc/reference-html/x270.html
/usr/share/gutenprint/doc/reference-html/x66.html
/usr/share/gutenprint/doc/reference-html/x78.html
/usr/share/gutenprint/doc/reference-html/x952.html
/usr/share/gutenprint/samples/colorbars4.png
/usr/share/gutenprint/samples/colorsweep.png
/usr/share/gutenprint/samples/extended.sample
/usr/share/gutenprint/samples/profile.jpg
/usr/share/gutenprint/samples/testpattern.sample
/usr/share/locale/ca/gutenprint_ca.po
/usr/share/locale/cs/gutenprint_cs.po
/usr/share/locale/da/gutenprint_da.po
/usr/share/locale/de/gutenprint_de.po
/usr/share/locale/el/gutenprint_el.po
/usr/share/locale/en_GB/gutenprint_en_GB.po
/usr/share/locale/es/gutenprint_es.po
/usr/share/locale/fi/gutenprint_fi.po
/usr/share/locale/fr/gutenprint_fr.po
/usr/share/locale/gl/gutenprint_gl.po
/usr/share/locale/hu/gutenprint_hu.po
/usr/share/locale/it/gutenprint_it.po
/usr/share/locale/ja/gutenprint_ja.po
/usr/share/locale/nb/gutenprint_nb.po
/usr/share/locale/nl/gutenprint_nl.po
/usr/share/locale/pl/gutenprint_pl.po
/usr/share/locale/pt/gutenprint_pt.po
/usr/share/locale/ru/gutenprint_ru.po
/usr/share/locale/sk/gutenprint_sk.po
/usr/share/locale/sl/gutenprint_sl.po
/usr/share/locale/sv/gutenprint_sv.po
/usr/share/locale/tr/gutenprint_tr.po
/usr/share/locale/uk/gutenprint_uk.po
/usr/share/locale/vi/gutenprint_vi.po
/usr/share/locale/zh_CN/gutenprint_zh_CN.po
/usr/share/locale/zh_TW/gutenprint_zh_TW.po

%files dev
%defattr(-,root,root,-)
/usr/include/gutenprint/array.h
/usr/include/gutenprint/bit-ops.h
/usr/include/gutenprint/channel.h
/usr/include/gutenprint/color.h
/usr/include/gutenprint/curve-cache.h
/usr/include/gutenprint/curve.h
/usr/include/gutenprint/dither.h
/usr/include/gutenprint/gutenprint-module.h
/usr/include/gutenprint/gutenprint-version.h
/usr/include/gutenprint/gutenprint.h
/usr/include/gutenprint/image.h
/usr/include/gutenprint/list.h
/usr/include/gutenprint/module.h
/usr/include/gutenprint/mxml.h
/usr/include/gutenprint/paper.h
/usr/include/gutenprint/path.h
/usr/include/gutenprint/printers.h
/usr/include/gutenprint/refcache.h
/usr/include/gutenprint/sequence.h
/usr/include/gutenprint/string-list.h
/usr/include/gutenprint/types.h
/usr/include/gutenprint/util.h
/usr/include/gutenprint/vars.h
/usr/include/gutenprint/weave.h
/usr/include/gutenprint/xml.h
/usr/include/gutenprintui2/curve.h
/usr/include/gutenprintui2/gammacurve.h
/usr/include/gutenprintui2/gutenprintui.h
/usr/include/gutenprintui2/typebuiltins.h
/usr/lib64/libgutenprint.so
/usr/lib64/libgutenprintui2.so
/usr/lib64/pkgconfig/gutenprint.pc
/usr/lib64/pkgconfig/gutenprintui2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/gutenprint/5.3/modules/color-traditional.so
/usr/lib64/gutenprint/5.3/modules/print-canon.so
/usr/lib64/gutenprint/5.3/modules/print-dpl.so
/usr/lib64/gutenprint/5.3/modules/print-dyesub.so
/usr/lib64/gutenprint/5.3/modules/print-escp2.so
/usr/lib64/gutenprint/5.3/modules/print-lexmark.so
/usr/lib64/gutenprint/5.3/modules/print-pcl.so
/usr/lib64/gutenprint/5.3/modules/print-ps.so
/usr/lib64/gutenprint/5.3/modules/print-raw.so
/usr/lib64/libgutenprint.so.8
/usr/lib64/libgutenprint.so.8.1.0
/usr/lib64/libgutenprintui2.so.1
/usr/lib64/libgutenprintui2.so.1.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gutenprint/COPYING
/usr/share/package-licenses/gutenprint/src_cups_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/escputil.1
/usr/share/man/man8/cups-calibrate.8
/usr/share/man/man8/cups-genppd.8
/usr/share/man/man8/cups-genppdupdate.8

%files locales -f gutenprint.lang
%defattr(-,root,root,-)

