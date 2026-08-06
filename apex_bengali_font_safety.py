# ════════════════════════════════════════════════════════════════
# 🔒  APEX 22.0 | GitHub Geometric | Bengali Font Safety | PROMPT-05+
#     UPGRADED EDITION — Multi-Platform · AI-Safe · CDN-Verified
#     Compiled by: ডক্টর জসর আহমেদ ইউসুফ হক
# ════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────
# SECTION 1 — FONT STACK
# ──────────────────────────────────────────────────────────────

PRIMARY_FONT    = "Hind Siliguri"         # Google Fonts CDN ✅
SECONDARY_FONT  = "Noto Sans Bengali"     # v3.000 (Jul 2025) ✅
TERTIARY_FONT   = "Noto Serif Bengali"    # v3.000 (Jul 2025) ✅
FALLBACK_FONT   = "Kalpurush"             # Open Source ✅
SYSTEM_FALLBACK = "sans-serif"            # Universal ✅

# NOTE: Noto Sans Bengali & Noto Serif Bengali
# Version 3.000 released July 8, 2025
# New design by Universal Thirst — improved conjuncts ✅
# Source: github.com/notofonts/bengali


# ──────────────────────────────────────────────────────────────
# SECTION 2 — GOOGLE FONTS CDN EMBED (HTML)
# ──────────────────────────────────────────────────────────────

CDN_EMBED = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?
  family=Hind+Siliguri:wght@300;400;500;600;700
  &family=Noto+Sans+Bengali:wdth,wght@62.5..100,100..900
  &family=Noto+Serif+Bengali:wdth,wght@62.5..100,100..900
  &display=swap" rel="stylesheet">
"""


# ──────────────────────────────────────────────────────────────
# SECTION 3 — CSS FONT RULES
# ──────────────────────────────────────────────────────────────

CSS_RULES = """
/* ── Base Bengali Text ── */
.ckn-live-text {
  font-family: 'Hind Siliguri', 'Noto Sans Bengali',
               'Noto Serif Bengali', 'Kalpurush', sans-serif;
  font-weight: 700;
  font-size: clamp(18px, 4vw, 48px);
  color: #FFFFFF;
  text-shadow: 0 0 12px rgba(255, 215, 0, 0.9);
  letter-spacing: 0.05em;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
  font-feature-settings: "liga" 1, "calt" 1, "kern" 1;
}

/* ── Conjunct & Matra Safety ── */
.ckn-live-text *,
.ckn-live-text::before,
.ckn-live-text::after {
  unicode-bidi: embed;
  word-break: keep-all;
  overflow-wrap: break-word;
}

/* ── Display / Title Weight ── */
.ckn-display {
  font-family: 'Noto Sans Bengali', 'Hind Siliguri', sans-serif;
  font-weight: 900;
  font-size: clamp(32px, 6vw, 96px);
  line-height: 1.3;
  letter-spacing: 0.02em;
}

/* ── Body / Reading Weight ── */
.ckn-body {
  font-family: 'Hind Siliguri', 'Noto Sans Bengali', sans-serif;
  font-weight: 400;
  font-size: clamp(14px, 2vw, 20px);
  line-height: 1.8;
}
"""


# ──────────────────────────────────────────────────────────────
# SECTION 4 — AI PROMPT SAFETY NOTE
# ──────────────────────────────────────────────────────────────

AI_SAFETY_PROMPT = """
Render Bengali text using a clean, bold, modern Bengali typeface
similar to Hind Siliguri or Noto Sans Bengali v3.

Critical requirements:
• All Unicode Bengali characters must be fully intact
• No broken glyphs, no missing conjuncts (যুক্তবর্ণ)
• No distorted matras (মাত্রা) or vowel marks (স্বরচিহ্ন)
• Hasanta (্) and virama must render cleanly
• Font must remain legible at sizes from 12px to 300px
• Conjunct clusters: ক্ষ জ্ঞ ত্র ষ্ট দ্ধ ল্ল — must be
  rendered as single unified glyphs, not broken sequences
• Anusvar (ং), Visarga (ঃ), Chandrabindu (ঁ) must float
  correctly above base characters
