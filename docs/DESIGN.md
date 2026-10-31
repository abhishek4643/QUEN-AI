# Design System

**Qwen2.5-Coder Autonomous AI Code Generation Engine**  
*Clean. Simple. Productive. UI Tokens, API Schemas, and Terminal Telemetry Specifications*

---

This document defines the visual design system, UI tokens, color palette, typography, and API interface guidelines for the Qwen2.5-Coder ecosystem, including web dashboards, interactive notebooks, and CLI telemetry outputs.

---

## 1. Design Principles

* **User-Centered**: Present execution tracebacks and self-correction iterations with immediate clarity.
* **Minimal & Clean**: Reduce visual clutter and focus developers on code diffs and test results.
* **Consistent**: Standardize status colors, badges, and schemas across REST APIs, notebooks, and terminal logs.
* **Accessible**: High-contrast ratios (> 4.5:1) ensuring readability in both dark and light development themes.

---

## 2. Color Palette

Primary brand, semantic feedback, and dark-theme surface colors:

| Token Name | Hex Code | Preview | Usage & Semantic Purpose |
| :--- | :--- | :--- | :--- |
| **Primary** | `#6366F1` | Indigo | Brand accent, primary buttons, active tabs, highlighted code keywords |
| **Secondary** | `#8B5CF6` | Purple | Model badge, LoRA adapter indicators, secondary actions |
| **Success** | `#10B981` | Emerald | Test `PASS` status, 100% benchmark badge, verified execution alerts |
| **Warning** | `#F59E0B` | Amber | Self-correction in-progress warnings, retries, soft timeouts |
| **Error** | `#EF4444` | Rose | Execution failure, syntax error traceback, assertion mismatch |
| **Background** | `#0F172A` | Slate 900 | Main dark canvas, root application background, terminal backdrop |
| **Surface** | `#1E293B` | Slate 800 | Elevated code cards, sandbox output blocks, modal dialogs |
| **Text Primary** | `#F8FAFC` | Slate 50 | Primary body text, code characters, headings |
| **Text Secondary**| `#94A3B8` | Slate 400 | Subtitles, parameter descriptions, line numbers, timestamps |

---

## 3. Typography

* **Code & Monospace Font**: `JetBrains Mono`, `Fira Code`, `SF Mono`, `monospace`
  * Weight: `400 Regular` for code body, `600 Semi-Bold` for function definitions and keywords.
  * Line Height: `1.6` for optimal readability during debugging.
* **Prose & Interface Font**: `Inter`, `-apple-system`, `sans-serif`
  * Headings: `600 Semi-Bold` / `700 Bold`.
  * Hierarchy:
    * `H1`: 24px (1.5rem)
    * `H2`: 18px (1.125rem)
    * `H3`: 14px (0.875rem)
    * `Body`: 13px (0.8125rem)
    * `Caption`: 11px (0.6875rem)

---

## 4. UI Components & Terminal Visuals

### 4.1 Status Badges

```text
[ PASS ]        Background: #10B981 | Text: #FFFFFF | Border-Radius: 4px
[ RUNTIME_ERR ] Background: #EF4444 | Text: #FFFFFF | Border-Radius: 4px
[ RETRY (1/2) ] Background: #F59E0B | Text: #000000 | Border-Radius: 4px
[ LORA ACTIVE ] Background: #8B5CF6 | Text: #FFFFFF | Border-Radius: 4px
```

### 4.2 Terminal Output Card Layout

```
+-------------------------------------------------------------------------------+
|  Qwen2.5-Coder Sandbox Telemetry                           [ PASS (0.42s) ]   |
+-------------------------------------------------------------------------------+
|  Problem: "Write a function to find maximum subarray sum (Kadane's Algo)"      |
|  Function Name: max_sub_array_sum                                             |
|                                                                               |
|  >>> Code Implementation:                                                     |
|  1 | def max_sub_array_sum(arr):                                              |
|  2 |     max_so_far = current_max = arr[0]                                    |
|  3 |     for x in arr[1:]:                                                    |
|  4 |         current_max = max(x, current_max + x)                            |
|  5 |         max_so_far = max(max_so_far, current_max)                        |
|  6 |     return max_so_far                                                    |
|                                                                               |
|  >>> Execution Verdict:                                                       |
|  [✓] assert max_sub_array_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6           |
|  [✓] assert max_sub_array_sum([1]) == 1                                       |
|  [✓] assert max_sub_array_sum([5, 4, -1, 7, 8]) == 23                        |
+-------------------------------------------------------------------------------+
```

---

## 5. Layout & Spacing System

* **Grid Base**: 4px base increment (`4px`, `8px`, `12px`, `16px`, `24px`, `32px`).
* **Container Padding**: 16px padding on mobile, 24px padding on desktop cards.
* **Border Radii**:
  * Micro (badges, tags): `4px`
  * Standard (input fields, code blocks): `8px`
  * Containers (cards, popups): `12px`

---

## 6. Interactive Error States

* **Traceback Highlighting**: Error lines render with an `#EF4444` left border and an `#1E1B4B` tinted background block.
* **Diff View**:
  * Removed erroneous code: Background `#7F1D1D` (`-` prefix).
  * Injected self-correction patch: Background `#064E3B` (`+` prefix).

