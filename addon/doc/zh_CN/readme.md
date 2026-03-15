# WinForms .NET 4.8 修复

这是一个 NVDA 插件原型，旨在恢复 .NET 4.8 Windows Forms 应用程序中缺失的核心辅助功能信息。

## 目的

本插件是针对以下问题的**概念验证实现**：
- [Issue #17454](https://github.com/nvaccess/nvda/issues/17454) - 组合框在折叠状态下无法读出选项改变。
- [Issue #19335](https://github.com/nvaccess/nvda/issues/19335) - ToolStripMenuItem 未读出选中状态。
- 修复了 WinForms ToolStripMenuItems 缺失辅助功能描述的问题。

## 功能

- **组合框导航修复**：确保在折叠的 .NET WinForms 组合框中使用方向键切换选项时，NVDA 能够正常读出当前选中项。
- **菜单项选中状态修复**：为缺失 UIA TogglePattern 的 ToolStripMenuItems 补齐选中状态信息。
- **菜单项辅助功能描述修复**：通过回退到传统（Legacy）属性，恢复 ToolStripMenuItems 缺失的辅助功能描述信息。

## 配置

**本插件没有设置选项。** 当检测到目标 .NET 4.8 WinForms 控件时，它会自动生效。
