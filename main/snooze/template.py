pkgname = "snooze"
pkgver = "0.5"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Run a command at a particular time"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://github.com/leahneukirchen/snooze"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d63fde85d9333188bed5996baabd833eaa00842ce117443ffbf8719c094be414"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]