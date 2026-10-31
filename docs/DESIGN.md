# Design System
### Qwen2.5-Coder — Clean. Simple. Productive.

This document defines the visual design system: UI components, design tokens, and user experience guidelines for the **Qwen2.5-Coder** software engineering system. The goal is to establish a modern, minimal, developer-friendly interface with consistent styling across terminal outputs, interactive notebooks, and web dashboards.

---

### 1. Design Principles

<table width="100%" cellpadding="0" cellspacing="8" border="0">
  <tr>
    <td width="25%" style="background-color: #0F172A; border: 1px solid #1E293B; border-radius: 8px; padding: 18px 14px;">
      <div style="color: #60A5FA; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 0.04em;">User-Centered</div>
      <div style="color: #94A3B8; font-size: 12px; margin-top: 6px; line-height: 1.5;">Simple and intuitive for developers; instant error tracebacks and one-click execution.</div>
    </td>
    <td width="25%" style="background-color: #0F172A; border: 1px solid #1E293B; border-radius: 8px; padding: 18px 14px;">
      <div style="color: #34D399; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 0.04em;">Minimal & Clean</div>
      <div style="color: #94A3B8; font-size: 12px; margin-top: 6px; line-height: 1.5;">Reduce clutter and focus strictly on code diffs, test assertions, and runtime states.</div>
    </td>
    <td width="25%" style="background-color: #0F172A; border: 1px solid #1E293B; border-radius: 8px; padding: 18px 14px;">
      <div style="color: #A78BFA; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 0.04em;">Consistent</div>
      <div style="color: #94A3B8; font-size: 12px; margin-top: 6px; line-height: 1.5;">Follow a unified design system across terminal logs, notebooks, and web dashboards.</div>
    </td>
    <td width="25%" style="background-color: #0F172A; border: 1px solid #1E293B; border-radius: 8px; padding: 18px 14px;">
      <div style="color: #38BDF8; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 0.04em;">Accessible</div>
      <div style="color: #94A3B8; font-size: 12px; margin-top: 6px; line-height: 1.5;">Usable for everyone; high-contrast syntax highlighting conforming to WCAG 2.1 AA.</div>
    </td>
  </tr>
</table>

---

### 2. Color Palette
*Primary colors used across the application:*

<table width="100%" cellpadding="0" cellspacing="6" border="0">
  <tr align="center">
    <td width="12.5%">
      <div style="background-color: #4F46E5; height: 46px; border-radius: 6px; margin-bottom: 8px;"></div>
      <div style="font-weight: 700; font-size: 12px; color: #F8FAFC;">Primary</div>
      <div style="font-family: monospace; font-size: 10px; color: #94A3B8; margin-top: 2px;">#4F46E5</div>
      <div style="font-size: 10px; color: #64748B; margin-top: 4px;">Brand accent / active CTA</div>
    </td>
    <td width="12.5%">
      <div style="background: linear-gradient(135deg, #7C3AED 0%, #A855F7 100%); height: 46px; border-radius: 6px; margin-bottom: 8px;"></div>
      <div style="font-weight: 700; font-size: 12px; color: #F8FAFC;">Secondary</div>
      <div style="font-family: monospace; font-size: 10px; color: #94A3B8; margin-top: 2px;">#8B5CF6</div>
      <div style="font-size: 10px; color: #64748B; margin-top: 4px;">Adapter badges / secondary UI</div>
    </td>
    <td width="12.5%">
      <div style="background-color: #10B981; height: 46px; border-radius: 6px; margin-bottom: 8px;"></div>
      <div style="font-weight: 700; font-size: 12px; color: #F8FAFC;">Success</div>
      <div style="font-family: monospace; font-size: 10px; color: #94A3B8; margin-top: 2px;">#10B981</div>
      <div style="font-size: 10px; color: #64748B; margin-top: 4px;">Pass verdicts / completed</div>
    </td>
    <td width="12.5%">
      <div style="background-color: #F59E0B; height: 46px; border-radius: 6px; margin-bottom: 8px;"></div>
      <div style="font-weight: 700; font-size: 12px; color: #F8FAFC;">Warning</div>
      <div style="font-family: monospace; font-size: 10px; color: #94A3B8; margin-top: 2px;">#F59E0B</div>
      <div style="font-size: 10px; color: #64748B; margin-top: 4px;">Retries / soft timeouts</div>
    </td>
    <td width="12.5%">
      <div style="background-color: #EF4444; height: 46px; border-radius: 6px; margin-bottom: 8px;"></div>
      <div style="font-weight: 700; font-size: 12px; color: #F8FAFC;">Error</div>
      <div style="font-family: monospace; font-size: 10px; color: #94A3B8; margin-top: 2px;">#EF4444</div>
      <div style="font-size: 10px; color: #64748B; margin-top: 4px;">Failed asserts / errors</div>
    </td>
    <td width="12.5%">
      <div style="background-color: #F8FAFC; border: 1px solid #E2E8F0; height: 46px; border-radius: 6px; margin-bottom: 8px;"></div>
      <div style="font-weight: 700; font-size: 12px; color: #F8FAFC;">Background</div>
      <div style="font-family: monospace; font-size: 10px; color: #94A3B8; margin-top: 2px;">#F8FAFC</div>
      <div style="font-size: 10px; color: #64748B; margin-top: 4px;">Canvas backdrop (Light)</div>
    </td>
    <td width="12.5%">
      <div style="background-color: #FFFFFF; border: 1px solid #E2E8F0; height: 46px; border-radius: 6px; margin-bottom: 8px;"></div>
      <div style="font-weight: 700; font-size: 12px; color: #F8FAFC;">Surface</div>
      <div style="font-family: monospace; font-size: 10px; color: #94A3B8; margin-top: 2px;">#FFFFFF</div>
      <div style="font-size: 10px; color: #64748B; margin-top: 4px;">Cards / modal surfaces</div>
    </td>
    <td width="12.5%">
      <div style="background-color: #0F172A; border: 1px solid #334155; height: 46px; border-radius: 6px; margin-bottom: 8px;"></div>
      <div style="font-weight: 700; font-size: 12px; color: #F8FAFC;">Text Primary</div>
      <div style="font-family: monospace; font-size: 10px; color: #94A3B8; margin-top: 2px;">#0F172A</div>
      <div style="font-size: 10px; color: #64748B; margin-top: 4px;">Primary dark slate text</div>
    </td>
  </tr>
