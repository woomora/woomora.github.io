#!/usr/bin/env python3
"""Keep the job market paper's abstract on the research page in step with the published PDF.

Reads the abstract from page one of the paper, between its "Abstract" and
"Keywords" headings, and writes it between the markers in research.md. Prints
what it did, and fails without touching the page if the text it reads looks
wrong, so a bad extraction never reaches the site.
"""

import io
import pathlib
import re
import sys
import urllib.request

PDF_URL = "https://woomora.github.io/JMP/WOO-MORA-JMP.pdf"
PAGE = pathlib.Path(__file__).resolve().parent.parent / "research.md"
START, END = "<!-- jmp-abstract:start -->", "<!-- jmp-abstract:end -->"


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "woomora.github.io abstract updater"})
    with urllib.request.urlopen(request, timeout=180) as response:
        return response.read()


def abstract_of(pdf):
    from pdfminer.high_level import extract_text
    from pdfminer.layout import LAParams

    # word_margin 0.1 keeps the spaces that justified lines would otherwise lose
    text = extract_text(io.BytesIO(pdf), page_numbers=[0],
                        laparams=LAParams(word_margin=0.1, char_margin=2.0, line_margin=0.5))
    found = re.search(r"\bAbstract\b(.*?)\bKeywords\b", text, re.S)
    if not found:
        sys.exit("No abstract found between 'Abstract' and 'Keywords' on page one.")
    return " ".join(found.group(1).split())


def checked(abstract):
    words = abstract.split()
    longest = max(words, key=len) if words else ""
    problems = []
    if not 120 <= len(words) <= 400:
        problems.append("%d words" % len(words))
    if not abstract[:1].isupper():
        problems.append("does not start with a capital letter")
    if not abstract.endswith("."):
        problems.append("does not end with a full stop")
    if len(longest) > 30:
        problems.append("words ran together: %s" % longest[:40])
    if problems:
        sys.exit("The abstract read from the paper looks wrong (%s). research.md left untouched."
                 % "; ".join(problems))
    return abstract


def main():
    page = PAGE.read_text(encoding="utf-8")
    block = re.search(re.escape(START) + r"\n(.*?)\n" + re.escape(END), page, re.S)
    if not block:
        sys.exit("The markers around the abstract are missing from research.md.")

    abstract = checked(abstract_of(fetch(PDF_URL)))
    if abstract == block.group(1):
        print("The abstract on the research page already matches the paper (%d words)."
              % len(abstract.split()))
        return

    PAGE.write_text(page[:block.start(1)] + abstract + page[block.end(1):], encoding="utf-8")
    print("Updated the abstract on the research page (%d words, was %d)."
          % (len(abstract.split()), len(block.group(1).split())))


if __name__ == "__main__":
    main()
