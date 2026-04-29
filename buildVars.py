# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries, SpeechDictionaries

# Since some strings in `addon_info` are translatable,
# we need to include them in the .po files.
# Gettext recognizes only strings given as parameters to the `_` function.
# To avoid initializing translations in this module we simply import a "fake" `_` function
# which returns whatever is given to it as an argument.
from site_scons.site_tools.NVDATool.utils import _

# Add-on information variables
addon_info = AddonInfo(
	# add-on Name/identifier, internal for NVDA
	addon_name="winFormsNet48Fixes",
	# Add-on summary/title, usually the user visible name of the add-on
	addon_summary=_("WinForms .NET 4.8 Fixes"),
	# Add-on description
	addon_description=_("""Consolidated accessibility fixes for .NET 4.8 WinForms applications, including ComboBox navigation and MenuItem checked state reporting."""),
	# version
	addon_version="0.2.0",
	# Brief changelog for this version
	addon_changelog=_("""### 0.2.0
* Restored missing MenuItem description reporting by falling back to legacy properties.
### 0.1.0
* Initial release.
* Fixed ComboBox selection reporting while collapsed (#17454).
* Fixed ToolStripMenuItem missing checked state reporting (#19335)."""),
	# Author(s)
	addon_author="Cary-rowen <manchen_0528@outlook.com>",
	# URL for the add-on documentation support
	addon_url="https://github.com/cary-rowen/winFormsNet48Fixes",
	# URL for the add-on repository where the source code can be found
	addon_sourceURL="https://github.com/cary-rowen/winFormsNet48Fixes",
	# Documentation file name
	addon_docFileName="readme.html",
	# Minimum NVDA version supported
	addon_minimumNVDAVersion="2023.1.0",
	# Last NVDA version supported/tested
	addon_lastTestedNVDAVersion="2025.3.3",
	# Add-on update channel
	addon_updateChannel=None,
	# Add-on license
	addon_license="GPL v2",
	# URL for the license document
	addon_licenseURL="https://www.gnu.org/licenses/gpl-2.0.html",
)

# Define the python files that are the sources of your add-on.
pythonSources: list[str] = ["addon/globalPlugins/winFormsNet48Fixes/*.py"]

# Files that contain strings for translation. Usually your python sources
i18nSources: list[str] = pythonSources + ["buildVars.py"]

excludedFiles: list[str] = []
baseLanguage: str = "en"
markdownExtensions: list[str] = ["markdown.extensions.tables"]
brailleTables: BrailleTables = {}

# Custom speech symbol dictionaries
# Symbol dictionary files reside in the locale folder, e.g. `locale\en`, and are named `symbols-<name>.dic`.
# If your add-on includes custom speech symbol dictionaries (most will not), fill out this dictionary.
# Each key is the name of the dictionary,
# with keys inside recording the following attributes:
# displayName (name of the speech dictionary shown to users and translatable),
# mandatory (True when always enabled, False when not).
symbolDictionaries: SymbolDictionaries = {}

# Custom speech dictionaries (distinct from symbol dictionaries above)
# Speech dictionary files reside in the speechDicts folder and are named `name.dic`.
# If your add-on includes custom speech (pronunciation) dictionaries (most will not), fill out this dictionary.
# Each key is the name of the dictionary,
# with keys inside recording the following attributes:
# displayName (name of the speech dictionary shown to users and translatable),
# mandatory (True when always enabled, False when not).
speechDictionaries: SpeechDictionaries = {}
