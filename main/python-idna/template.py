pkgname = "python-idna"
pkgver = "3.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Internationalized Domain Names in Applications (IDNA) for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/kjd/idna"
source = f"$(PYPI_SITE)/i/idna/idna-{pkgver}.tar.gz"
sha256 = "467fbad99067910785144ce333826c71fb0e63a425657295239737f7ecd125f3"

def post_install(self):
    self.install_license("LICENSE.md")
