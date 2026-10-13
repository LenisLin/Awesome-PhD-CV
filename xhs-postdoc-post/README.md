# Xiaohongshu public postdoc CV assets

This folder contains a public, redacted Xiaohongshu post package for 2027 postdoc / interview opportunity discovery.

## Files

- `xhs_postdoc_cv_public.tex`: one-page public CV source.
- `xhs_postdoc_cv_public.pdf`: compiled public CV.
- `xhs_postdoc_cv_public.png`: image used for Xiaohongshu image-text posting.
- `generate_cover.py`: generates the Chinese cover image.
- `xhs_cover.png`: first image for the Xiaohongshu post.
- `xhs_title.txt`: title used by the Xiaohongshu CLI.
- `xhs_content.txt`: body text used by the Xiaohongshu CLI.

## Redaction policy

Retained:
- Name: Yuxiang Lin.
- Current role: Ph.D. Candidate in Computational Biology and Bioinformatics, Xiamen University, expected 2027.
- Preferred regions: Singapore and North America.
- Research fit: spatial transcriptomics, tumor microenvironment, multi-omics medicine, biomedical AI agents.
- Public profile: `https://lenislin.github.io/`.

Removed or intentionally not shown:
- Email address.
- ORCID.
- Full Google Scholar URL.
- Full GitHub URL.
- GPA.
- Advisor name and advisor link.
- Full publication list.

## Regeneration

Run from this directory:

```bash
xelatex -interaction=nonstopmode xhs_postdoc_cv_public.tex
pdftoppm -png -r 300 -singlefile xhs_postdoc_cv_public.pdf xhs_postdoc_cv_public
python3 generate_cover.py
```

## Verification

```bash
pdftotext xhs_postdoc_cv_public.pdf -
pdfinfo xhs_postdoc_cv_public.pdf
```

The extracted text should not contain the original email, ORCID, Google Scholar URL, GitHub URL, GPA, or advisor name.

## Xiaohongshu review flow

Only use the local Xiaohongshu skill CLI:

```bash
cd /home/lenislin/.codex/skills/xiaohongshu-skills
python scripts/cli.py check-login
python scripts/cli.py fill-publish \
  --title-file /home/lenislin/Experiment/projects/Lecture/Awesome-PhD-CV/xhs-postdoc-post/xhs_title.txt \
  --content-file /home/lenislin/Experiment/projects/Lecture/Awesome-PhD-CV/xhs-postdoc-post/xhs_content.txt \
  --images /home/lenislin/Experiment/projects/Lecture/Awesome-PhD-CV/xhs-postdoc-post/xhs_cover.png \
           /home/lenislin/Experiment/projects/Lecture/Awesome-PhD-CV/xhs-postdoc-post/xhs_postdoc_cv_public.png
```

After the browser preview is manually reviewed, publish only with explicit user confirmation:

```bash
python scripts/cli.py click-publish
```

If the post is not published, save the draft rather than discarding the browser tab.
