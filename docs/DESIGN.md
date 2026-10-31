# 🎨 Design System
### Qwen2.5-Coder — Clean. Simple. Productive.

> This document defines the visual design system, UI components, color palette, typography tokens, and telemetry UX guidelines for the **Qwen2.5-Coder Autonomous AI Code Generation Engine**. The goal is to create a modern, minimal, developer-friendly interface with consistent look and feel across terminal outputs, interactive notebooks, and web dashboards.

---

### 1. Design Principles

<table>
  <tr>
    <td width="25%" style="background-color: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 14px;">
      <div style="font-size: 20px; margin-bottom: 6px;">👥</div>
      <div style="color: #60a5fa; font-weight: bold; font-size: 13px;">User-Centered</div>
      <div style="color: #9ca3af; font-size: 11px; margin-top: 4px;">Immediate, intuitive error tracebacks and one-click code generation.</div>
    </td>
    <td width="25%" style="background-color: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 14px;">
      <div style="font-size: 20px; margin-bottom: 6px;">🍃</div>
      <div style="color: #34d399; font-weight: bold; font-size: 13px;">Minimal & Clean</div>
      <div style="color: #9ca3af; font-size: 11px; margin-top: 4px;">Zero visual clutter; focus strictly on code diffs, test asserts, and execution states.</div>
    </td>
    <td width="25%" style="background-color: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 14px;">
      <div style="font-size: 20px; margin-bottom: 6px;">🧱</div>
      <div style="color: #a78bfa; font-weight: bold; font-size: 13px;">Consistent</div>
      <div style="color: #9ca3af; font-size: 11px; margin-top: 4px;">Unified badges, terminal formatting, and status codes across the entire stack.</div>
    </td>
    <td width="25%" style="background-color: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 14px;">
      <div style="font-size: 20px; margin-bottom: 6px;">♿</div>
      <div style="color: #38bdf8; font-weight: bold; font-size: 13px;">Accessible</div>
      <div style="color: #9ca3af; font-size: 11px; margin-top: 4px;">High-contrast syntax highlighting compliant with WCAG 2.1 AA standards.</div>
    </td>
  </tr>
</table>

---

### 2. Color Palette
*Primary colors used across the application, terminal logs, and web telemetry:*

<table>
  <tr>
    <td width="12.5%" align="center">
      <div style="background-color: #6366F1; height: 38px; border-radius: 6px; margin-bottom: 6px;"></div>
      <b style="font-size: 11px;">Primary</b><br>
      <code style="font-size: 10px; color: #94a3b8;">#6366F1</code>
    </td>
    <td width="12.5%" align="center">
      <div style="background-color: #8B5CF6; height: 38px; border-radius: 6px; margin-bottom: 6px;"></div>
      <b style="font-size: 11px;">Secondary</b><br>
      <code style="font-size: 10px; color: #94a3b8;">#8B5CF6</code>
    </td>
    <td width="12.5%" align="center">
      <div style="background-color: #10B981; height: 38px; border-radius: 6px; margin-bottom: 6px;"></div>
      <b style="font-size: 11px;">Success</b><br>
      <code style="font-size: 10px; color: #94a3b8;">#10B981</code>
    </td>
    <td width="12.5%" align="center">
      <div style="background-color: #F59E0B; height: 38px; border-radius: 6px; margin-bottom: 6px;"></div>
      <b style="font-size: 11px;">Warning</b><br>
      <code style="font-size: 10px; color: #94a3b8;">#F59E0B</code>
    </td>
    <td width="12.5%" align="center">
      <div style="background-color: #EF4444; height: 38px; border-radius: 6px; margin-bottom: 6px;"></div>
      <b style="font-size: 11px;">Error</b><br>
      <code style="font-size: 10px; color: #94a3b8;">#EF4444</code>
    </td>
    <td width="12.5%" align="center">
      <div style="background-color: #0F172A; border: 1px solid #334155; height: 38px; border-radius: 6px; margin-bottom: 6px;"></div>
      <b style="font-size: 11px;">Background</b><br>
      <code style="font-size: 10px; color: #94a3b8;">#0F172A</code>
    </td>
    <td width="12.5%" align="center">
      <div style="background-color: #1E293B; border: 1px solid #475569; height: 38px; border-radius: 6px; margin-bottom: 6px;"></div>
      <b style="font-size: 11px;">Surface</b><br>
      <code style="font-size: 10px; color: #94a3b8;">#1E293B</code>
    </td>
    <td width="12.5%" align="center">
      <div style="background-color: #F8FAFC; height: 38px; border-radius: 6px; margin-bottom: 6px;"></div>
      <b style="font-size: 11px;">Text Primary</b><br>
      <code style="font-size: 10px; color: #94a3b8;">#F8FAFC</code>
    </td>
  </tr>
