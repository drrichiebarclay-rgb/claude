# Builds snippets/muto-bf-review-box.liquid from the REVIEWS.io export. Every quote is checked word for word.
import json, html, re, sys
R = {x['product_review_id']: x for x in json.load(open(sys.argv[1]))}
# id, display name, age (only as the reviewer wrote it), life stage (from their own words), tags, quote ("…" = cut)
L = [
 (51870896,'Adam','46','Trains 4–5 times a week, races Hyrox','Recovery,Sleep,Wearable user',"…my sleep is hitting good to excellent consistently and recovery from work outs hasn't been over 24 hours since I started MUTO.…"),
 (51870911,'Sunjit B.','53','Medic, strength trains 3 times a week','Recovery,Busy life',"…I wanted to slim down my supplements to 1 which met all my needs.…I feel very strong in the gym when lifting weights.…"),
 (51870901,'Kevin','36','Working, already nails the basics','Energy,Busy life',"I'm 36, and I feel as resilient as my 20s.…I'm feeling way sharper at work and I have constant energy throughout the day, no crashes, nothing.…"),
 (51870912,'Fiona S.','','Busy mum of 3','Energy,Busy life',"…My energy levels are better, my HRV has improved and I feel more relaxed in the mornings (which is a rare thing to say as a busy mum of 3!)…"),
 (51870866,'Jonathon R.','Mid 30s','','Energy',"Being in my mid 30s, everything has started to slow down. Muto is providing me with a sense of vitality which I haven’t experienced since my mid 20s…"),
 (51870885,'Michelle F.','','Mum of a 24-year-old son','Energy',"My 24 year old son recommended I try this. I have been using for almost a month and can honestly say I have felt such a difference…"),
 (51870882,'Mathew H.','','Whoop user','Recovery,Energy,Wearable user',"…In the first 4 weeks: My HRV went up by 32%, my resting heart rate dropped by 7% and my average recovery score improved by 26%…"),
 (51870874,'Sam','','Working on work and fitness goals','Energy,Busy life',"…I feel like I have more energy and a clearer mind.…It’s helping massively towards achieving work and fitness goals."),
 (51870876,'Jack','','Oura ring user','Energy,Wearable user',"Tracking through my Oura ring for the past two weeks HRV was up significantly after two days. Energy is up and staying consistent.…"),
 (51870868,'Hugh K.','','Oura ring user','Recovery,Sleep,Wearable user',"I track the effectiveness of my supplements using my Oura ring, and all my key biometrics are improving: recovery, sleep, HRV and RHR…"),
 (51870884,'Matteo M.','','Garmin user','Energy,Sleep,Wearable user',"Since starting taking Muto my energy levels and my sleep has improved drastically (even within the first month)…"),
 (51870864,'Emma F.','','Whoop user','Energy,Wearable user',"Within a few days I had more energy, felt more focussed and my Whoop HRV rose from 80 to 120.…"),
 (51870918,'Josh R.','','Oura ring user','Energy,Wearable user',"…More energy and clear focus when I start my day. HRV is up on my oura ring, and feeling good.…"),
 (51870903,'Tom L.','','Whoop user','Recovery,Wearable user',"…30 days taking MUTO my recovery is still consistently green (whoop), I'm now starting to see an increase in HRV for my first time ever.…"),
 (51870895,'Russell','','Oura ring user','Wearable user',"…Already noticed a positive difference in my HRV through my OURA ring data.…"),
 (52482185,'Rebeca, San José','','Training for the Boston Marathon','Recovery,Energy',"I started taking Muto for my Boston Marathon training hoping to have better recovery; and it did not disappoint.…I feel very energetic every day."),
 (51870867,'Ayo P.','','Keen runner','Recovery',"As a keen runner, I’ve noticed how Muto has helped me recover faster meaning I can train harder, more often.…"),
 (51870907,'Linzey R.','','Endurance sport, trains most days','Recovery',"I do a lot of endurance sport and train most days…My HRV is averaging higher and I feel better in myself. I am recovering quicker too.…"),
 (52431255,'Alexandra, Bearsden','','Tracks her HRV','Recovery,Energy',"…definitely feel more focused during the day and that my recovery is quicker and better than normal.…"),
 (51870902,'Abraham S.','','Has tracked recovery and HRV for years','Recovery',"…The biggest shift was in my HRV: even after hard sessions, I woke up feeling recovered instead of drained.…"),
 (51870889,'K R','','Bought it for healthy ageing','Recovery,Sleep',"…bought it to support healthy ageing and have been genuinely surprised at how quickly I felt a difference. My recovery and sleep have noticeably improved.…"),
 (51870863,'Danny S.','','','Energy,Sleep',"…I have sustained energy, I sleep better, perform better in workouts, and don’t crash anymore."),
 (51870872,'Beth','','','Sleep,Energy',"I've been using for one month now and really feel the difference! Better sleep, better skin, more energy - happy days!"),
 (51870888,'Holly P.','','','Sleep,Energy',"I didn't realise how flat I'd been feeling until this helped lift me out of it. More vitality, brighter mood, and deeper sleep."),
 (51870906,'George','','','Sleep,Recovery',"After just 2 weeks of taking Muto, I saw a 20% uptick in my HRV and noticeably better sleep.…"),
 (51870879,'Fiona L.','','','Sleep',"Has definitely helped my sleep and reduced my sugar cravings in the evening massively."),
 (54717775,'Lynda, Preston','','','Sleep,Energy',"3 mths in and having the best sleep - no afternoon slump and in general feeling great"),
 (51870873,'Becca','','Struggles with mornings','Energy',"…I predominantly struggle with mornings but already feel myself finding these easier, having more energy throughout the whole day…"),
 (51870877,'Brendan','','','Recovery,Energy',"Started using muto because I felt like my body couldn’t keep up with the amount of exercise I wanted to do. After taking muto, I felt more energised and ready for my next session!…"),
 (51870926,'Lotti','','','Recovery,Energy',"Muto has so much more science behind it than the average supplement brand.…I've been using it for a month and I already feel better and have noticed improved recovery and energy."),
 (51870897,'Qasim M.','','','',"…The product is clearly well thought-out, science-led, and supported by real-world results."),
 (51870890,'Amy C.','','','',"I love that this replaces multiple products. The quality feels high and the results have been real – more vitality and better overall wellbeing."),
 (51870904,'T. F.','','','',"…What i am here to say is that I have NEVER experience such a high level of customer service as with this company.…"),
 (51870920,'Catalin-Constantin M.','','','',"…the way that they have done their branding along with explaining the science behind longevity is top quality. Dr Richie Barclay knows his stuff."),
]
FILTERS = ['Energy','Recovery','Sleep','Busy life','Wearable user']
norm = lambda s: re.sub(r"\s+", " ", html.unescape(s).replace('’', "'").replace('‘', "'")).strip()
bad = 0
for (i, n, a, st, tg, q) in L:
  src = norm(R[i]['review'])
  for part in [p.strip() for p in q.split('…') if p.strip()]:
    if norm(part) not in src: print('NOT VERBATIM', i, part); bad += 1
  if 51870930 <= i <= 51870962: print('EXCLUDED RANGE', i); bad += 1
  if a and a.lower() not in src.lower() and a.replace(' ','') not in src.replace(' ',''):
    if not (a == '53' and '53year' in src): print('AGE NOT IN TEXT', i, a); bad += 1
  for t in filter(None, tg.split(',')):
    assert t in FILTERS, t
