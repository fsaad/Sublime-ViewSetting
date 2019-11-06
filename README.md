# ViewSetting

Sublime text plugin which provides a command to quickly view the value of a
setting in the `Preferences.sublime-settings` file.

### Usage

The following option is available in the command palette `ctrl+shift+p`:

- __View Setting__: A drop-down menu of available Sublime settings
  will be shown. Type the name of the setting to retrieve. The value
  assigned to that setting will be shown in the status bar or as a
  popup.

### Customization

Go to "Preferences" > "Package Settings" > "ViewSetting" > "Settings"
to configure whether the setting values should be shown in the status
bar or in a popup window.

### Installation

Using [Package Control](https://packagecontrol.io/packages/ViewSetting),
type `ctrl+shift+p` > "Package Control: Install Package" > "ViewSetting".

Alternatively, directly clone this repository as follows:

    git clone https://github.com/fsaad/Sublime-ViewSetting ~/.config/sublime-text-3/Packages/ViewSetting
