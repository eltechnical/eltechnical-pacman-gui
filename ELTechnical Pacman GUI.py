import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget, QAbstractItemView, QHBoxLayout, QComboBox, QMessageBox
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QKeyEvent


class ELTechnicalPacmanGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ELTechnical Pacman GUI')
        self.setGeometry(100, 100, 500, 600)

        self.layout = QVBoxLayout()

        self.label = QLabel("Select well-known packages to install:")
        self.layout.addWidget(self.label)

        # Expanded list of well-known programs (without drivers or hardware-specific apps)
        self.well_known_packages = [
            "gedit", "firefox", "vlc", "libreoffice", "gimp", "atom", "visual-studio-code",
            "chromium", "mpv", "thunderbird", "blender", "inkscape", "obs-studio", "spotify",
            "docker", "virtualbox", "git", "code", "xterm", "krita", "audacity", "pycharm",
            "filezilla", "thunar", "skypeforlinux", "teamviewer", "slack", "zoom", "electron",
            "sublime-text", "steam", "discord", "telegram-desktop", "telegram", "postman", "java",
            "python", "nodejs", "npm", "ruby", "go", "clang", "gitkraken", "insomnia", "kdenlive", 
            "intellij-idea", "pinta", "libreoffice-fresh"
        ]

        # ListWidget for displaying well-known programs
        self.package_list = QListWidget()
        self.package_list.addItems(self.well_known_packages)
        self.package_list.setSelectionMode(QAbstractItemView.MultiSelection)  # Allow multi-selection
        self.layout.addWidget(self.package_list)

        # Layout for the installer selection
        self.installer_layout = QHBoxLayout()

        self.installer_label = QLabel("Select package manager:")
        self.installer_layout.addWidget(self.installer_label)

        # Dropdown for selecting the installer (yay or pacman)
        self.installer_selector = QComboBox()
        self.installer_selector.addItem("pacman")
        self.installer_selector.addItem("yay")
        self.installer_layout.addWidget(self.installer_selector)

        self.layout.addLayout(self.installer_layout)

        # Install button
        self.install_button = QPushButton('Install Selected Apps')
        self.install_button.clicked.connect(self.install_packages)
        self.layout.addWidget(self.install_button)

        self.setLayout(self.layout)

        # Flag to track Ctrl key press
        self.ctrl_held = False

        # To handle ctrl key for selection manually
        self.package_list.setFocusPolicy(Qt.StrongFocus)  # Make sure the list can receive focus
        self.package_list.installEventFilter(self)

    def eventFilter(self, source, event):
        if source == self.package_list:
            if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Control:
                self.ctrl_held = True
            elif event.type() == QEvent.KeyRelease and event.key() == Qt.Key_Control:
                self.ctrl_held = False

        return super().eventFilter(source, event)

    def install_packages(self):
        selected_items = self.package_list.selectedItems()

        # Ensure that the user selects at least one app
        if not selected_items:
            QMessageBox.warning(self, "No Package Selected", "Please select at least one package to install.")
            return

        # Display the password prompt
        if not self.prompt_for_password():
            return

        installer = self.installer_selector.currentText()

        # Iterate through selected items and install them
        for item in selected_items:
            app_name = item.text()
            success = self.try_install(app_name, installer)
            if success:
                QMessageBox.information(self, "Installation Success", f"{app_name} has been successfully installed!")
            else:
                QMessageBox.critical(self, "Installation Failed", f"Failed to install {app_name}.")

    def prompt_for_password(self):
        # Trigger a graphical password prompt using pkexec (without needing a terminal)
        try:
            result = subprocess.run(
                ["pkexec", "--disable-internal-agent", "echo", "Password Required"], 
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return True
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Authentication Failed", "Password authentication failed. Please try again.")
            return False

    def try_install(self, app_name, installer):
        command = []

        if installer == "yay":
            command = f"pkexec yay -S --noconfirm {app_name}"
        elif installer == "pacman":
            command = f"pkexec pacman -S --noconfirm {app_name}"

        try:
            result = subprocess.run(
                command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            return True
        except subprocess.CalledProcessError as e:
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ELTechnicalPacmanGUI()
    window.show()
    sys.exit(app.exec_())
