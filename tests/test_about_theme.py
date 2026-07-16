import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AboutThemeContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = (ROOT / "index.md").read_text(encoding="utf-8")
        cls.head = (ROOT / "_includes/head.html").read_text(encoding="utf-8")
        cls.layout = (ROOT / "_layouts/default.html").read_text(encoding="utf-8")
        cls.scss = (ROOT / "_sass/_site.scss").read_text(encoding="utf-8")

    def test_about_is_a_distinct_editorial_section(self):
        self.assertIn('<section id="about" class="page-section about-section">', self.index)
        self.assertNotIn('<section id="about" class="hero">', self.index)
        self.assertIn('class="about-label">About</p>', self.index)
        self.assertEqual(self.index.count('class="about-copy"'), 1)

    def test_about_tells_a_bounded_research_story(self):
        for text in (
            "East China Normal University",
            "Nuanwa Technology",
            "Uceng Intelligence",
            "memory-augmented embodied agents",
        ):
            self.assertIn(text, self.index)
        for unsupported in ("real-robot", "foundation-model research", "ten-thousand-GPU"):
            self.assertNotIn(unsupported, self.index)

    def test_theme_bootstraps_before_paint(self):
        self.assertIn('localStorage.getItem("site-theme")', self.head)
        self.assertIn('document.documentElement.dataset.theme', self.head)
        self.assertIn('name="theme-color"', self.head)

    def test_theme_toggle_is_accessible_and_persistent(self):
        self.assertIn('class="theme-toggle"', self.layout)
        self.assertIn('type="button"', self.layout)
        self.assertIn('aria-label="Switch to dark theme"', self.layout)
        self.assertIn('localStorage.setItem("site-theme"', self.layout)
        self.assertIn('data-icon="moon"', self.layout)
        self.assertIn('data-icon="sun"', self.layout)

    def test_theme_and_about_styles_are_complete(self):
        for selector in (
            ':root[data-theme="dark"]',
            ".theme-toggle",
            ".about-section",
            ".about-label",
            ".about-copy",
        ):
            self.assertIn(selector, self.scss)
        self.assertIn("prefers-reduced-motion: reduce", self.scss)


if __name__ == "__main__":
    unittest.main()
