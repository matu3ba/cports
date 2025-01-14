pkgname = "libgcc-chimera"
pkgver = "15.0.7"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release", "-Wno-dev",
    # prevent a bunch of checks
    "-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
    # we want to link it into libgcc_s
    "-DCOMPILER_RT_BUILTINS_HIDE_SYMBOLS=OFF",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    # we are only building builtins
    "-DCOMPILER_RT_BUILD_BUILTINS=ON",
    # disable everything else
    "-DCOMPILER_RT_BUILD_CRT=OFF",
    "-DCOMPILER_RT_BUILD_LIBFUZZER=OFF",
    "-DCOMPILER_RT_BUILD_MEMPROF=OFF",
    "-DCOMPILER_RT_BUILD_PROFILE=OFF",
    "-DCOMPILER_RT_BUILD_SANITIZERS=OFF",
    "-DCOMPILER_RT_BUILD_XRAY=OFF",
    "-DCOMPILER_RT_BUILD_ORC=OFF",
    # simplifies lookup
    "-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON",
]
hostmakedepends = ["cmake", "ninja", "python", "perl", "clang-tools-extra"]
makedepends = [
    "llvm-devel", "zlib-devel", "libffi-devel", "ncurses-devel",
    "libunwind-devel", "linux-headers"
]
pkgdesc = "Chimera shim for libgcc runtime compatibility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "8b5fcb24b4128cf04df1b0b9410ce8b1a729cb3c544e6da885d234280dedeac6"
# shim
options = ["!check", "!lto"]

cmake_dir = "compiler-rt"

_trip = self.profile().triplet
_soname = "libgcc_s.so.1"

configure_args += [
    f"-DCMAKE_ASM_COMPILER_TARGET={_trip}",
    f"-DCMAKE_C_COMPILER_TARGET={_trip}",
    f"-DCMAKE_CXX_COMPILER_TARGET={_trip}",
]

tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC"],
}

def post_build(self):
    from cbuild.util import compiler
    # make a libgcc_s.so.1 from the builtins
    cc = compiler.C(self)
    cc.invoke([], f"build/{_soname}", ldflags = [
        "-nostdlib", "-shared", f"-Wl,-soname,{_soname}",
        "-Wl,--whole-archive", f"build/lib/{_trip}/libclang_rt.builtins.a",
        "-Wl,--no-as-needed", "-lunwind"
    ])

def do_install(self):
    self.install_lib(f"build/{_soname}")
