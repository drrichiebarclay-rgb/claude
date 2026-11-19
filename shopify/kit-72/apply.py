"""MUTO: welcome kit worth £72, not £87, on every page (Richie, 19 Nov 2026).

live/ holds the live theme's files as fetched on 19 Nov (every template, the header and footer groups and the
offer-card section). Each file that still says £87 is copied to theme/ with the figure changed to £72. Nothing
else in those files is touched. The offer-card section takes the figure from snippets/muto-offer.liquid (the
single source added in the main product page work), so it cannot drift again. Run: python3 apply.py
"""
import glob, os, re, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
shutil.rmtree(os.path.join(HERE, "theme"), ignore_errors=True)
n_files = 0
for p in sorted(glob.glob(os.path.join(HERE, "live", "**", "*"), recursive=True)):
    if not os.path.isfile(p):
        continue
    src = open(p, encoding="utf-8", newline="").read()
    if "£87" not in src:
        continue
    rel = os.path.relpath(p, os.path.join(HERE, "live"))
    # every £87 in these files is the welcome-kit figure: check that before changing any
    for m in re.finditer("£87", src):
        ctx = src[max(0, m.start() - 40):m.end()]
        if not re.search(r"kit worth £87$", ctx):
            raise SystemExit(f"{rel}: an £87 that is not the kit worth: {ctx!r}")
    if rel == "sections/muto-sci.liquid":
        out = src.replace("free welcome kit worth £87", "free welcome kit worth {% render 'muto-offer', key: 'kit3' %}")
    else:
        out = src.replace("kit worth £87", "kit worth £72")
    assert "£87" not in out
    q = os.path.join(HERE, "theme", rel)
    os.makedirs(os.path.dirname(q), exist_ok=True)
    open(q, "w", encoding="utf-8", newline="").write(out)
    print(rel, src.count("£87"))
    n_files += 1
print(n_files, "files")