if bad: sys.exit('fix the list')
counts = {f: sum(f in tg.split(',') for (_, _, _, _, tg, _) in L) for f in FILTERS}
print('reviews', len(L), counts)
e = lambda s: html.escape(s, quote=True)
slides = []
for k, (i, n, a, st, tg, q) in enumerate(L):
  v = R[i]['reviewer'].get('verified_buyer') == 'yes'
  stars = int(R[i]['rating'])
  who = '<b>' + e(n) + (', ' + e(a) if a else '') + '</b>'
  if st: who += '<i>' + e(st) + '</i>'
  who += '<span>' + ('Verified buyer' if v else 'Reviewed on REVIEWS.io') + '</span>'
  slides.append(
    '    <figure class="mc-rv__slide" data-tags="|' + '|'.join(filter(None, tg.split(','))) + '|" data-rid="' + str(i) + '"' + ('' if k == 0 else ' aria-hidden="true"') + '>\n'
    '      <div class="mc-rv__top"><span class="mc-rv__stars" role="img" aria-label="' + str(stars) + ' out of 5 stars">' + '★' * stars + '☆' * (5 - stars) + '</span></div>\n'
    '      <blockquote class="mc-rv__q">“' + e(q) + '”</blockquote>\n'
    '      <figcaption class="mc-rv__who">' + who + '</figcaption>\n'
    '    </figure>')
chips = '\n'.join('    <button type="button" class="mc-rv__chip" data-f="' + e(f) + '" aria-pressed="' + ('true' if f == 'All' else 'false') + '">' + e(f) + '</button>' for f in ['All'] + FILTERS)
tpl = open(sys.argv[2]).read()
out = tpl.replace('%%SLIDES%%', '\n'.join(slides)).replace('%%CHIPS%%', chips).replace('%%N%%', str(len(L)))
open(sys.argv[3], 'w').write(out)
print('written', sys.argv[3])