</table>

---

### 3. Typography
*We use JetBrains Mono for syntax-highlighted code and Inter for clean, modern interfaces:*

<table>
  <tr>
    <td width="80" align="center" style="font-size: 40px; font-weight: bold; background-color: #1e293b; color: #f8fafc; border-radius: 8px;">Aa</td>
    <td style="padding-left: 16px;">
      <b style="font-size: 16px; color: #f8fafc;">Inter & JetBrains Mono</b><br>
      <span style="color: #94a3b8; font-size: 12px;">Primary interface and high-legibility monospace fonts for syntax trees, stack traces, and code diffs.</span>
    </td>
  </tr>
</table>

| Element | Font Family | Size | Weight | Line Height |
| :-- | :-- | :-: | :-: | :-: |
| **Heading 1 (H1)** | Inter | 24px (1.5rem) | 700 Bold | 1.3 |
| **Heading 2 (H2)** | Inter | 18px (1.125rem) | 600 Semi-Bold | 1.4 |
| **Heading 3 (H3)** | Inter | 14px (0.875rem) | 600 Semi-Bold | 1.4 |
| **Body Text** | Inter | 13px (0.8125rem) | 400 Regular | 1.6 |
| **Code & Traces** | JetBrains Mono | 12px (0.75rem) | 400 Regular / 600 Bold | 1.6 |
| **Badges & Labels**| Inter | 11px (0.6875rem) | 700 Bold | 1.2 |

---

### 4. UI Components

#### Interactive Buttons
<div style="margin: 10px 0;">
  <span style="background-color: #6366F1; color: white; padding: 6px 16px; border-radius: 6px; font-weight: bold; font-size: 12px; margin-right: 8px;">Generate Solution</span>
  <span style="background-color: #1E293B; color: #e2e8f0; border: 1px solid #475569; padding: 6px 16px; border-radius: 6px; font-weight: bold; font-size: 12px; margin-right: 8px;">Run Sandbox Tests</span>
  <span style="background-color: #EF4444; color: white; padding: 6px 16px; border-radius: 6px; font-weight: bold; font-size: 12px;">Abort Subprocess</span>
</div>

#### Execution Status Badges
<div style="margin: 10px 0;">
  <span style="background-color: #059669; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: bold; margin-right: 6px;">✓ PASS</span>
  <span style="background-color: #dc2626; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: bold; margin-right: 6px;">✕ RUNTIME_ERROR</span>
  <span style="background-color: #d97706; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: bold; margin-right: 6px;">⟳ RETRY (1/2)</span>
  <span style="background-color: #7c3aed; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: bold;">⚡ LORA ACTIVE</span>
</div>

#### Terminal Execution Card Mockup
```text
+---------------------------------------------------------------------------------+
|  Qwen2.5-Coder Sandbox Telemetry                             [ PASS (0.42s) ]   |
+---------------------------------------------------------------------------------+
|  Problem: "Write a function to find maximum subarray sum (Kadane's Algo)"       |
|  Function Name: max_sub_array_sum                                               |
|                                                                                 |
|  >>> Code Implementation:                                                       |
|  1 | def max_sub_array_sum(arr):                                                |
|  2 |     max_so_far = current_max = arr[0]                                      |
|  3 |     for x in arr[1:]:                                                      |
|  4 |         current_max = max(x, current_max + x)                              |
|  5 |         max_so_far = max(max_so_far, current_max)                          |
|  6 |     return max_so_far                                                      |
|                                                                                 |
|  >>> Test Suite Assertions:                                                     |
|  [✓] assert max_sub_array_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6             |
|  [✓] assert max_sub_array_sum([1]) == 1                                         |
|  [✓] assert max_sub_array_sum([5, 4, -1, 7, 8]) == 23                          |
+---------------------------------------------------------------------------------+
```
