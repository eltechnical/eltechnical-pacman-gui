# Maintainer: ELTechnical
pkgname=eltechnical-pacman-gui
pkgver=1.0.0
pkgrel=1
pkgdesc="A Qt-based GUI frontend for pacman with a list of well-known apps to install."
arch=('any')
url="https://github.com/eltechnical/eltechnical-pacman-gui"
license=('none')
depends=('python' 'python-pyqt5')
source=("ELTechnical Pacman GUI.py")
sha256sums=('SKIP')

package() {
  install -Dm755 "$srcdir/ELTechnical Pacman GUI.py" "$pkgdir/usr/bin/eltechnical-pacman-gui"
}

