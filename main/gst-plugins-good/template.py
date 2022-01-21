pkgname = "gst-plugins-good"
pkgver = "1.18.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--auto-feature=enabled",
    "-Ddefault_library=shared",
    "-Dglib-asserts=disabled",
    "-Dglib-checks=disabled",
    "-Dgobject-cast-checks=disabled",
    "-Dexamples=disabled",
    "-Ddoc=disabled",
    # there are too many auto features and it's difficult to take care that
    # nothing is accidentally disabled and so on, so implicitly enable all,
    # and then disable what's not relevant to us:
    "-Ddirectsound=disabled",
    "-Dosxaudio=disabled",
    "-Dosxvideo=disabled",
    "-Doss=disabled",
    "-Doss4=disabled",
    "-Dwaveform=disabled",
    "-Drpicamsrc=disabled", # proprietary
    "-Dspeex=disabled", # obsolete, replaced by opus
    "-Dximagesrc=disabled", # maybe? probably obsolete
    "-Daalib=disabled", # old and obsolete
    "-Ddv=disabled", # maybe?
    "-Ddv1394=disabled", # maybe?
    "-Dqt5=disabled", # no qt5 in main, maybe package separately?
    "-Dshout2=disabled", # TODO
    "-Dsoup=disabled", # TODO for gst 1.20 where libsoup3 is stable
]
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny", "glib-devel", "orc",
]
makedepends = [
    "gstreamer-devel", "gst-plugins-base-devel", "libpng-devel", "gtk+3-devel",
    "gdk-pixbuf-devel", "libbz2-devel", "libxml2-devel", "libgudev-devel",
    "v4l-utils-devel", "libcaca-devel", "pipewire-jack-devel", "wavpack-devel",
    "taglib-devel", "libvpx-devel", "flac-devel", "mpg123-devel", "lame-devel",
    "twolame-devel", "libpulse-devel", "orc-devel",
]
checkdepends = ["pipewire"]
depends = [f"gst-plugins-base>={pkgver}"]
pkgdesc = "GStreamer good plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3aaeeea7765fbf8801acce4a503a9b05f73f04e8a35352e9d00232cfd555796b"
# 4 out of 105 tests currently fail, one is qtmux (just disable), debug others
options = ["!check"]