"""Usage examples for Stealth Browser Runner."""
from stealth_browser_runner import StealthBrowser, quick_run


def basic_example() -> None:
    """Launch a stealth browser and visit a URL."""
    with StealthBrowser() as browser:
        page = browser.new_page()
        page.goto("https://example.com")
        print("title:", page.title())
        print("URL:", page.url)


def proxy_example() -> None:
    """Use a SOCKS5 proxy for the stealth browser session."""
    proxy = {
        "server": "socks5://gate.example.com:1080",
        "username": "your_username",
        "password": "your_password",
    }
    with StealthBrowser(proxy=proxy, headless=True) as browser:
        page = browser.new_page()
        page.goto("https://httpbin.org/ip")
        print("IP check result:", page.inner_text("body"))


def reproducible_example() -> None:
    """Same seed = same fingerprint every time (useful for debugging)."""
    with StealthBrowser(seed=12345) as browser:
        page = browser.new_page()
        page.goto("https://example.com")
        print("seed demo — page title:", page.title())


def quick_run_example() -> None:
    """One-liner for quick scripts."""
    page = quick_run("https://example.com")
    print("quick_run result — title:", page.title())


if __name__ == "__main__":
    print("=== Basic Example ===")
    basic_example()

    print("\n=== Reproducible Fingerprint ===")
    reproducible_example()