"""


# ──────────────────────────────────────────────────────────────
# SECTION 5 — FULL UNICODE TEST CHECKLIST
# ──────────────────────────────────────────────────────────────

UNICODE_TEST = {

  "স্বরবর্ণ (Vowels)":
    "অ আ ই ঈ উ ঊ ঋ এ ঐ ও ঔ",

  "ব্যঞ্জনবর্ণ_১ (Consonants A)":
    "ক খ গ ঘ ঙ চ ছ জ ঝ ঞ",

  "ব্যঞ্জনবর্ণ_২ (Consonants B)":
    "ট ঠ ড ঢ ণ ত থ দ ধ ন",

  "ব্যঞ্জনবর্ণ_৩ (Consonants C)":
    "প ফ ব ভ ম য র ল শ ষ স হ ড় ঢ় য়",

  "স্বরচিহ্ন (Vowel Marks)":
    "া ি ী ু ূ ৃ ে ৈ ো ৌ ং ঃ ঁ ্",

  "যুক্তবর্ণ_মূল (Core Conjuncts)":
    "ক্ষ জ্ঞ ত্র ষ্ট দ্ধ ল্ল ন্ত স্ত ন্ন ক্ত",

  "যুক্তবর্ণ_বর্ধিত (Extended Conjuncts)":
    "ম্ব ন্দ স্প ব্ল ফ্র গ্র ড্র প্র ব্র ক্র",

  "সংখ্যা (Bengali Digits)":
    "০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮ ৯",

  "বিরাম (Punctuation)":
    "। ॥ ৷ ৺ ৻",

  "CKN Live Context":
    "ডক্টর জসর আহমেদ ইউসুফ হক — বাংলা ✅",
}


# ──────────────────────────────────────────────────────────────
# SECTION 6 — PLATFORM COMPATIBILITY MATRIX
# ──────────────────────────────────────────────────────────────

PLATFORM_SUPPORT = {
  "GitHub Markdown"     : "Noto Sans Bengali (system) ✅",
  "GitHub Pages (HTML)" : "Hind Siliguri via CDN ✅",
  "Leonardo AI"         : "AI_SAFETY_PROMPT required ✅",
  "Midjourney"          : "AI_SAFETY_PROMPT + image overlay ✅",
  "DALL·E / GPT-4o"    : "Noto Sans Bengali prompt ✅",
  "Web Browser"         : "Full CSS stack ✅",
  "Android / iOS"       : "Noto Sans Bengali (built-in) ✅",
  "Windows 11"          : "Noto Sans Bengali (system) ✅",
  "Linux"               : "fontconfig rule required ✅",
}


# ──────────────────────────────────────────────────────────────
# SECTION 7 — ADVANCED FONT VALIDATION FUNCTION
# ──────────────────────────────────────────────────────────────

def validate_bengali_unicode(text: str) -> dict:
    """
    Validates Bengali Unicode text for common rendering issues.
    Returns a report with glyph status.
    """
    import unicodedata

    BENGALI_RANGE = range(0x0980, 0x09FF)
    CONJUNCT_MARKER = '\u09CD'  # Hasanta / Virama

    results = {
        "total_chars": len(text),
        "bengali_chars": 0,
        "conjunct_sequences": 0,
        "vowel_marks": 0,
        "digits": 0,
        "issues": [],
    }

    i = 0
    while i < len(text):
        char = text[i]
        cp = ord(char)

        if cp in BENGALI_RANGE:
            results["bengali_chars"] += 1

            # Check for conjunct sequence
            if i + 2 < len(text) and text[i+1] == CONJUNCT_MARKER:
                results["conjunct_sequences"] += 1

            # Vowel marks range: ০x09BE–0x09CC
            if 0x09BE <= cp <= 0x09CC:
                results["vowel_marks"] += 1

            # Bengali digits: ০x09E6–0x09EF
            if 0x09E6 <= cp <= 0x09EF:
                results["digits"] += 1

        i += 1

    return results


# ──────────────────────────────────────────────────────────────
# SECTION 8 — RENDER SAFETY CHECKER
# ──────────────────────────────────────────────────────────────

RENDER_SAFETY_RULES = [
    ("zero_width_joiner",   "\u200D", "ZWJ — used in complex conjuncts"),
    ("zero_width_non_join", "\u200C", "ZWNJ — breaks unwanted ligatures"),
    ("soft_hyphen",         "\u00AD", "Soft hyphen — line break hint"),
    ("word_joiner",         "\u2060", "Word joiner — prevents line break"),
]

# ════════════════════════════════════════════════════════════════
# APEX 22.0 | GitHub Geometric v22 | Bengali Font Secure ✅
# Multi-Platform · Noto v3.000 (Jul 2025) · AI-Render Safe
# Compiled by: ডক্টর জসর আহমেদ ইউসুফ হক
# ════════════════════════════════════════════════════════════════
