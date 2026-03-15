# WinForms .NET 4.8 Fixes

A prototype NVDA add-on that restores essential accessibility reporting for .NET 4.8 Windows Forms applications.

## Purpose

This add-on is a **proof-of-concept implementation** for:
- [Issue #17454](https://github.com/nvaccess/nvda/issues/17454) - ComboBox selection not reported when collapsed.
- [Issue #19335](https://github.com/nvaccess/nvda/issues/19335) - ToolStripMenuItem checked state not reported.
- Missing description reporting for WinForms ToolStripMenuItems.

## Features

- **ComboBox Navigation Fix**: Ensures that selection changes are announced when using arrow keys in a collapsed .NET WinForms ComboBox.
- **MenuItem Checked State Fix**: Restores reporting of the "Checked" and "Unchecked" status when navigating ToolStripMenuItems that lack the UIA TogglePattern.
- **MenuItem Description Fix**: Restores reporting of accessibility descriptions for ToolStripMenuItems by falling back to legacy properties.

## Configuration

**This add-on has no settings.**
