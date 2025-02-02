pkgname = "libde265"
pkgver = "1.0.11"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-option-checking"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Open H.265 codec implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.libde265.org"
source = f"https://github.com/strukturag/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "0bf84eb1896140d6b5f83cd3302fe03c478a5b8c391f26629b9882c509fc7d04"
hardening = ["!cfi"] # TODO

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")

def post_install(self):
    # do not polute /usr/bin with junk
    for f in [
        "acceleration_speed", "bjoentegaard", "block-rate-estim",
        "gen-enc-table", "hdrcopy", "rd-curves", "tests", "yuv-distortion"
    ]:
        self.rm(self.destdir / "usr/bin" / f)

@subpackage("libde265-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libde265-progs")
def _progs(self):
    return self.default_progs()
