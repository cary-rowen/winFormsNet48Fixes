# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2026 Cary-rowen <manchen_0528@outlook.com>
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
#
# Fixes:
# https://github.com/nvaccess/nvda/issues/19335 (Checked state reporting)
# https://github.com/nvaccess/nvda/issues/17454 (ComboBox navigation)
# Also fixes missing description reporting for WinForms ToolStripMenuItems.

from __future__ import annotations
from collections.abc import Callable
from typing import Any
from comtypes import COMError
import api
import controlTypes
import globalPluginHandler
import eventHandler
import UIAHandler
import oleacc
from NVDAObjects.UIA import UIA, MenuItem


class WinFormsMenuItem(MenuItem):
	"""Overlay class for .NET 4.8 WinForms ToolStripMenuItems."""

	def _get_states(self) -> set[int]:
		states = super()._get_states()
		# Fallback to LegacyIAccessiblePattern to retrieve the real checked state.
		try:
			accState = self.UIAElement.GetCurrentPropertyValue(
				UIAHandler.UIA_LegacyIAccessibleStatePropertyId,
			)
			if accState & oleacc.STATE_SYSTEM_CHECKED:
				states.add(controlTypes.State.CHECKABLE)
				states.add(controlTypes.State.CHECKED)
		except COMError:
			pass
		return states

	def _get_description(self) -> str | None:
		description = super()._get_description()
		if description:
			return description
		# Retrieve directly from LegacyIAccessibleDescription property.
		try:
			return self.UIAElement.GetCurrentPropertyValue(
				UIAHandler.UIA_LegacyIAccessibleDescriptionPropertyId,
			)
		except COMError:
			return None


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	"""Consolidated fixes for .NET 4.8 WinForms ComboBoxes and MenuItems."""

	def _isWinForms48(self, obj: Any, role: controlTypes.Role) -> bool:
		"""Identifies target controls using window class and UIA provider info."""
		if not isinstance(obj, UIA) or obj.role != role:
			return False
		wClass = obj.windowClassName
		if not wClass.startswith("WindowsForms10"):
			return False
		if role == controlTypes.Role.COMBOBOX and ".COMBOBOX" not in wClass:
			return False
		desc = obj.UIAElement.cachedProviderDescription or ""
		if "Version=4.0" not in desc or "System.Windows.Forms" not in desc:
			return False
		if role == controlTypes.Role.MENUITEM and "ToolStripMenuItem" not in desc:
			return False
		return True

	def chooseNVDAObjectOverlayClasses(self, obj: UIA, clsList: list[type]) -> None:
		if self._isWinForms48(obj, controlTypes.Role.MENUITEM):
			clsList.insert(0, WinFormsMenuItem)

	def event_UIA_elementSelected(self, obj: UIA, nextHandler: Callable[[], None]) -> None:
		nextHandler()
		if obj.role != controlTypes.Role.LISTITEM:
			return
		focus = api.getFocusObject()
		if self._isWinForms48(focus, controlTypes.Role.COMBOBOX):
			focus.event_valueChange()

	def event_gainFocus(self, obj: UIA, nextHandler: Callable[[], None]) -> None:
		nextHandler()
		if self._isWinForms48(obj, controlTypes.Role.COMBOBOX):
			eventHandler.requestEvents("UIA_elementSelected", obj.processID, "ComboLBox")
