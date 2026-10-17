"""Copy every image setting from the live -2 template into the preview template,
so the preview shows the same photography as live.
Usage: python3 sync_images.py live-in.json preview-product.muto-nad-45.json"""
import json, re, sys
load = lambda f: json.loads(re.sub(r"^/\*.*?\*/", "", open(f).read(), flags=re.S))
L, P = load(sys.argv[1]), load(sys.argv[2])
n = 0
for sk, s in L["sections"].items():
    if sk not in P["sections"]:
        continue
    ps = P["sections"][sk]
    for k, v in s.get("settings", {}).items():
        if "image" in k and ps["settings"].get(k) != v:
            ps["settings"][k] = v; n += 1
    for bk, b in s.get("blocks", {}).items():
        pb = ps.get("blocks", {}).get(bk)
        if not pb:
            continue
        for k, v in b.get("settings", {}).items():
            if "image" in k and pb["settings"].get(k) != v:
                pb["settings"][k] = v; n += 1
json.dump(P, open(sys.argv[2], "w"), ensure_ascii=False, indent=2)
print("synced", n, "image settings")
