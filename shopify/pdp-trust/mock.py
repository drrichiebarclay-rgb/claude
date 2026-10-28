import json,html,sys
sp=sys.argv[1]
c=open('theme/templates/product.muto-nad-45.json').read(); d=json.loads(c[c.index('{'):]); S=d['sections']
e=html.escape; br=lambda s:e(s).replace('\n','<br>')
SPK='<span class="mc__trust-spark"></span>'
out=[]
st=S['statement']['settings']
out.append(f'<div class="mc mc--stm"><div class="mc__wrap"><section class="mc__stm"><h2 class="mc__h2 mc__stm-head">{br(st["heading"])}</h2><p class="mc__stm-sub">{e(st["sub"])}</p></section></div></div>')
s=S['standards']; ss=s['settings']; items=''
for i,k in enumerate(s['block_order'],1):
    b=s['blocks'][k]['settings']
    tail=(f'<p class="mc__trust-label mc__std-note">{b["no_link_note"]}</p>' if b['no_link_note'] and not b['link'] else '')
    items+=f'<li class="mc__std-item"><div class="mc__std-meta"><span class="mc__trust-label mc__std-num">0{i}</span><span class="mc__trust-tag">{SPK}{e(b["stat"])}</span></div><h3 class="mc__std-title">{e(b["title"])}</h3><div class="mc__rt mc__std-text">{b["text"]}</div>{tail}</li>'
out.append(f'<div class="mc mc--std"><div class="mc__wrap"><section class="mc__std"><div class="mc__trust-top"><h2 class="mc__h2">{br(ss["heading"])}</h2><p class="mc__trust-note">{e(ss["lede"])}</p></div><ol class="mc__std-list">{items}</ol></section></div></div>')
r=S['reviews_top']; rs=r['settings']; cards=''
for k in r['block_order']:
    b=r['blocks'][k]['settings']
    cards+=f'<li class="mc__rev-card"><p class="mc__rev-stars">★★★★★</p><p class="mc__trust-tag mc__rev-topic">{SPK}{e(b["topic"])}</p><blockquote class="mc__rev-quote">“{e(b["quote"])}”</blockquote><p class="mc__rev-who"><span class="mc__rev-name">{e(b["name"])}</span><span class="mc__trust-label mc__rev-ver">✓ Verified buyer</span></p></li>'
out.append(f'<div class="mc mc--rev"><div class="mc__wrap"><section class="mc__rev"><div class="mc__trust-top"><h2 class="mc__h2">{br(rs["heading"])}</h2><div class="mc__rev-side"><p class="mc__trust-note">{e(rs["eyebrow"])}</p><div class="mc__rev-nav"><button class="mc__rev-btn">←</button><p class="mc__trust-label mc__rev-count">01 / 0{len(r["block_order"])}</p><button class="mc__rev-btn">→</button></div></div></div><ul class="mc__rev-rail mc__rail">{cards}</ul><p class="mc__rev-foot">{e(rs["foot"])}</p></section></div></div>')
f=S['founder']; fs=f['settings']; facts=''.join(f'<div class="mc__fdr-fact"><dt class="mc__trust-label">{e(f["blocks"][k]["settings"]["label"])}</dt><dd>{e(f["blocks"][k]["settings"]["value"])}</dd></div>' for k in f['block_order'])
out.append(f'<div class="mc mc--fdr"><div class="mc__wrap"><section class="mc__fdr"><div class="mc__fdr-media"><div class="mc__fdr-frame"><div class="mh__slot"><img class="mh__img" src="portrait.jpg" alt=""></div></div></div><div class="mc__fdr-copy"><p class="mc__trust-label mc__fdr-eyebrow">{fs["eyebrow"]}</p><h2 class="mc__h2 mc__fdr-head">{br(fs["heading"])}</h2><div class="mc__rt mc__fdr-text">{fs["text"]}</div><figure class="mc__fdr-quote"><blockquote>{e(fs["quote"])}</blockquote><figcaption class="mc__trust-label">{e(fs["quote_by"])}</figcaption></figure><dl class="mc__fdr-facts">{facts}</dl><a class="mc__trust-link" href="#">{fs["link_label"]} →</a></div></section></div></div>')
crea=open(sp+'/muto-crea.css').read(); css=crea+open('theme/assets/muto-crea-trust.css').read()+open(sp+'/muto-home.css').read()+crea
open(sp+'/mock.html','w').write(f'<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width"><style>body{{margin:0}}{css}</style>'+''.join(out))
