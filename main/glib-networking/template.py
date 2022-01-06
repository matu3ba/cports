pkgname = "glib-networking"
pkgver = "2.70.1"
pkgrel = 0
build_style = "meson"
# use gnutls for the time being, as openssl module is broken with 3.x,
# and i'm not sure why (webkit tls connections do not work)
configure_args = [
    "-Dgnutls=enabled", "-Dopenssl=disabled", "-Dlibproxy=enabled",
    "-Dgnome_proxy=enabled"
]
hostmakedepends = [
    "meson", "pkgconf", "ca-certificates", "gettext-tiny"
]
makedepends = [
    "gnutls-devel", "gsettings-desktop-schemas-devel",
    "libglib-devel", "libproxy-devel"
]
depends = ["gsettings-desktop-schemas"]
checkdepends = ["glib"]
pkgdesc = "Network extensions for glib"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/glib-networking"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2a16bfc2d271ccd3266e3fb462bc8a4103c02e81bbb339aa92d6fb060592d7bc"

def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive = True)