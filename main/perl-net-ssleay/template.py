pkgname = "perl-net-ssleay"
pkgver = "1.92"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl", "openssl"]
makedepends = ["perl", "zlib-devel", "openssl-devel"]
depends = ["perl"]
pkgdesc = "Perl extension for using OpenSSL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-2.0"
url = "https://metacpan.org/release/Net-SSLeay"
source = f"$(CPAN_SITE)/Net/Net-SSLeay-{pkgver}.tar.gz"
sha256 = "47c2f2b300f2e7162d71d699f633dd6a35b0625a00cbda8c50ac01144a9396a9"
# missing checkdepends
options = ["!check"]

if self.profile().arch == "riscv64":
    # ld: error: section size decrease is too large
    tool_flags = {"CFLAGS": ["-mno-relax"]}
