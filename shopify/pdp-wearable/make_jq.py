"""Turn the build (make_wearable.py output) into a jq program that edits the live template in place.
Usage: python3 make_jq.py > wearable.jq"""
import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
def load(p):
    raw = open(p).read(); return json.loads(raw[raw.index('*/') + 2:] if raw.lstrip().startswith('/*') else raw)
A = load(os.path.join(HERE, "base/live__product.muto-nad-bf-premium.json"))
B = load(os.path.join(HERE, "product.muto-nad-wearable.json"))
ops = []
J = lambda x: json.dumps(x, ensure_ascii=False)
def path(p): return J(p)
def walk(a, b, p):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in a:
            if k not in b: ops.append("delpaths([%s])" % path(p + [k]))
        for k in b:
            if k not in a: ops.append("setpath(%s; %s)" % (path(p + [k]), J(b[k])))
            else: walk(a[k], b[k], p + [k])
    elif a != b:
        if isinstance(a, str) and isinstance(b, str) and len(a) > 2000:
            raise SystemExit("long string at %s: handled separately" % p)
        ops.append("setpath(%s; %s)" % (path(p), J(b)))
# Long custom-liquid strings: literal replacements (split/join), not full copies
LONG = [["sections", "head_styles", "settings", "custom_liquid"], ["sections", "ag1_plans", "settings", "custom_liquid"]]
for p in LONG:
    a, b = A, B
    for k in p: a, b = a[k], b[k]
    # find the changed middle: common prefix and suffix
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]: i += 1
    j = 0
    while j < min(len(a), len(b)) - i and a[-1 - j] == b[-1 - j]: j += 1
    old, new = a[i:len(a) - j], b[i:len(b) - j]
    # widen to a unique anchor
    while a.count(old) != 1 or not old:
        i -= 1; old, new = a[i] + old, b[i] + new
    ops.append("(getpath(%s) | split(%s) | join(%s)) as $v | setpath(%s; $v)" % (path(p), J(old), J(new), path(p)))
    for d_ in (A, B):
        x = d_
        for k in p[:-1]: x = x[k]
        x[p[-1]] = None
walk(A, B, [])
print(" | ".join(ops))