</table>

---

### 3. Typography
*We use Inter as the primary font for a clean, modern look, and JetBrains Mono for execution code:*

<div style="background-color: #0F172A; border: 1px solid #1E293B; border-radius: 8px; padding: 18px 20px; margin: 14px 0;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
      <td width="90" align="center" style="font-size: 42px; font-weight: 800; background-color: #1E293B; color: #F8FAFC; border-radius: 8px; padding: 8px 12px;">Aa</td>
      <td style="padding-left: 20px;">
        <div style="font-size: 18px; font-weight: 700; color: #F8FAFC;">Inter & JetBrains Mono</div>
        <div style="color: #60A5FA; font-size: 12px; font-weight: 600; margin-top: 2px;">Primary font family</div>
        <div style="color: #94A3B8; font-size: 12px; margin-top: 4px;">Clean, modern, and highly readable across code diffs, logs, and technical specifications.</div>
      </td>
    </tr>
  </table>
</div>

| Element | Font Family | Size | Weight | Line Height |
| :-- | :-- | :-: | :-: | :-: |
| **Heading 1 (H1)** | Inter | 24px (1.5rem) | 700 Bold | 1.3 |
| **Heading 2 (H2)** | Inter | 18px (1.125rem) | 600 Semi-Bold | 1.4 |
| **Heading 3 (H3)** | Inter | 14px (0.875rem) | 600 Semi-Bold | 1.4 |
| **Body Text** | Inter | 13px (0.8125rem) | 400 Regular | 1.6 |
| **Code & Stack Traces** | JetBrains Mono | 12px (0.75rem) | 400 Regular / 600 Bold | 1.6 |
| **Status Badges & Pills** | Inter | 11px (0.6875rem) | 600 Semi-Bold | 1.2 |

---

### 4. UI Components
*Standard components to be used throughout the application:*

#### Buttons
<div style="margin: 12px 0;">
  <button style="background-color: #4F46E5; color: #FFFFFF; border: none; border-radius: 6px; padding: 8px 18px; font-size: 12px; font-weight: 600; cursor: pointer; margin-right: 8px;">Primary</button>
  <button style="background-color: #1E293B; color: #E2E8F0; border: 1px solid #475569; border-radius: 6px; padding: 8px 18px; font-size: 12px; font-weight: 600; cursor: pointer; margin-right: 8px;">Secondary</button>
  <button style="background-color: #EF4444; color: #FFFFFF; border: none; border-radius: 6px; padding: 8px 18px; font-size: 12px; font-weight: 600; cursor: pointer;">Destructive</button>
</div>

#### Status Badges
<div style="margin: 12px 0;">
  <span style="background-color: #065F46; color: #A7F3D0; padding: 4px 12px; border-radius: 12px; font-size: 11px; font-weight: 600; letter-spacing: 0.03em; margin-right: 8px;">PASS</span>
  <span style="background-color: #991B1B; color: #FECACA; padding: 4px 12px; border-radius: 12px; font-size: 11px; font-weight: 600; letter-spacing: 0.03em; margin-right: 8px;">RUNTIME ERROR</span>
  <span style="background-color: #92400E; color: #FDE68A; padding: 4px 12px; border-radius: 12px; font-size: 11px; font-weight: 600; letter-spacing: 0.03em; margin-right: 8px;">RETRY (1/2)</span>
  <span style="background-color: #5B21B6; color: #DDD6FE; padding: 4px 12px; border-radius: 12px; font-size: 11px; font-weight: 600; letter-spacing: 0.03em;">LORA ACTIVE</span>
</div>

#### Terminal Execution Card
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
|  [OK] assert max_sub_array_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6             |
|  [OK] assert max_sub_array_sum([1]) == 1                                         |
|  [OK] assert max_sub_array_sum([5, 4, -1, 7, 8]) == 23                          |
+---------------------------------------------------------------------------------+
```
