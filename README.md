# Stealth Browser Runner

<p>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.11+-blue.svg" alt="Python 3.11+"></a>
  <a href="https://github.com/luoshixin93-sudo/stealth-browser-runner/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>

<h3 align="center">A lightweight Playwright-based stealth browser runner with anti-detection and proxy rotation support.</h3>

## Overview

**Stealth Browser Runner** is a Python library that wraps Playwright to provide a browser automation experience that is harder to detect. It uses a patched Firefox profile with realistic browser fingerprints and humanized mouse/click behavior, making automated browsing look more natural to anti-bot systems.

> Inspired by [invisible_playwright](https://github.com/feder-cr/invisible_playwright) — a community-built automation wrapper for stealth browsing.

## How It Works

Anti-bot systems ask two questions. Stealth Browser Runner handles both:

**1. Is this a real browser?**  
Yes — it's Firefox with a carefully crafted stealth profile applied at the fingerprint level.

- Fingerprints (GPU, audio, fonts, screen, canvas) are set deterministically from a seed value
- No JavaScript injection or page-level overrides that can be detected by runtime checks

**2. Is a real person using it?**  
Yes — mouse movements and inputs follow realistic human patterns.

- Every click and hover follows a natural mouse path with Bezier-curve timing, no teleporting
- Each input is byte-identical to a real human input source

## Quick Start

### Installation

```bash
pip install playwright
playwright install firefox
```

### Basic Example

```python
from stealth_browser_runner import StealthBrowser

def main() -> None:
    with StealthBrowser() as browser:
        page = browser.new_page()
        page.goto("https://example.com")
        page.fill("#search", "hello world")
        page.click("#submit")
        print("title:", page.title())

if __name__ == "__main__":
    main()
```

### With Proxy

```python
from stealth_browser_runner import StealthBrowser

proxy = {
    "server": "socks5://your-proxy-host:1080",
    "username": "user",
    "password": "pass",
}

with StealthBrowser(proxy=proxy) as browser:
    page = browser.new_page()
    page.goto("https://example.com")
    print("page loaded via proxy:", page.title())
```

### Reproducible Fingerprint

```python
from stealth_browser_runner import StealthBrowser

# Same seed = same fingerprint every run (useful for debugging)
with StealthBrowser(seed=42) as browser:
    page = browser.new_page()
    page.goto("https://example.com")
```

## Key Features

- **100% Playwright-compatible** — all methods, sync and async, zero API breaking changes
- **Realistic mouse motion** — Bezier-curve paths with human timing
- **Proxy support** — SOCKS5, SOCKS4, HTTP, HTTPS; DNS routed through proxy by default
- **Pinnable fingerprints** — freeze individual fingerprint fields while keeping others random
- **Timezone control** — auto-derived from proxy IP or explicitly set via IANA timezone name
- **Lightweight** — minimal dependencies, simple API

## Requirements

- Python 3.11+
- [Playwright](https://playwright.dev/python/docs/intro) (`pip install playwright`)
- Firefox browser (`playwright install firefox`)

## Disclaimer

This project is for educational and automation purposes only. Use it responsibly and in compliance with the terms of service of any website you interact with.

---

Made with ❤️ for cloud phone automation → [qtphone.com](https://www.qtphone.com/)
